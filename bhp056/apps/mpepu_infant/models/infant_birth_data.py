from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.urlresolvers import reverse
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
        verbose_name="1. What was the infant's birth weight? ",
        help_text="Measured in Kilograms (kg)",
        )
    infant_length = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        verbose_name="2. What was the infant's length at birth? ",
        help_text="Measured in centimeters, (cm)",
        )
    head_circumference = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="3. What was the head circumference in centimeters? ",
        help_text="Measured in centimeters, (cm)",
        )
    apgar_score = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="4. Was Apgar Score performed? ",
        help_text="If 'No' go to question 10. Otherwise complete question 9a-c",
        )
    apgar_score_min_1 = models.IntegerField(
        max_length=2,
        verbose_name="4a. At 1 minute: ",
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
        verbose_name="4b. At 5 minutes: ",
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
        verbose_name="4c. At 10 minutes: ",
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
        verbose_name="5. Were any congenital anomalies identified? ",
        help_text="If 'Yes' please complete the Congenital Anomalies Form (Form MP015)",
        )
    other_birth_info = models.TextField(
        max_length=250,
        verbose_name="6.Other birth information ",
        blank=True,
        null=True,
        )

    history = AuditTrail()

#     def save(self, *args, **kwargs):
#         super(InfantBirthData, self).save(*args, **kwargs)
#         if self.congenital_anomalities.lower() == 'yes':
#             model = get_model('mpepu_infant', 'infantcongenitalanomalies')
#             """add congenital anomalies form"""
#             AdditionalEntryBucket.objects.add_for(
#                 registered_subject=self.infant_visit.appointment.registered_subject,
#                 model=model,
#                 qset=Q(registered_subject=self.infant_visit.appointment.registered_subject),
#                 )

    def __unicode__(self):
        return unicode(self.infant_birth)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantbirthdata_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Birth Record: Data"
        verbose_name_plural = "Infant Birth Records: Data"
