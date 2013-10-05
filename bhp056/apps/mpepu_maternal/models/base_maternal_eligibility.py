from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from edc.choices.common import YES_NO
from edc.base.model.validators import eligible_if_yes

from ..classes import MaternalEligibilityConsentHelper
from .maternal_consent import MaternalConsent
from .base_maternal_registration_model import BaseMaternalRegistrationModel


class BaseMaternalEligibility(BaseMaternalRegistrationModel):

    """Base model for maternal eligibility forms (EN001/2)."""

    maternal_consent = models.OneToOneField(MaternalConsent,
        verbose_name="Mother's Consent"
        )

    is_hiv_positive = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="4. Evidence of confirmed HIV positive status",
        help_text="By indicating YES, you confirm that you  have copied such evidence for the patient chart",
        validators=[
            eligible_if_yes,
            ]
        )
    agree_follow_up = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="5. Is the participant willing to be followed up until the baby is 18 months of age?",
        help_text="if no ,INELIGIBLE",
        validators=[
            eligible_if_yes,
            ]
        )
    # added for v2
    is_cd4_low = models.IntegerField(
        verbose_name="6. What is the mother's lowest known CD4 count?",
        max_length=4,
        validators=[MinValueValidator(0), MaxValueValidator(3000)],
        null=True,
        blank=True,
        help_text="v2",
        )
    # added for v2
    feeding_choice = models.CharField(
        verbose_name="7. Does the mother plan to breastfeed?",
        max_length=3,
        null=True,
        blank=True,
        choices=YES_NO,
        help_text="v2",
        )
    # added for v2
    maternal_haart = models.CharField(
        verbose_name="8. Is the mother willing to initiate HAART or currently on HAART?",
        max_length=3,
        null=True,
        #blank=True,
        choices=YES_NO,
        help_text=("If mother is initiating HAART, infant will need continuous NVP until mother"
                   " has been treated for 6weeks (v2)"),
        )

    def get_versioned_field_names(self, version_number):
        """Returns a list of field names by version number."""
        retval = []
        if version_number == 2:
            retval = ['is_cd4_low', 'feeding_choice', 'maternal_haart']
        return retval

    def get_consent_helper_cls(self):
        return MaternalEligibilityConsentHelper

    def get_subject_identifier(self):
        return self.registered_subject.subject_identifier

    def get_result_value(self, attr=None):
        """Returns a result value for given attr name for the lab_tracker."""
        retval = None
        if not attr in dir(self):
            raise TypeError('Attribute {0} does not exist in model {1}'.format(attr, self._meta.object_name))
        if attr == 'is_hiv_positive':
            if self.is_hiv_positive.lower() == 'yes':
                retval = 'POS'
            else:
                retval = 'NEG'
        return retval

    class Meta:
        abstract = True
