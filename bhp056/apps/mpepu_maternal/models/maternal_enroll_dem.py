from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO
from bhp_base_model.fields import OtherCharField
from mpepu_list.models.maternal_enroll import HhGoods
from apps.mpepu.choices import MARITAL_STATUS, HIGHEST_EDUCATION, CURRENT_OCCUPATION, MONEY_PROVIDER, TOILET_FACILITY
from apps.mpepu.choices import HOUSE_TYPE, ETHNICITY, MONEY_EARNED, WATER_SOURCE, COOKING_METHOD, KNOW_HIV_STATUS
from mpepu_maternal.models import BaseScheduledVisitModel
from maternal_enroll import MaternalEnroll


class MaternalEnrollDem(BaseScheduledVisitModel):

    """Model for Maternal Enrollment: Demographics"""

    maternal_enroll = models.OneToOneField(MaternalEnroll)

    marital_status = models.CharField(
        max_length=25,
        verbose_name="1. Current Marital status ",
        choices=MARITAL_STATUS,
        help_text="",
        )
    marital_status_other = OtherCharField(
        max_length=35,
        verbose_name="1a. if other specify...",
        blank=True,
        null=True,
        )
    ethnicity = models.CharField(
        max_length=25,
        verbose_name="2. Ethnicity ",
        choices=ETHNICITY,
        help_text="",
        )
    ethnicity_other = OtherCharField(
        max_length=35,
        verbose_name="2a. if other specify...",
        blank=True,
        null=True,
        )
    highest_education = models.CharField(
        max_length=25,
        verbose_name="3. Highest educational level completed ",
        choices=HIGHEST_EDUCATION,
        help_text="",
        )
    current_occupation = models.CharField(
        max_length=75,
        verbose_name="4. Current occupation",
        choices=CURRENT_OCCUPATION,
        help_text="",
        )
    current_occupation_other = OtherCharField(
        max_length=35,
        verbose_name="4a. if other specify...",
        blank=True,
        null=True,
        )
    provides_money = models.CharField(
        max_length=50,
        verbose_name="5. Who provides most of your money?",
        choices=MONEY_PROVIDER,
        help_text="",
        )
    provides_money_other = OtherCharField(
        max_length=35,
        verbose_name="5a. if other specify...",
        blank=True,
        null=True,
        )
    money_earned = models.CharField(
        max_length=50,
        verbose_name="6. How much money do you personally earn? ",
        choices=MONEY_EARNED,
        help_text="",
        )
    money_earned_other = OtherCharField(
        max_length=35,
        verbose_name="6a. if other specify...",
        blank=True,
        null=True,
        )
    own_phone = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="7. Do you have your own cell phone that you use regularly? ",
        help_text="",
        )
    water_source = models.CharField(
        max_length=50,
        verbose_name="8. At your primary home  where do you get most of your family's drinking water?",
        choices=WATER_SOURCE,
        help_text="the home where you are likely to spend the most time with your baby over the first 18 months",
        )

    house_electrified = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="9. Is there electricity in this house / compound? ",
        help_text="",
        )

    house_fridge = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="10. Is there a refrigerator being used in this house / compound?  ",
        help_text="",
        )

    cooking_method = models.CharField(
        max_length=50,
        verbose_name="11. What is the primary method of cooking in this house / compound?",
        choices=COOKING_METHOD,
        help_text="",
        )
    hh_goods = models.ManyToManyField(HhGoods,
        verbose_name="12. Do you have any of the following in the household?  ",
        help_text="Tick all that apply",
        )
    toilet_facility = models.CharField(
        max_length=50,
        verbose_name="13. Which of the following types of toilet facilities do you most often use at this house / compound? ",
        choices=TOILET_FACILITY,
        help_text="",
        )
    toilet_facility_other = OtherCharField(
        max_length=35,
        verbose_name="13a. if other specify...",
        blank=True,
        null=True,
        )
    house_people_number = models.IntegerField(
        verbose_name="14. How many people, including yourself, stay in this home / compound most of the time?",
        help_text="",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100),
            ]
        )
    house_type = models.CharField(
        max_length=50,
        verbose_name="15. Housing type?  ",
        choices=HOUSE_TYPE,
        help_text="Indicate the primary type of housing used over the past 30 days",
        )
    know_hiv_status = models.CharField(
        max_length=50,
        verbose_name="16. How many people know that you are HIV infected?",
        choices=KNOW_HIV_STATUS,
        help_text="",
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % (self.maternal_enroll)

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalenrolldem_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Enrollment: Demographics"
