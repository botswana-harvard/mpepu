from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO
from edc.subject.haart.choices import ARV_STATUS_WITH_NEVER

from .base_scheduled_visit_model import BaseScheduledVisitModel


class InfantArvProph(BaseScheduledVisitModel):

    prophylatic_nvp = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Was the baby supposed to be taking taking prophylactic NVP for any period since the last attended scheduled visit?",
        )

    arv_status = models.CharField(
        max_length=25,
        verbose_name="What is the status of the participant's ARV prophylaxis at this visit or since the last visit? ",
        choices=ARV_STATUS_WITH_NEVER,
        help_text="referring to prophylaxis other than single dose NVP",
        default='N/A',
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % (self.infant_visit)

    def report_datetime(self):
        return datetime.today()

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantarvproph_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = 'Infant NVP or AZT Proph'
