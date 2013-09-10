from datetime import timedelta, date
from bhp_dashboard_registered_subject.classes import RegisteredSubjectDashboard
#from bhp_subject_summary.models import Link
from mpepu_infant.models import InfantBirth, InfantVisit, InfantEligibility
from mpepu_infant_rando.models import InfantRando
from mpepu_maternal.models import MaternalConsent, MaternalLabDel
from mpepu_lab.models import InfantRequisition


class InfantDashboard(RegisteredSubjectDashboard):

    def __init__(self, **kwargs):

        self.dashboard_type = 'infant'
        super(InfantDashboard, self).__init__(**kwargs)
        self.visit_model = InfantVisit
        self.visit_model_app_label = InfantVisit._meta.app_label
        self.visit_model_name = InfantVisit._meta.module_name
        self.requisition_model = InfantRequisition
        self.subject_type = 'infant'
        self.context.add(
            visit_model_name=self.visit_model_name,
            requisition_model=InfantRequisition,
            visit_model=self.visit_model,
            visit_model_app_label=self.visit_model_app_label,
            subject_type=self.subject_type,
            home=kwargs.get('home', 'mpepu'),
            search_name=kwargs.get('search_name', 'infant'),
            )

    def create(self, **kwargs):

        self.dashboard_identifier = kwargs.get("registered_subject").subject_identifier
        # call super to initialize default context
        super(InfantDashboard, self).create(**kwargs)
        self.context.add(
            home='mpepu',
            search_name='infantbirth')
        stratum = {'feeding_choice': '-', 'bf_duration': '-'}
        if self.registered_subject:
            if InfantRando.objects.filter(subject_identifier=self.get_subject_identifier()):
                infant_rando = InfantRando.objects.get(subject_identifier=self.get_subject_identifier())
                stratum['randomization_datetime'] = infant_rando.randomization_datetime
                stratum['feeding_choice'] = infant_rando.feeding_choice
                if infant_rando.bf_duration:
                    #stratum['bf_duration'] = '{0} ({1})'.format(stratum['bf_duration'], infant_rando.bf_duration)
                    stratum['bf_duration'] = infant_rando.bf_duration
                    # TODO: v2 get rando_bf_duration from eligibility checklist and show along with BF duration
                    if InfantEligibility.objects.filter(registered_subject__subject_identifier=self.get_subject_identifier()).exists():
                        rando_bf_duration = InfantEligibility.objects.get(registered_subject__subject_identifier=self.get_subject_identifier()).rando_bf_duration
                        if rando_bf_duration == 'No':
                            stratum['bf_duration'] = '{0} ({1})'.format(stratum['bf_duration'], rando_bf_duration)
            else:
                stratum = {'feeding_choice': 'pending', 'bf_duration': '-'}
        self.context.add(stratum=stratum)
        maternal_consent = MaternalConsent.objects.get(subject_identifier=self.registered_subject.relative_identifier)
        self.context.add(maternal_consent=maternal_consent)
        maternal_labdel = MaternalLabDel.objects.get(maternal_visit__appointment__registered_subject__subject_identifier=self.registered_subject.relative_identifier)
        delivery_date = maternal_labdel.delivery_datetime.date()
        if InfantBirth.objects.filter(registered_subject__subject_identifier__exact=self.get_subject_identifier()):
            infant_birth = InfantBirth.objects.get(registered_subject__subject_identifier__exact=self.get_subject_identifier())
        else:
            infant_birth = InfantBirth.objects.none()
        # weight
        #if InfantFuPhysical.objects.filter(infant_visit__appointment__registered_subject__subject_identifier=self.subject_identifier).count() > 1:
        #    weights = InfantFuPhysical.objects.filter(infant_visit__appointment__registered_subject__subject_identifier=self.subject_identifier)
        # lab plots
        #show_lab_plots = []
        #if Lab.objects.filter(subject_identifier=self.subject_identifier, result__resultitem__test_code__code='CD4').count() > 1:
        #    show_lab_plots.append({'title': 'CD4', 'url_arg': 'CD4'})
        #if Lab.objects.filter(subject_identifier=self.subject_identifier, result__resultitem__test_code__code__in=['AUVL', 'PHM', 'PHS', ]).count() > 1:
        #    show_lab_plots.append({'title': 'Viral Load', 'url_arg': 'VL'})
        days_alive = None
        if infant_birth:
            if date.today() - infant_birth.dob <= timedelta(days=60):
                days_alive = (date.today() - infant_birth.dob + timedelta(days=1)).days
        self.context.add(
            infant_birth=infant_birth,
            delivery_date=delivery_date,
            local_results=self.render_labs(),
            #show_lab_plots=show_lab_plots,
            days_alive=days_alive)
