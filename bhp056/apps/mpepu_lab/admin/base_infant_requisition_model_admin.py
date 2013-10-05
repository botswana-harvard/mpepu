from edc.lab.lab_requisition.admin import BaseRequisitionModelAdmin
from apps.mpepu_infant.models import InfantVisit


class BaseInfantRequisitionModelAdmin (BaseRequisitionModelAdmin):

    visit_model = InfantVisit
    visit_fieldname = 'infant_visit'
    dashboard_type = 'infant'
