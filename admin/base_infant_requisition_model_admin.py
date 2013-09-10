from lab_requisition.admin import BaseRequisitionModelAdmin
from mpepu_infant.models import InfantVisit


class BaseInfantRequisitionModelAdmin (BaseRequisitionModelAdmin):

    visit_model = InfantVisit
    visit_fieldname = 'infant_visit'
    dashboard_type = 'infant'
