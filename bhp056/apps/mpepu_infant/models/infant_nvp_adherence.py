from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail

from ..choices import REASON_MISSED_PROPHYLAXIS
from .infant_arv_proph import InfantArvProph
from .base_scheduled_visit_model import BaseScheduledVisitModel


class InfantNvpAdherence(BaseScheduledVisitModel):

    """
    if mother BF on haart less than 6 weeks and ...
    what about weaning????
    """
    infant_arv_proph = models.ForeignKey(InfantArvProph)

    days_missed = models.IntegerField(
        max_length=2,
        verbose_name="Since the last attended scheduled visit, how many entire days of scheduled prophylactic NVP were missed ",
        help_text="Enter '0' if no entire days missed",
        )
    reason_missed = models.CharField(
        verbose_name="If at least one day of prophylactic NVP was missed,list the primary reason that a day was missed:",
        max_length=25,
        choices=REASON_MISSED_PROPHYLAXIS,
        blank=True,
        null=True,
        help_text="If 'Other', specify below",
        )
    reason_missed_other = models.TextField(
        max_length=200,
        verbose_name="Other, specify",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % (self.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantnvpadherence_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = 'Infant NVP Adherence'
