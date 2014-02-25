from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.subject.consent.models.base_consented_uuid_model import BaseConsentedUuidModel
from apps.mpepu.choices import DX_DRUG_RELATIONSHIP, DRUG_RELATIONSHIP

from .infant_base_uuid_model import InfantBaseUuidModel
from .infant_fu_dx2_proph import InfantFuDx2Proph
from .infant_off_study_mixin import InfantOffStudyMixin


# class InfantFuDx2ProphItems(InfantOffStudyMixin, BaseConsentedUuidModel):#me
class InfantFuDx2ProphItems(InfantBaseUuidModel):# found

    infant_fu_dx = models.ForeignKey(InfantFuDx2Proph)

    dx = models.CharField(
        max_length=50,
        choices=DX_DRUG_RELATIONSHIP,
        verbose_name="Diagnosis",
        help_text="",
        blank=True,
        null=True,
        )
    ctx = models.CharField(
        max_length=50,
        choices=DRUG_RELATIONSHIP,
        verbose_name="Relationship to study CTX/placebo ",
        blank=True,
        null=True,
        )
    nvp = models.CharField(
        max_length=50,
        choices=DRUG_RELATIONSHIP,
        verbose_name="Relationship to infant NVP prophylaxis",
        help_text="",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def get_visit(self):
        return self.infant_fu_dx.infant_visit

    def __unicode__(self):
        return unicode(self.infant_fu_dx.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantfudx2prophitems_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant FollowUp: Dx to Proph Items"
        verbose_name_plural = "Infant FollowUp: Dx to Proph Items"
