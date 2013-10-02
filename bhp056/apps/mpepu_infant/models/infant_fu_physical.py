from django.db import models
from django.core.urlresolvers import reverse
from edc.audit.audit_trail import AuditTrail
from bhp_base_model.fields import OtherCharField
from edc.choices.common import YES_NO
from .base_scheduled_visit_model import BaseScheduledVisitModel
from infant_fu import InfantFu


class InfantFuPhysical(BaseScheduledVisitModel):

    """Infant follow up physical assessment."""

    infant_fu = models.ForeignKey(InfantFu)

    weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="1a. Weight ",
        help_text="Measured in kg.",
        )
    height = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="1b. Height ",
        help_text="",
        )
    has_abnormalities = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="1c. Abnormal findings ",
        help_text="If 'YES', answer Question 1d, otherwise go to Question 2",
        )
    abnormalities = OtherCharField(
        max_length=100,
        verbose_name="1d. Describe abnormal physical findings",
        blank=True,
        null=True,
        )
    was_hospitalized = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="2. Has the child been hospitalized overnight since the last scheduled visit (or since discharge after birth,if this is the randomization visit)?",
        help_text=" If 'Yes', the primary diagnosis(es) associated with the hospitalization(s) must be recorded in follow up diagnoses section.",
        )
    days_hospitalized = models.IntegerField(
        verbose_name="2a. If 'Yes', total number of days of hospitalization since the last scheduled visit.",
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
