from bhp_dashboard_registered_subject.classes import RegisteredSubjectDashboard
from edc.subject.registration.models import RegisteredSubject
from mpepu_infant.models import InfantBirth
from mpepu_maternal.models import MaternalConsent, MaternalVisit, MaternalLabDel  # MaternalLocator
from mpepu_lab.models import MaternalRequisition


class MaternalDashboard(RegisteredSubjectDashboard):

    def __init__(self, **kwargs):

        self.dashboard_type = 'maternal'

        super(MaternalDashboard, self).__init__(**kwargs)

        self.visit_model = MaternalVisit
        self.visit_model_app_label = MaternalVisit._meta.app_label
        self.visit_model_name = MaternalVisit._meta.module_name
        self.requisition_model = MaternalRequisition
        self.subject_type = 'maternal'

        self.context.add(
            visit_model_name=self.visit_model_name,
            requisition_model=MaternalRequisition,
            visit_model=self.visit_model,
            visit_model_app_label=self.visit_model_app_label,
            subject_type=self.subject_type,
            home=kwargs.get('home', 'mpepu'),
            search_name=kwargs.get('search_name', 'maternal'),
            )

    def create(self, **kwargs):

        self.dashboard_identifier = kwargs.get("registered_subject").subject_identifier

        # call super to initialize default context 
        super(MaternalDashboard, self).create(**kwargs)

        maternal_consent = MaternalConsent.objects.get(subject_identifier=self.get_subject_identifier())

        # list infant on the side bar. If InfantBirth information is available, use that
        infants = {}

        for infant_registered_subject in RegisteredSubject.objects.filter(subject_type='INFANT', relative_identifier__iexact=self.get_subject_identifier()):
            #look for infant birth record
            if InfantBirth.objects.filter(registered_subject__exact=infant_registered_subject):
                infants[infant_registered_subject.subject_identifier] = InfantBirth.objects.get(registered_subject__exact=infant_registered_subject).__dict__
            else:
                infants[infant_registered_subject.subject_identifier] = {'subject_identifier': infant_registered_subject.subject_identifier}
        # any plots to show?
        show_lab_plots = []
        # get delivery date if delivered
        if MaternalLabDel.objects.filter(maternal_visit__appointment__registered_subject__subject_identifier=self.get_subject_identifier()):
            delivery_datetime = MaternalLabDel.objects.get(maternal_visit__appointment__registered_subject__subject_identifier=self.get_subject_identifier()).delivery_datetime
        else:
            delivery_datetime = None
        self.context.add(
            # home = 'mpepu',
            # search_name = 'maternalconsent',
            maternal_consent=maternal_consent,
            infants=infants,
            local_results=self.render_labs(),
            #locator=self.render_locator(MaternalLocator),
            show_lab_plots=show_lab_plots,
            delivery_datetime=delivery_datetime,
            )
