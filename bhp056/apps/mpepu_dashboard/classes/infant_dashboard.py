from datetime import timedelta, date

from edc.dashboard.subject.classes import RegisteredSubjectDashboard
from edc.lab.lab_clinic_api.classes import EdcLabResults
from edc.subject.registration.models import RegisteredSubject

from apps.mpepu_infant.models import InfantBirth, InfantVisit, InfantEligibility
from apps.mpepu_infant_rando.models import InfantRando
from apps.mpepu_maternal.models import MaternalConsent, MaternalLabDel, MaternalLocator
from apps.mpepu_lab.models import InfantRequisition, PackingList
from .dashboard_mixin import DashboardMixin

from edc.lab.lab_clinic_api.models import Panel


class InfantDashboard(DashboardMixin, RegisteredSubjectDashboard):

    view = 'infant_dashboard'
    dashboard_name = 'Infant Dashboard'
    dashboard_url_name = 'subject_dashboard_url'
    urlpatterns = [
        RegisteredSubjectDashboard.urlpatterns[0][:-1] + '(?P<appointment_code>{appointment_code})/$'
        ] + RegisteredSubjectDashboard.urlpatterns
    urlpattern_options = dict(
        RegisteredSubjectDashboard.urlpattern_options,
        dashboard_model=RegisteredSubjectDashboard.urlpattern_options['dashboard_model'] + '|infant_birth_record',
        dashboard_type='infant',
        appointment_code='2000|2010|2015|2020|2030|2060|2090|2120|2150|2180')

    template_name = 'infant_dashboard.html'

    def __init__(self, *args, **kwargs):
        super(InfantDashboard, self).__init__(*args, **kwargs)
        self._infant_birth = None
        self._maternal_identifier = None
        self.dashboard_type_list = ['infant']
        self.visit_model = InfantVisit
        self.dashboard_models['infant_birth'] = InfantBirth
        self.membership_form_category= ['infant_rando_eligible', 'infant_pre_randomize', 'infant_birth_record']
#         self.extra_url_context = ""
        self._locator_model = None
        self._requisition_model = InfantRequisition
        

#     def add_to_context(self):
    def get_context_data(self, **kwargs):
        self.context = super(InfantDashboard, self).get_context_data(**kwargs)
        panels = Panel.objects.all()
        self.context.update(
            home='mpepu',
            search_name='infant',
            maternal_dashboard_url=self.get_maternal_dashboard_url(),
            title='Infant Dashboard',
            delivery_datetime=self.get_delivery_datetime(),
            stratum=self.get_feeding_stratum(),
            infant_birth = self.infant_birth,
#             infant_birth=self.get_infant_birth(),
            delivery_date=self.get_delivery_date(),
            maternal_consent=self.get_maternal_consent(),
            days_alive=self.get_days_alive(),
            panels=panels,
            local_results=self.render_labs()
        )
        return self.context

    def render_labs(self):
#         super(InfantDashboard, self).render_labs()
        if self._requisition_model:
            edc_lab_results = EdcLabResults()
            return edc_lab_results.results_template(self.subject_identifier, False)
        return ''

    @property
    def subject_type(self):
        return 'infant'

    @property
    def consent(self):
        pass

    @property
    def registered_subject(self):
        if not self._registered_subject:
            try:
                self._registered_subject = RegisteredSubject.objects.get(pk=self.dashboard_id)
            except RegisteredSubject.DoesNotExist:
                try:
                    self._registered_subject = RegisteredSubject.objects.get(subject_identifier=self.subject_identifier)
                except RegisteredSubject.DoesNotExist:
                    try:
                        self._registered_subject = self.appointment.registered_subject
                    except AttributeError:
                        pass
        return self._registered_subject

    @property
    def subject_identifier(self):
        self._subject_identifier = None
        if self.infant_birth:
            self._subject_identifier=self.infant_birth.registered_subject.subject_identifier
        return self._subject_identifier

    def get_registered_subject(self):
        return self.registered_subject

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

    def get_locator_model(self):
        return MaternalLocator

    def get_locator_scheduled_visit_code(self):
        """ Returns visit where the locator is scheduled, TODO: maybe search visit definition for this?."""
        return '1000M'

    @RegisteredSubjectDashboard.locator_model.getter
    def locator_model(self):
        return self.get_locator_model()

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

                        #v4 changed to enable users to know which infants have mothers who were unwilling to be randomized [Opt-out]

                        if rando_bf_duration == 'No':
                            stratum['bf_duration'] = '{0} ({1})'.format(stratum['bf_duration'], 'Opt-out')
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
        consent = MaternalConsent.objects.get(subject_identifier=self.registered_subject.relative_identifier)
        return consent

    def get_maternal_lab_del(self):
        return MaternalLabDel.objects.get(maternal_visit__appointment__registered_subject__subject_identifier=self.get_maternal_identifier())

    @property
    def infant_birth(self):
        if InfantBirth.objects.filter(id=self.dashboard_id):
            self._infant_birth = InfantBirth.objects.get(id=self.dashboard_id)
        elif self.appointment:
            self._infant_birth = InfantBirth.objects.get(registered_subject=self.appointment.registered_subject)
        elif self.registered_subject:
            try:
                self._infant_birth = InfantBirth.objects.get(registered_subject=self.registered_subject)
            except Exception as e:
                self._infant_birth = InfantBirth.objects.none()
        else:
            self._infant_birth = InfantBirth.objects.none()
        return self._infant_birth

    def get_infant_birth(self):
        return self.infant_birth

    def get_delivery_date(self):
        return self.get_maternal_lab_del().delivery_datetime.date()

    def get_days_alive(self):
        days_alive = None
        if self.get_infant_birth():
            if date.today() - self.get_infant_birth().dob <= timedelta(days=60):
                days_alive = (date.today() - self.get_infant_birth().dob + timedelta(days=1)).days
        return days_alive

    def subject_hiv_status(self):
        super(InfantDashboard, self).subject_hiv_status
        eligibility = InfantEligibility.objects.filter(registered_subject=self.registered_subject)
        if eligibility and eligibility[0].hiv_status == 'Yes':
            self._subject_hiv_status = 'POS'
        elif not self._subject_hiv_status:
            self._subject_hiv_status = 'UNK'
        return self._subject_hiv_status

