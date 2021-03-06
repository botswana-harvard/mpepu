from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.base.model.fields.custom.custom_fields import OtherCharField
from edc.choices.common import YES_NO

from .base_scheduled_visit_model import BaseScheduledVisitModel
from .infant_fu import InfantFu


class InfantFuPhysical(BaseScheduledVisitModel):

    """Infant follow up physical assessment."""

    infant_fu = models.OneToOneField(InfantFu)

    weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Weight ",
        help_text="Measured in kg.",
        )
    height = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Height ",
        help_text="",
        )
    head_circumference = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="What was the head circumference in centimeters? ",
        help_text="Measured in centimeters, (cm)",
        )
    has_abnormalities = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="Abnormal findings ",
        help_text="If 'YES', continue, otherwise go to Question 8",
        )
    abnormalities = OtherCharField(
        max_length=100,
        verbose_name="Describe abnormal physical findings",
        blank=True,
        null=True,
        )
    was_hospitalized = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Has the child been hospitalized overnight since the last scheduled visit (or since discharge after birth,if this is the randomization visit)?",
        help_text=" If 'Yes', the primary diagnosis(es) associated with the hospitalization(s) must be recorded in follow up diagnoses section.",
        )
    days_hospitalized = models.IntegerField(
        verbose_name="If 'Yes', total number of days of hospitalization since the last scheduled visit.",
        help_text="",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def __unicode__(self):
        return unicode(self.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantfuphysical_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant FollowUp: Physical"
        verbose_name_plural = "Infant FollowUp: Physical"
