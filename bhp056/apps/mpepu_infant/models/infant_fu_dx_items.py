from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO
from edc.core.bhp_diagnosis.models import BaseBaseDiagnosisItem

from ..choices import DX_INFANT
from .infant_fu_dx import InfantFuDx
from .infant_off_study_mixin import InfantOffStudyMixin


class InfantFuDxItems(InfantOffStudyMixin, BaseBaseDiagnosisItem):

    infant_fu_dx = models.ForeignKey(InfantFuDx)

    fu_dx = models.CharField(
        max_length=150,
        choices=DX_INFANT,
        verbose_name="Diagnosis",
        # null = True,
        help_text="",
        )
    fu_dx_specify = models.CharField(
        max_length=50,
        verbose_name="Diagnosis specification",
        help_text="",
        blank=True,
        null=True,
        )

    health_facility = models.CharField(
        choices=YES_NO,
        max_length=3,
        verbose_name="Seen at health facility for Dx",
        help_text="",
        # null = True,
        )
    was_hospitalized = models.CharField(
        choices=YES_NO,
        max_length=3,
        verbose_name="Hospitalized?",
        help_text="",
        # null = True,
        )

    history = AuditTrail()

    def get_report_datetime(self):
        return self.infant_fu_dx.get_report_datetime()

    def get_subject_identifier(self):
        return self.infant_fu_dx.get_subject_identifier()

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.get_visit().appointment.registered_subject.relative_identifier

    def get_visit(self):
        return self.infant_fu_dx.infant_visit

    def __unicode__(self):
        return unicode(self.infant_fu_dx.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantfudxitems_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant FollowUp: Dx Items"
        verbose_name_plural = "Infant FollowUp: Dx Items"
