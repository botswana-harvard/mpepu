from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO

from apps.mpepu.choices import NEXT_FEEDING_CHOICE, FEEDING_DURATION, CORRECT_BF_DURATION

from ..choices import YES_NO_FF
from .base_scheduled_visit_model import BaseScheduledVisitModel


class PostNatalInfantFeedingSurvey(BaseScheduledVisitModel):

    feeding_satisfaction = models.CharField(
        verbose_name=("1.Were you satisfied with the infant feeding choice, breast feeding or"
                      " formula feeding, that you initially selected for your infant : "),
        max_length=3,
        choices=YES_NO,
        )
    next_feeding_choice = models.CharField(
        verbose_name=("2.How do you think you will feed your next infant from birth through "
                      " the first six months of life :  "),
        max_length=30,
        choices=NEXT_FEEDING_CHOICE,
        )
    feeding_period = models.CharField(
        verbose_name="3.Do you think your infant breastfed for the right number of months:",
        max_length=3,
        choices=YES_NO_FF,
        )
    feeding_duration = models.CharField(
        verbose_name="3a.If No to Q3 above, the duration of breastfeeding of my infant was:",
        max_length=3,
        choices=FEEDING_DURATION,
        null=True,
        blank=True,
        )
    correct_bf_duration = models.CharField(
        verbose_name=("4. What do you think the correct duration of breastfeeding should be"
                      " if a mother has HIV but taking Highly Active Antiretroviral Treatment"
                      " to prevent mother-to-child HIV transmission throughout breastfeeding: "),
        max_length=50,
        choices=CORRECT_BF_DURATION,
        )

    history = AuditTrail()

    class Meta:
        app_label = 'mpepu_maternal'
        verbose_name = "Post Natal Infant Feeding Survey"

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_postnatalinfantfeedingsurvey_change', args=(self.id,))
