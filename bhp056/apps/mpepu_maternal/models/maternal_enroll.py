from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO, YES_NO_NA
from edc.base.model.fields.custom.custom_fields import OtherCharField

from apps.mpepu.choices import RECRUIT_SOURCE

from .base_scheduled_visit_model import BaseScheduledVisitModel


class MaternalEnroll(BaseScheduledVisitModel):

    """Model for Maternal enrollment (first of several).

        mp003

        this is not a registration form, just a form to collect 'other data'
        This form is initiated at the time of maternal enrollment,
        and can be completed and submitted any time before randomization
    """

    recruit_source = models.CharField(
        max_length=75,
        choices=RECRUIT_SOURCE,
        verbose_name="1. The mother first learned about the Mpepu study from ",
        help_text="",
        )
    recruit_source_other = OtherCharField(
        max_length=35,
        verbose_name="1a. if other specify...",
        blank=True,
        null=True,
        )

    prev_pregnancies = models.IntegerField(
        verbose_name="2. Not including this pregnancy, how many previous pregnancies for this participant?",
        help_text="",
        )

    prior_health_haart = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="3. Before this pregnancy, was the mother on HAART for her own health",
        help_text="For her own health and not just PMTCT for an earlier pregnancy or breastfeeding.",
        )

    prev_pregnancy_arv = models.CharField(
        max_length=25,
        choices=YES_NO_NA,
        verbose_name="4. Was the mother on any ARVs during previous pregnancies (or immediately following delivery) for PMTCT purposes (and not for her own health)? ",
        help_text="not including this pregnancy",
        )
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="5. Mother's weight? ",
        help_text="Measured in Kilograms (kg)",
        )
    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="6. Mother's height? ",
        help_text="Measured in Centimeters (cm)",
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s %s %s" % (self.maternal_visit.appointment.registered_subject, self.maternal_visit.appointment.visit_definition.code, self.maternal_visit.report_datetime)

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalenrollment_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Enrollment"
