from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail

from apps.mpepu_list.models.infant_vaccines import InfantVaccines

from ..choices import FEEDING_CHOICES
from .base_scheduled_visit_model import BaseScheduledVisitModel
from .infant_birth import InfantBirth


class InfantBirthFeed(BaseScheduledVisitModel):

    """infant feeding"""

    infant_birth = models.OneToOneField(InfantBirth)

    feeding_after_delivery = models.CharField(
        max_length=50,
        choices=FEEDING_CHOICES,
        verbose_name="1. How was the infant being fed immediately after delivery? ",
        help_text=" ...before discharge from maternity",
        )

    vaccination = models.ManyToManyField(InfantVaccines,
        verbose_name="2. Since delivery, did the child receive any of the following vaccinations",
        help_text="Select all that apply",
        )

    comments = models.TextField(
        max_length=250,
        verbose_name="Comment if any additional pertinent information: ",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def __unicode__(self):
        return unicode(self.infant_birth)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantbirthfeed_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Birth: Feeding & Vaccination"
        verbose_name_plural = "Infant Birth: Feeding & Vaccination"
