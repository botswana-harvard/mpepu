from django.db import models
from django.core.urlresolvers import reverse
from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO, POS_NEG_ONLY
from apps.mpepu.choices import SIX_MONTHS_FEEDING
from base_scheduled_visit_model import BaseScheduledVisitModel


class FeedingChoiceSectionOne (BaseScheduledVisitModel):

    last_baby_feeding = models.CharField(
        verbose_name=("2. For the last infant, I practiced the following feeding method from "
                      "birth through the first six months of life: "),
        max_length=35,
        choices=SIX_MONTHS_FEEDING,
        help_text="If answer =2, go to Q2a .Otherwise skip to Q3")
    baby_weaned_age = models.IntegerField(
        verbose_name=("2a. How many months old was your last baby when you weaned him/her from"
                      " breast milk? (Completely stopped providing breast milk): "),
        max_length=2,
        null=True,
        blank=True,
        help_text="")
    hiv_aware_feeding = models.CharField(
        verbose_name=("3. I was aware of my HIV status when I made the feeding decision for "
                      "the infant described in Q2 above:: "),
        max_length=3,
        choices=YES_NO,
        help_text="If 'Yes' go to Q4, otherwise skip Q4")
    hiv_status = models.CharField(
        verbose_name=("4. My HIV status was:"),
        max_length=8,
        choices=POS_NEG_ONLY,
        null=True,
        blank=True,
        help_text="")

    history = AuditTrail()

    class Meta:
        app_label = 'mpepu_maternal'
        verbose_name = "Feeding Choice: Section 1"
        verbose_name_plural = "Feeding Choice: Section 1"

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_feedingchoicesectionone_change', args=(self.id,))
