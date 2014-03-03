from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.lab.lab_requisition.models import BaseClinicRequisition
# from edc.entry_meta_data.managers import RequisitionMetaDataManager

from apps.mpepu_maternal.models import MaternalVisit

from ..managers import RequisitionManager


class MaternalRequisition(BaseClinicRequisition):

    maternal_visit = models.ForeignKey(MaternalVisit)

    entry_meta_data_manager = RequisitionManager(MaternalVisit)

    history = AuditTrail()

    def get_visit(self):
        if not self.id:
            return None
        return self.maternal_visit

    class Meta:
        app_label = 'mpepu_lab'
        verbose_name = 'Maternal Laboratory Requisition'
