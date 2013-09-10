from django.db import models
from django.core.urlresolvers import reverse
from audit_trail.audit import AuditTrail
from bhp_base_model.fields import OtherCharField
from bhp_common.choices import YES_NO
from mpepu_infant.models import BaseScheduledVisitModel
from infant_fu import InfantFu


class InfantFuNewMed(BaseScheduledVisitModel):

    infant_fu = models.ForeignKey(InfantFu)

    new_medications = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="6.Has the child recieved a NEW course of any of the following medications since the last attended scheduled visit",
        help_text="do not report if the same course was recorded at previous visit. only report oral and intravenous meds",
        )
    other_medications = OtherCharField(
        max_length=35,
        verbose_name="6a.Other medication that is important to report,in the view of the investigator(either because of potential overlapping toxicity with study CTX/placebo or NVP,or for some other reason(specify medication)",
        help_text="",
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % (self.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantfunewmed_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant FollowUp: New Medication"