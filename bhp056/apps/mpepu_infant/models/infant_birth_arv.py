from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO_UNKNOWN, YES_NO_UNKNOWN_NA
from edc.base.model.validators import date_not_future

from .base_scheduled_visit_model import BaseScheduledVisitModel
from .infant_birth import InfantBirth


class InfantBirthArv(BaseScheduledVisitModel):

    """infant arv information"""

    infant_birth = models.OneToOneField(InfantBirth)

    azt_after_birth = models.CharField(
        max_length=15,
        choices=YES_NO_UNKNOWN,
        verbose_name="Did infant receive AZT syrup after birth?",
        help_text="",
        )
    azt_dose_date = models.DateField(
        verbose_name="If yes,date of first dose of AZT?",
        help_text="",
        validators=[date_not_future, ],
        blank=True,
        null=True,
        )
    azt_additional_dose = models.CharField(
        max_length=15,
        choices=YES_NO_UNKNOWN_NA,
        verbose_name="Was the infant given additional doses of AZT before discharge from the hospital? ",
        help_text="if insufficient timing from delivery to next required dose has elapsed, please enter 'Not applicable'",
        )
    sdnvp_after_birth = models.CharField(
        max_length=15,
        choices=YES_NO_UNKNOWN,
        verbose_name="Did the infant receive single dose NVP after birth? ",
        help_text="",
        )
    nvp_dose_date = models.DateField(
        verbose_name="If yes Date of first Dose NVP? ",
        help_text="",
        validators=[date_not_future, ],
        blank=True,
        null=True,
        )

    additional_nvp_doses = models.CharField(
        max_length=15,
        choices=YES_NO_UNKNOWN_NA,
        verbose_name="Was the infant given additional doses of NVP before discharge from the hospital? ",
        help_text="Only applicable to breastfed infants of mothers not on HAART or on HAART < 6 weeks",
        )

    azt_discharge_supply = models.CharField(
        max_length=15,
        choices=YES_NO_UNKNOWN_NA,
        verbose_name="Was the infant discharged with a supply of AZT? ",
        help_text="if infant not yet discharged, please enter 'Not applicable'",
        )
    nvp_discharge_supply = models.CharField(
        max_length=15,
        choices=YES_NO_UNKNOWN_NA,
        verbose_name="Was the infant discharged with a supply of NVP? ",
        help_text="only applicable to breastfed infnats of mothers either not on HAART or on HAART <6 weeks",
        )
    infant_arv_comments = models.TextField(
        max_length=250,
        verbose_name="Comment if any additional pertinent information: ",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def __unicode__(self):
        return unicode(self.infant_birth)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantbirtharv_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Birth Record: ARV"
        verbose_name_plural = "Infant Birth Records: ARV"
