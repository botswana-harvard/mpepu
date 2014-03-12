from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO

from apps.mpepu.choices import AGREEING_TERMS, DECIDED_FEEDING_CHOICE
from apps.mpepu_list.models import MaternalBfFfRisksBenefits, MaternalUndecidedFeeding

from .base_scheduled_visit_model import BaseScheduledVisitModel


class FeedingChoiceSectionThree (BaseScheduledVisitModel):

    risk_benefit_training = models.ManyToManyField(MaternalBfFfRisksBenefits,
        verbose_name=("I received training about the risks and benefits of breast and "
                      "formula feeding: "),
        )
    und_risk_benefit = models.CharField(
        verbose_name=("The training increased my understanding of the risk and benefits"
                      " of breastfeeding and formula feeding:  "),
        max_length=35,
        choices=AGREEING_TERMS,
        )
    ff_advice = models.CharField(
        verbose_name="I was advised by a health worker to formula feed my baby: ",
        max_length=35,
        choices=AGREEING_TERMS,
        )
    bf_advice = models.CharField(
        verbose_name="I was advised by a health worker to breastfeed my baby: ",
        max_length=35,
        choices=AGREEING_TERMS,
        )
    feeding_choice_made = models.CharField(
        verbose_name="I have already made a feeding choice for my infant: ",
        max_length=3,
        choices=YES_NO,
        help_text="If Yes go to Q7, and if No go to Q8",
        )
    chosen_feeding_choice = models.CharField(
        verbose_name="I made this feeding choice: ",
        max_length=50,
        choices=DECIDED_FEEDING_CHOICE,
        help_text="",
        )
    undecided_feeding = models.ManyToManyField(MaternalUndecidedFeeding,
        verbose_name="I have not yet decided how to feed my baby because: ",
        help_text="Check all that apply ",
        )

    history = AuditTrail()

    class Meta:
        app_label = 'mpepu_maternal'
        verbose_name = "Feeding Choice: Section 3"
        verbose_name_plural = "Feeding Choice: Section 3"

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_feedingchoicesectionthree_change', args=(self.id,))
