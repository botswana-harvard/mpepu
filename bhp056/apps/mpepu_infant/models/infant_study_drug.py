from django.db import models
from django.core.urlresolvers import reverse

from edc.choices import YES_NO
from edc.audit.audit_trail import AuditTrail

from ..choices import CTX_PLACEBO_STATUS
from .base_scheduled_visit_model import BaseScheduledVisitModel


class InfantStudyDrug(BaseScheduledVisitModel):

    on_placebo_status = models.CharField(
        verbose_name="3. Was the baby supposed to be taking CTX/Placebo for any period since the last attended scheduled visit?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )
    drug_status = models.CharField(
        verbose_name="What is the status of the participant's CTX/Placebo at this visit or since the last visit?",
        choices=CTX_PLACEBO_STATUS,
        max_length=90,
        help_text="",
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % (self.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantstudydrug_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Study Drug Record"
