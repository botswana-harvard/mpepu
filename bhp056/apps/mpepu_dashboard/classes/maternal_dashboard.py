from collections import OrderedDict

from edc.core.bhp_common.utils import convert_from_camel
from edc.dashboard.subject.classes import RegisteredSubjectDashboard
from edc.subject.registration.models import RegisteredSubject

from apps.mpepu_infant.models import InfantBirth
from apps.mpepu_maternal.models import MaternalConsent, MaternalVisit, MaternalLabDel, MaternalLocator, MaternalEligibilityAnte, MaternalEligibilityPost
from apps.mpepu_lab.models import MaternalRequisition, PackingList
from .dashboard_mixin import DashboardMixin


class MaternalDashboard(DashboardMixin, RegisteredSubjectDashboard):

    view = 'maternal_dashboard'
    dashboard_name = 'Maternal Dashboard'
    dashboard_url_name = 'subject_dashboard_url'
    urlpatterns = [
        RegisteredSubjectDashboard.urlpatterns[0][:-1] + '(?P<appointment_code>{appointment_code})/$'
        ] + RegisteredSubjectDashboard.urlpatterns
    urlpattern_options = dict(
        RegisteredSubjectDashboard.urlpattern_options,
        dashboard_model=RegisteredSubjectDashboard.urlpattern_options['dashboard_model'] + '|maternal_consent|materna_eligibility_post|maternal_eligibility_ante',
        dashboard_type='maternal',
        appointment_code='1000M|2000M|2010M|2020M|2030M|2060M|2090M|2120M|2150M|2180M')

    template_name = 'maternal_dashboard.html'
    
    def __init__(self, *args, **kwargs):
        super(MaternalDashboard, self).__init__(*args, **kwargs)
        self.visit_model = MaternalVisit
        #self._registered_subject = None
        self.dashboard_type_list = ['maternal']
        self.dashboard_models['maternal_consent']  = MaternalConsent
        #self.extra_url_context = ""
        self.membership_form_category= ['maternal_eligible_antenatal', 'maternal_eligible_postnatal', 'maternal_postnatal_reg', 'maternal_resistance']
        #self._locator_model = None
        self._requisition_model = MaternalRequisition
        

    #def add_to_context(self):
    def get_context_data(self, **kwargs):
        self.context = super(MaternalDashboard, self).get_context_data(**kwargs)
        self.context.update(
            home='mpepu',
            infants=self.get_infants(),
            search_name='maternal',
            infant_dashboard_url=self.get_infant_dashboard_url(),
            title='Maternal Dashboard',
            delivery_datetime=self.get_delivery_datetime(),
            maternal_consent=self.consent
            )
        return self.context

    @property
    def consent(self):
        self._consent = None
        try:
            self._consent = MaternalConsent.objects.get(id=self.dashboard_id)
        except MaternalConsent.DoesNotExist:
            if self.appointment:
                self._consent = MaternalConsent.objects.get(registered_subject=self.appointment.registered_subject)
        return self._consent

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
        if self.consent:
            self._subject_identifier = self.consent.subject_identifier
        else:
            pass
        return self._subject_identifier

   
    def subject_type(self):
        return 'infant'
    
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

    @RegisteredSubjectDashboard.locator_model.getter
    def locator_model(self):
        return MaternalLocator

    def get_packing_list_model(self):
        return PackingList

    def get_infants(self):
        """Returns a list of infants identifiers asssociated with the maternal subject_identifier by querying the Birth model or RegisteredSubject."""
        infants = OrderedDict()
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

    def subject_hiv_status(self):
        super(MaternalDashboard, self).subject_hiv_status
        eligible_ante = MaternalEligibilityAnte.objects.filter(registered_subject=self.registered_subject)
        eligible_post = MaternalEligibilityPost.objects.filter(registered_subject=self.registered_subject)
        if eligible_ante:
            if eligible_ante[0].is_hiv_positive == 'Yes':
                self._subject_hiv_status = 'POS'
        elif eligible_post:
            if eligible_post[0].is_hiv_positive == 'Yes':
                self._subject_hiv_status = 'POS'
        elif not self._subject_hiv_status:
            self._subject_hiv_status = 'UNK'
        return self._subject_hiv_status
