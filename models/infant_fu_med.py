from django.db import models
from django.core.urlresolvers import reverse
from audit_trail.audit import AuditTrail
from bhp_common.choices import YES_NO
from mpepu_infant.models import BaseScheduledVisitModel
from mpepu_list.models import InfantVaccines
from infant_fu import InfantFu


class InfantFuMed(BaseScheduledVisitModel):

    infant_fu = models.ForeignKey(InfantFu)

    vaccines_received = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="7.Since the last attended scheduled visit,did the child recieve any of the following vaccinations",
        help_text="",
        )

    vaccination = models.ManyToManyField(InfantVaccines,
        verbose_name="7a. Vaccines received",
        help_text="Select all the vaccines that were received",
        )

    comments = models.TextField(
        max_length=500,
        verbose_name="8.Comment",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % (self.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantfumed_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant FollowUp: Medication"
