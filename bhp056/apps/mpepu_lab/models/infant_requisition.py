from django.db import models
from audit_trail.audit import AuditTrail
from mpepu_infant.models import InfantVisit
from lab_requisition.models import BaseClinicRequisition


class InfantRequisition(BaseClinicRequisition):

    infant_visit = models.ForeignKey(InfantVisit)

    history = AuditTrail()

    def get_visit(self):
        if not self.id:
            return None
        return self.infant_visit

    class Meta:
        app_label = 'mpepu_lab'
        verbose_name = 'Infant Laboratory Requisition'
