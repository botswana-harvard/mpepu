from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO
from edc.base.model.fields.custom.custom_fields import OtherCharField

from apps.mpepu.choices import HIV_INSIDE_DISCLOSURE, HIV_OUTSIDE_DISCLOSURE, TIME_AFTER_DELIVERY, AGREEING_TERMS
from apps.mpepu_list.models import MaternalFeedingInfluence

from .base_scheduled_visit_model import BaseScheduledVisitModel


class FeedingChoiceSectionTwo(BaseScheduledVisitModel):

    status_disclosure = models.CharField(
        verbose_name="1. I have disclosed my HIV status to: ",
        max_length=45,
        choices=HIV_INSIDE_DISCLOSURE,
        help_text="",
        )
    disclose_hiv_father = models.CharField(
        verbose_name="2. I have disclosed my HIV status to the father of this baby: ",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )
    outside_disclosure = models.CharField(
        verbose_name="3. I have disclosed my HIV status to: ",
        max_length=45,
        choices=HIV_OUTSIDE_DISCLOSURE,
        help_text="",
        )
    influential_people = models.ManyToManyField(MaternalFeedingInfluence,
        verbose_name=("4.The individual(s) most influential in assisting me in making an "
                      "appropriate feeding choice for this baby is/are (select 3): "),
        help_text="Rank up to the three most influential persons",
        )
    influential_people_other = OtherCharField()

    work_influence = models.CharField(
        verbose_name="5.My feeding choice will be influenced by my need to return to work: ",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )
    work_return = models.CharField(
        verbose_name="6.If 'Yes' to Q5 above, I plan to return to work: ",
        max_length=35,
        choices=TIME_AFTER_DELIVERY,
        )

    #7.Please let us know if you agree with any of the following statements: """

    bf_hiv_worry = models.CharField(
        verbose_name=("7a.I am worried that my baby will become HIV infected if he/she "
                      " breastfeeds: "),
        max_length=35,
        choices=AGREEING_TERMS,
        )
    infant_hiv_risk = models.CharField(
        verbose_name=("7b.I am worried that my infant is at risk for dying in the first two "
                      " years of their life:  "),
        max_length=35,
        choices=AGREEING_TERMS,
        )
    hiv_worry = models.CharField(
        verbose_name="7c.I worry more about my baby getting HIV than about my baby dying: ",
        max_length=35,
        choices=AGREEING_TERMS,
        )
    death_worry = models.CharField(
        verbose_name="7d. I worry more about my baby dying than about my baby getting HIV:",
        max_length=35,
        choices=AGREEING_TERMS,
        )
    bf_hiv_arv = models.CharField(
        verbose_name=("7e. I feel I can breastfeed and still keep my baby from getting HIV by"
                      " using antiretroviral medicines: "),
        max_length=35,
        choices=AGREEING_TERMS,
        )
    safe_ff = models.CharField(
        verbose_name="7f. I feel I can safely prepare formula for my baby: ",
        max_length=35,
        choices=AGREEING_TERMS,
        )
    bf_ff_benefits = models.CharField(
        verbose_name=("7g.I understand the risks and benefits of breastfeeding and formula "
                      "feeding for my baby:"),
        max_length=35,
        choices=AGREEING_TERMS,
        )
    baby_bf_choice = models.CharField(
        verbose_name="7h.I am the person who can make the best feeding choice for my baby: ",
        max_length=35,
        choices=AGREEING_TERMS,
        )
    doc_feeding_advice = models.CharField(
        verbose_name="7i. A nurse or a doctor should tell me the best way to feed my baby:  ",
        max_length=35,
        choices=AGREEING_TERMS,
        )

    history = AuditTrail()

    class Meta:
        app_label = 'mpepu_maternal'
        verbose_name = "Feeding Choice: Section 2"
        verbose_name_plural = "Feeding Choice: Section 2"

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_feedingchoicesectiontwo_change', args=(self.id,))
