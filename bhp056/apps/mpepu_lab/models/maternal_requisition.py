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
        return self.maternal_visit

    def get_subject_identifier(self):
        return self.get_visit().subject_identifier

    class Meta:
        app_label = 'mpepu_lab'
        verbose_name = 'Maternal Laboratory Requisition'
