from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO
from edc.base.model.validators import eligible_if_yes, eligible_if_no

from apps.mpepu_maternal.models import BaseScheduledVisitModel


class ResistanceEligibility(BaseScheduledVisitModel):

    co_enrolled = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Is participant co-enrolled in the Mpepu study?",
        help_text='if no, INELIGIBLE',
        validators=[eligible_if_yes]
        )
    status_evidence = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Evidence of confirmed HIV positive status",
        help_text=("By indicating YES, you confirm that you have copied such evidence for the"
                   " patient chart"),
        validators=[eligible_if_yes]
        )
    lates_cd4 = models.IntegerField(
        max_length=4,
        verbose_name="What is the mother's nadir (lowest recorded) CD4 count?",
        validators=[MinValueValidator(0), MaxValueValidator(3000)],
        )
    who_illness = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Has the mother ever experienced a WHO stage 3 or 4 illness?",
        validators=[eligible_if_no],
        help_text='if yes, INELIGIBLE',
        )
    stopped_arv = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name=("Has the Mother Stopped (or definitely planning to stop) EFV/TDF/FTC or"
                      " EFV/TDF/3TC postpartum?"),
        )
    incarcerated = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Is participant currently involuntarily incarcerated?",
        validators=[eligible_if_no]
        )

    history = AuditTrail()

    class Meta:
        app_label = 'mpepu_maternal'
        verbose_name = 'ARV Resistance Eligibility'
        verbose_name_plural = 'ARV Resistance Eligibility'
