from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail

from apps.mpepu.choices import MP010_MEDICATIONS, DRUG_ROUTE

from .infant_fu_new_med import InfantFuNewMed
from .infant_base_uuid_model import InfantBaseUuidModel


class InfantFuNewMedItems(InfantBaseUuidModel):

    infant_fu_med = models.ForeignKey(InfantFuNewMed)

    medication = models.CharField(
        max_length=100,
        choices=MP010_MEDICATIONS,
        verbose_name="Medication",
        blank=True,
        null=True,
        )
    drug_route = models.CharField(
        max_length=20,
        choices=DRUG_ROUTE,
        verbose_name="Drug route",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def get_visit(self):
        return self.infant_fu_med.infant_visit

    def __unicode__(self):
        return unicode(self.infant_fu_med.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantfunewmeditems_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant FollowUp: New Med Items"
        verbose_name_plural = "Infant FollowUp: New Med Items"
