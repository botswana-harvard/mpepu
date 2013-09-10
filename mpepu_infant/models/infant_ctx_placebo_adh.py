from django.db import models
from django.core.urlresolvers import reverse
from audit_trail.audit import AuditTrail
from mpepu_infant.choices import REASON_MISSED_CTX_PLACEBO
from mpepu_infant.models import BaseScheduledVisitModel


class InfantCtxPlaceboAdh(BaseScheduledVisitModel):

    """MP011 - Infant Study Drug Record"""

    day_missed_drug = models.IntegerField(
        verbose_name="Since the last attended scheduled visit, how many entire days of scheduled CTX/Placebo were missed",
        max_length=2,
        help_text="Enter '0' if no entire days missed",
        blank=True,
        null=True,
        )
    reason_missed = models.CharField(
        verbose_name="If at least one day of CTX/Placebo was missed, list the primary reason that a day was missed",
        choices=REASON_MISSED_CTX_PLACEBO,
        max_length=50,
        help_text="",
        default='N/A',
        )
    reason_missed_other = models.CharField(
        verbose_name="if other, specify",
        max_length=100,
        help_text="",
        blank=True,
        null=True,
        )
    history = AuditTrail()

    objects = models.Manager()

    def __unicode__(self):
        return "%s" % (self.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantctxplaceboadh_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Ctx Placebo:Adherence"
