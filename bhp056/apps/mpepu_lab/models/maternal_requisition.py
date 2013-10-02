from django.db import models
from edc.audit.audit_trail import AuditTrail
from mpepu_maternal.models import MaternalVisit
from lab_requisition.models import BaseClinicRequisition


class MaternalRequisition(BaseClinicRequisition):

    maternal_visit = models.ForeignKey(MaternalVisit)

    history = AuditTrail()

    def get_visit(self):
        if not self.id:
            return None
        return self.maternal_visit

    class Meta:
        app_label = 'mpepu_lab'
        verbose_name = 'Maternal Laboratory Requisition'
