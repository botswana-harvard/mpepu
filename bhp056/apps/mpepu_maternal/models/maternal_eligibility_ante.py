from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail

from .base_maternal_eligibility import BaseMaternalEligibility


class MaternalEligibilityAnte(BaseMaternalEligibility):

    """Model for Maternal Eligiblity Ante-Natal"""

    gestational_age = models.IntegerField(
        verbose_name="Gestational age",
        help_text="if <26 weeks,ineligible",
        validators=[
            MaxValueValidator(43),
            MinValueValidator(26)
            ]
        )

    history = AuditTrail()

    def get_registration_datetime(self):
        return self.registration_datetime

    def __unicode__(self):
        return unicode(self.registered_subject)

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternaleligibilityante_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Eligibility Ante-Natal"
        verbose_name_plural = "Maternal Eligibility Ante-Natal"
