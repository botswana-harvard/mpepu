from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.lab.lab_requisition.models import BaseClinicRequisition

from apps.mpepu_infant.models import InfantVisit

from .aliquot_type import AliquotType
from .packing_list import PackingList
from .panel import Panel

from ..managers import RequisitionManager


class InfantRequisition(BaseClinicRequisition):

    infant_visit = models.ForeignKey(InfantVisit)

    entry_meta_data_manager = RequisitionManager(InfantVisit)

    packing_list = models.ForeignKey(PackingList, null=True, blank=True)

    aliquot_type = models.ForeignKey(AliquotType)

    panel = models.ForeignKey(Panel)

    history = AuditTrail()

    def get_visit(self):
        if not self.id:
            return None
        return self.infant_visit

    class Meta:
        app_label = 'mpepu_lab'
        verbose_name = 'Infant Laboratory Requisition'
        unique_together = ('infant_visit', 'panel', 'is_drawn')
