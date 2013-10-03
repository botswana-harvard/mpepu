from edc.lab.lab_requisition.admin import BaseRequisitionModelAdmin
from apps.mpepu_maternal.models import MaternalVisit


class BaseMaternalRequisitionModelAdmin (BaseRequisitionModelAdmin):

    visit_model = MaternalVisit
    visit_fieldname = 'maternal_visit'
    dashboard_type = 'maternal'
