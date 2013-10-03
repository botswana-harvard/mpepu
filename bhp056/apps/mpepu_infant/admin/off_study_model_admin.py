from edc.subject.off_study.admin import BaseOffStudyModelAdmin


class OffStudyModelAdmin (BaseOffStudyModelAdmin):

    dashboard_type = 'infant'
    visit_model_name = 'infantvisit'
