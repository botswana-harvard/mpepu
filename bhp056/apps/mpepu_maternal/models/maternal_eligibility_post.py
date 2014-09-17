from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc.audit.audit_trail import AuditTrail

from .base_maternal_eligibility import BaseMaternalEligibility
from .maternal_eligibility_ante import MaternalEligibilityAnte


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

    def save(self):
        self.ante_natal_check(self)

    def ante_natal_check(self, eligibility_post, exception_cls=None):
        """If mother registered antenatally then eligibility post form should not be filled in"""
        if not exception_cls:
            exception_cls = ValidationError
        has_infant_pre_eligibility = MaternalEligibilityAnte.objects.filter(registered_subject=eligibility_post.registered_subject)

        if has_infant_pre_eligibility:
            raise exception_cls('This participant has been enrolled ante-natally. Please fill in the Post Natal Registration form instead.')

    def get_result_datetime(self):
        return self.registration_datetime

    def get_test_code(self):
        return 'HIV'

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternaleligibilitypost_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Eligibility Post-Partum"
        verbose_name_plural = "Maternal Eligibility Post-Partum"
