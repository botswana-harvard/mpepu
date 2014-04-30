from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO

from .base_scheduled_visit_model import BaseScheduledVisitModel


class FeedingChoice(BaseScheduledVisitModel):

    first_time_feeding = models.CharField(
        verbose_name=("This pregnancy represents the first time I have had to make an infant"
                      " feeding choice: "),
        max_length=3,
        choices=YES_NO,
        help_text="If 'YES' skip to SECTION II",
        )

    history = AuditTrail()

    class Meta:
        app_label = 'mpepu_maternal'
        verbose_name = "Feeding Choice"

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_feedingchoice_change', args=(self.id,))
