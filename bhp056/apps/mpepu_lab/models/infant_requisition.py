from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.lab.lab_requisition.models import BaseClinicRequisition
# from edc.entry_meta_data.managers import RequisitionMetaDataManager

from apps.mpepu_infant.models import InfantVisit

from ..managers import RequisitionManager


class InfantRequisition(BaseClinicRequisition):

    infant_visit = models.ForeignKey(InfantVisit)
    
    entry_meta_data_manager = RequisitionManager(InfantVisit)

    history = AuditTrail()

    def get_visit(self):
        if not self.id:
            return None
        return self.infant_visit

    class Meta:
        app_label = 'mpepu_lab'
        verbose_name = 'Infant Laboratory Requisition'
