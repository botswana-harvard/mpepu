from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO, YES_NO_NA

from .base_scheduled_visit_model import BaseScheduledVisitModel


class InfantStoolCollection(BaseScheduledVisitModel):

    """Infant stool collection. Processed in consent version 4.0 and at rando, 3, 6 and 18mnths"""

    sample_obtained = models.CharField(
        verbose_name="A stool sample/specimen can be obtained from the nappy of this child today ",
        choices=YES_NO,
        max_length=3,
        help_text=("If a stool samples/specimen cannot be obtained today, do not complete the"
                   " remainder of this form"),
        )
    axi_temp = models.DecimalField(
        verbose_name="Record the child's axillary temperature",
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=False,
        help_text="degrees celcius",
        )
    past_diarrhea = models.CharField(
        verbose_name="Has this infant/child had diarrhea in the past 7 days?",
        choices=YES_NO,
        max_length=3,
        null=True,
        blank=False,
        help_text=("Diarrhea is defined as 3 or more loose or watery stools with or without blood"
                   " over a 24 hour period and the stool pattern is a change from the"
                   " infant's/child's normal stool pattern"),
        )
    diarrhea_past_24hrs = models.CharField(
        verbose_name=("If the child has had diarrhea in the last 7 days, has the child's"
                      " diarrhea continued in the last 24 hours?"),
        max_length=15,
        choices=YES_NO_NA,
        null=True,
        blank=False,
        help_text="",
        )
    antibiotics_7days = models.CharField(
        verbose_name="Has this infant/child taken antibiotics in the past 7 days, other than CTX/Placebo?",
        choices=YES_NO,
        max_length=3,
        null=True,
        blank=False,
        help_text=("If the answer to this question is yes, please ensure that antibiotic"
                   " information is recorded on NEW MEDICATIONS EDC form"),
        )
    antibiotic_dose_24hrs = models.CharField(
        verbose_name=("If this infant/child has taken antibiotics in the past 7 days, have they"
                      " taken a dose in the last 24 hours, other than CTX/Placebo?"),
        max_length=15,
        choices=YES_NO_NA,
        null=True,
        blank=False,
        help_text="",
        )

    history = AuditTrail()

    objects = models.Manager()

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Stool Collection"
        verbose_name_plural = "Infant Stool Collection"
