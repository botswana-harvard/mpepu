from django.db import models
from django.core.urlresolvers import reverse
from audit_trail.audit import AuditTrail
from bhp_common.choices import YES_NO
from mpepu_infant.models import BaseScheduledVisitModel


class InfantFu(BaseScheduledVisitModel):

    physical_assessment = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="1. Was physical assessment done today?",
        help_text="",
        )

    diarrhea_illness = models.CharField(
        verbose_name="2. Since the last scheduled visit, has the infant had any diarrheal illness (at least 3 loose stools per day which is ALSO a change from the normal)",
        max_length=3,
        choices=YES_NO,
        help_text="must be of grade 3 or 4",
        )

    has_dx = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="3. Since the last attended scheduled visit, has the infant had any diagnosis that were NEW events",
        help_text="\'NEW events\' are those that were never previously reported OR a NEW episode of a previously resolved diagnosis",
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % (self.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantfu_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant FollowUp"
