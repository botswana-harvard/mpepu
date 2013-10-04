from edc.dashboard.subject.classes import RegisteredSubjectDashboard
from edc.subject.registration.models import RegisteredSubject
from apps.mpepu_infant.models import InfantBirth
from apps.mpepu_maternal.models import MaternalConsent, MaternalVisit, MaternalLabDel, MaternalLocator
from apps.mpepu_lab.models import MaternalRequisition, PackingList


class MaternalDashboard(RegisteredSubjectDashboard):

    view = 'maternal_dashboard'
    dashboard_name = 'Maternal Dashboard'

    def __init__(self, *args, **kwargs):
        kwargs.update({'dashboard_models': {'maternal_consent': MaternalConsent}})
        super(MaternalDashboard, self).__init__(*args, **kwargs)

    def add_to_context(self):
        super(MaternalDashboard, self).add_to_context()
        self.context.add(
            home='mpepu',
            search_name='maternal',
            subject_dashboard_url='maternal_dashboard_url',
            infant_dashboard_url=self.get_infant_dashboard_url(),
            title='Maternal Dashboard',
            subject_consent=self.get_consent(),
            delivery_datetime=self.get_delivery_datetime(),
            infants=self.get_infants(),
            )

    def get_infant_dashboard_url(self):
        return 'subject_dashboard_url'

    def set_dashboard_type_list(self):
        self._dashboard_type_list = ['subject']

    def set_consent(self):
        """Sets to the subject consent, if it has been completed."""
        self._consent = None
        if MaternalConsent.objects.filter(subject_identifier=self.get_subject_identifier()):
            self._consent = MaternalConsent.objects.get(subject_identifier=self.get_subject_identifier())

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
        # list infant on the side bar. If InfantBirth information is available, use that
        infants = {}
        for infant_registered_subject in RegisteredSubject.objects.filter(subject_type='INFANT', relative_identifier__iexact=self.get_subject_identifier()):
            #look for infant birth record
            if InfantBirth.objects.filter(registered_subject__exact=infant_registered_subject):
                infants[infant_registered_subject.subject_identifier] = InfantBirth.objects.get(registered_subject__exact=infant_registered_subject).__dict__
            else:
                infants[infant_registered_subject.subject_identifier] = {'subject_identifier': infant_registered_subject.subject_identifier}
        return infants

    def get_delivery_datetime(self):
        # get delivery date if delivered
        if MaternalLabDel.objects.filter(maternal_visit__appointment__registered_subject__subject_identifier=self.get_subject_identifier()):
            delivery_datetime = MaternalLabDel.objects.get(maternal_visit__appointment__registered_subject__subject_identifier=self.get_subject_identifier()).delivery_datetime
        else:
            delivery_datetime = None
        return delivery_datetime
