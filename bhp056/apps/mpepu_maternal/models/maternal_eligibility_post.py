from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc.audit.audit_trail import AuditTrail

from .base_maternal_eligibility import BaseMaternalEligibility


class MaternalEligibilityPost(BaseMaternalEligibility):

    """ Maternal Eligiblity determined post-partum """

    days_pnc = models.IntegerField(
        verbose_name="3.How many days postnatal? ",
        help_text="if >34 days, ineligible",
        validators=[
            MaxValueValidator(34),
            MinValueValidator(0)
            ]
        )

    history = AuditTrail()

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternaleligibilitypost_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Eligibility Post-Partum"
        verbose_name_plural = "Maternal Eligibility Post-Partum"
