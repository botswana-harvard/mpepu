from edc.core.bhp_common.utils import convert_from_camel
from edc.dashboard.subject.classes import RegisteredSubjectDashboard
from edc.subject.registration.models import RegisteredSubject

from apps.mpepu_infant.models import InfantBirth
from apps.mpepu_maternal.models import MaternalConsent, MaternalVisit, MaternalLabDel, MaternalLocator
from apps.mpepu_lab.models import MaternalRequisition, PackingList


class MaternalDashboard(RegisteredSubjectDashboard):

    view = 'maternal_dashboard'
    dashboard_name = 'Maternal Dashboard'
    dashboard_url_name = 'subject_dashboard_url'

    def __init__(self, *args, **kwargs):
        self._visit_model = MaternalVisit
        self._registered_subject = None
        self._dashboard_type_list = ['maternal']
        self.extra_url_context = ""
        kwargs.update({'dashboard_models': {'maternal_consent': MaternalConsent}, 'membership_form_category': 'maternal'})
        self._locator_model = None
        self._requisition_model = None
        super(MaternalDashboard, self).__init__(*args, **kwargs)

    def add_to_context(self):
        super(MaternalDashboard, self).add_to_context()
        self.context.add(
            home='mpepu',
            infants=self.get_infants(),
            search_name='maternal',
            infant_dashboard_url=self.get_infant_dashboard_url(),
            title='Maternal Dashboard',
            delivery_datetime=self.get_delivery_datetime(),
            maternal_consent=self.consent
            )

    @property
    def consent(self):
        self._consent = None
        if MaternalConsent.objects.filter(subject_identifier=self.subject_identifier):
            self._consent = MaternalConsent.objects.get(subject_identifier=self.subject_identifier)
        return self._consent

    def set_registered_subject(self, pk=None):
        self._registered_subject = self.registered_subject
        if RegisteredSubject.objects.filter(subject_identifier=self.subject_identifier):
            self._registered_subject = RegisteredSubject.objects.get(subject_identifier=self.subject_identifier)

    def get_registered_subject(self):
        if not self._registered_subject:
            self.set_registered_subject()
        return self._registered_subject

    def set_membership_form_category(self, category):
        self._membership_form_category = 'maternal'

    def get_infant_dashboard_url(self):
        return 'subject_dashboard_url'

    def set_dashboard_type_list(self):
        self._dashboard_type_list = ['maternal']

    def get_subject_identifier(self):
        return self.subject_identifier

    def get_visit_model(self):
        return MaternalVisit

    def get_requisition_model(self):
        return MaternalRequisition

    def get_locator_model(self):
        return MaternalLocator

    def get_locator_scheduled_visit_code(self):
        """ Returns visit where the locator is scheduled, TODO: maybe search visit definition for this?."""
        return '1000M'

    def get_packing_list_model(self):
        return PackingList

    def get_infants(self):
        """Returns a list of infants identifiers asssociated with the maternal subject_identifier by querying the Birth model or RegisteredSubject."""
        infants = {}
        for infant_registered_subject in RegisteredSubject.objects.filter(subject_type='infant', relative_identifier__iexact=self.get_subject_identifier()):
            #look for infant birth record
            if InfantBirth.objects.filter(registered_subject__exact=infant_registered_subject).exists():
                infant_birth = InfantBirth.objects.get(registered_subject__exact=infant_registered_subject)
                dct = infant_birth.__dict__
                dct['dashboard_model'] = convert_from_camel(infant_birth._meta.object_name)
                dct['dashboard_id'] = convert_from_camel(infant_birth.pk)
                dct['dashboard_type'] = 'infant'
                infants[infant_registered_subject.subject_identifier] = dct
            else:
                dct = {'subject_identifier': infant_registered_subject.subject_identifier}
                dct['dashboard_model'] = 'registered_subject'
                dct['dashboard_id'] = infant_registered_subject.pk
                dct['dashboard_type'] = 'infant'
                infants[infant_registered_subject.subject_identifier] = dct
        return infants

    def get_delivery_datetime(self):
        # get delivery date if delivered
        if MaternalLabDel.objects.filter(maternal_visit__appointment__registered_subject__subject_identifier=self.get_subject_identifier()):
            delivery_datetime = MaternalLabDel.objects.get(maternal_visit__appointment__registered_subject__subject_identifier=self.get_subject_identifier()).delivery_datetime
        else:
            delivery_datetime = None
        return delivery_datetime
