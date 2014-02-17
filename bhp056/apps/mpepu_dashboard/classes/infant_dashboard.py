from datetime import timedelta, date

from edc.dashboard.subject.classes import RegisteredSubjectDashboard
from edc.subject.registration.models import RegisteredSubject

from apps.mpepu_infant.models import InfantBirth, InfantVisit, InfantEligibility
from apps.mpepu_infant_rando.models import InfantRando
from apps.mpepu_maternal.models import MaternalConsent, MaternalLabDel, MaternalLocator
from apps.mpepu_lab.models import InfantRequisition, PackingList

from edc.lab.lab_clinic_api.models import Panel


class InfantDashboard(RegisteredSubjectDashboard):

    view = 'infant_dashboard'
    dashboard_name = 'Infant Dashboard'
    dashboard_url_name = 'subject_dashboard_url'

    def __init__(self, *args, **kwargs):
        self._infant_birth = None
        self._maternal_identifier = None
        self._dashboard_type_list = self.set_dashboard_type_list()
        self._visit_model = InfantVisit
        kwargs.update({'dashboard_models': {'infant_birth': InfantBirth}, 'membership_form_category': 'infant'})
        self.extra_url_context = ""
        self._locator_model = None
        self._requisition_model = None
        super(InfantDashboard, self).__init__(*args, **kwargs)

    def add_to_context(self):
        super(InfantDashboard, self).add_to_context()
        panels = Panel.objects.all()
        self.context.add(
            home='mpepu',
            search_name='infant',
            maternal_dashboard_url=self.get_maternal_dashboard_url(),
            title='Infant Dashboard',
            delivery_datetime=self.get_delivery_datetime(),
            stratum=self.get_feeding_stratum(),
            infant_birth=self.get_infant_birth(),
            delivery_date=self.get_delivery_date(),
            maternal_consent=self.get_maternal_consent(),
            days_alive=self.get_days_alive(),
            panels=panels
            )

    def set_registered_subject(self, pk=None):
        self._registered_subject = self.registered_subject
        if RegisteredSubject.objects.filter(subject_identifier=self.subject_identifier):
            self._registered_subject = RegisteredSubject.objects.get(subject_identifier=self.subject_identifier)

    def get_registered_subject(self):
        if not self._registered_subject:
            self.set_registered_subject()
        return self._registered_subject

    def set_membership_form_category(self):
        self._membership_form_category = 'infant'

    def get_maternal_dashboard_url(self):
        return 'subject_dashboard_url'

    def set_dashboard_type_list(self):
        self._dashboard_type_list = ['infant']

    def set_consent(self):
        """Sets to the subject consent, if it has been completed."""
        self._consent = self.get_maternal_consent()

    def get_delivery_datetime(self):
        # get delivery date if delivered
        return self.get_maternal_lab_del().delivery_datetime

    def get_visit_model(self):
        return InfantVisit

    def get_requisition_model(self):
        return InfantRequisition

    def get_locator_model(self):
        return MaternalLocator

    def get_locator_scheduled_visit_code(self):
        """ Returns visit where the locator is scheduled, TODO: maybe search visit definition for this?."""
        return '1000M'

    def get_packing_list_model(self):
        return PackingList

    def get_subject_identifier(self):
        return self.subject_identifier

    def get_feeding_stratum(self):
        stratum = {'feeding_choice': '-', 'bf_duration': '-'}
        if self.get_registered_subject():
            if InfantRando.objects.filter(subject_identifier=self.get_subject_identifier()):
                infant_rando = InfantRando.objects.get(subject_identifier=self.get_subject_identifier())
                stratum['randomization_datetime'] = infant_rando.randomization_datetime
                stratum['feeding_choice'] = infant_rando.feeding_choice
                if infant_rando.bf_duration:
                    stratum['bf_duration'] = infant_rando.bf_duration
                    # TODO: v2 get rando_bf_duration from eligibility checklist and show along with BF duration
                    if InfantEligibility.objects.filter(registered_subject__subject_identifier=self.get_subject_identifier()).exists():
                        rando_bf_duration = InfantEligibility.objects.get(registered_subject__subject_identifier=self.get_subject_identifier()).rando_bf_duration
                        #v4 changed to enable users to know which infants have mothers who were unwilling to be randomized NWR.
                        if rando_bf_duration == 'No':
                            stratum['bf_duration'] = '{0} ({1})'.format(stratum['bf_duration'], 'NWR')
            else:
                stratum = {'feeding_choice': 'pending', 'bf_duration': '-'}
        return stratum

    def set_maternal_identifier(self):
        self._maternal_identifier = self.get_registered_subject().relative_identifier

    def get_maternal_identifier(self):
        if not self._maternal_identifier:
            self.set_maternal_identifier()
        return self._maternal_identifier

    def get_maternal_locator(self):
        return MaternalLocator.objects.get(registered_subject__subject_identifier=self.get_maternal_identifier())

    def get_maternal_consent(self):
        return MaternalConsent.objects.get(subject_identifier=self.get_maternal_identifier())

    def get_maternal_lab_del(self):
        return MaternalLabDel.objects.get(maternal_visit__appointment__registered_subject__subject_identifier=self.get_maternal_identifier())

    def set_infant_birth(self):
        if InfantBirth.objects.filter(registered_subject__subject_identifier__exact=self.get_subject_identifier()):
            self._infant_birth = InfantBirth.objects.get(registered_subject__subject_identifier__exact=self.get_subject_identifier())
        else:
            self._infant_birth = InfantBirth.objects.none()

    def get_infant_birth(self):
        if not self._infant_birth:
            self.set_infant_birth()
        return self._infant_birth

    def get_delivery_date(self):
        return self.get_maternal_lab_del().delivery_datetime.date()

    def get_days_alive(self):
        days_alive = None
        if self.get_infant_birth():
            if date.today() - self.get_infant_birth().dob <= timedelta(days=60):
                days_alive = (date.today() - self.get_infant_birth().dob + timedelta(days=1)).days
        return days_alive
