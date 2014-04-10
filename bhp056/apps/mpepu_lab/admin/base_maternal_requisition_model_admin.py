from edc.lab.lab_requisition.admin import BaseRequisitionModelAdmin
from apps.mpepu_maternal.models import MaternalVisit


class BaseMaternalRequisitionModelAdmin (BaseRequisitionModelAdmin):

    visit_model = MaternalVisit
    visit_fieldname = 'maternal_visit'
    dashboard_type = 'maternal'

    def __init__(self, *args, **kwargs):
        super(BaseMaternalRequisitionModelAdmin, self).__init__(*args, **kwargs)
        # remove these fields from admin fields list, default values should apply
        for fld in ['test_code']:
            self.fields.remove(fld)
