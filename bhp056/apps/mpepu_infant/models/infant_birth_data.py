from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Q, get_model

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO
# from edc.subject.entry.models import AdditionalEntryBucket

from .base_scheduled_visit_model import BaseScheduledVisitModel
from .infant_birth import InfantBirth


class InfantBirthData(BaseScheduledVisitModel):

    """birth data"""

    infant_birth = models.OneToOneField(InfantBirth)

    infant_birth_weight = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        verbose_name="What was the infant's birth weight? ",
        help_text="Measured in Kilograms (kg)",
        )
    infant_length = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        verbose_name="What was the infant's length at birth? ",
        help_text="Measured in centimeters, (cm)",
        )
    head_circumference = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="What was the head circumference in centimeters? ",
        help_text="Measured in centimeters, (cm)",
        )
    apgar_score = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Was Apgar Score performed? ",
        help_text="If 'No' go to question 10. Otherwise continue",
        )
    apgar_score_min_1 = models.IntegerField(
        max_length=2,
        verbose_name="At 1 minute: ",
        help_text="-1 if unknown",
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(-1)
            ]
        )
    apgar_score_min_5 = models.IntegerField(
        max_length=2,
        verbose_name="At 5 minutes: ",
        help_text="-1 if unknown",
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(-1)
            ]
        )
    apgar_score_min_10 = models.IntegerField(
        max_length=2,
        verbose_name="At 10 minutes: ",
        help_text="-1 if unknown",
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(-1)
            ]
        )
    congenital_anomalities = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Were any congenital anomalies identified? ",
        help_text="If 'Yes' please complete the Congenital Anomalies Form (Form MP015)",
        )
    other_birth_info = models.TextField(
        max_length=250,
        verbose_name="Other birth information ",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def __unicode__(self):
        return unicode(self.infant_birth)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantbirthdata_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Birth Record: Data"
        verbose_name_plural = "Infant Birth Records: Data"
