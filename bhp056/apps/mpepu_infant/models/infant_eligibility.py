import copy
from datetime import datetime, time

from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from edc.audit.audit_trail import AuditTrail
from edc.subject.consent.classes import ConsentHelper
from edc.choices.common import YES_NO, YES_NO_NA
from edc.base.model.validators import eligible_if_no

from apps.mpepu_infant_rando.classes import Eligibility

from ..choices import RANDOMIZATION_MATERNAL_ART_STATUS, RANDOMIZATION_MATERNAL_FEEDING_CHOICE, RANDOMIZATION_SITE
from .infant_birth import InfantBirth
from .base_infant_registered_subject_model import BaseInfantRegisteredSubjectModel
from .infant_visit import InfantVisit


class InfantEligibility(BaseInfantRegisteredSubjectModel):

    """ Determine eligibility of an infant to the study.

    In admin InfantEligibilityAdmin.save_model() call InfantRando.objects.randomize()

    """

    infant_birth = models.OneToOneField(InfantBirth)

    hiv_status = models.CharField(
        max_length=12,
        choices=YES_NO,
        verbose_name="2. Infant is known HIV positive  ",
        help_text="If yes, INELIGIBLE",
        validators=[
            eligible_if_no,
            ]
        )
    # added v2
    weight = models.DecimalField(
        verbose_name="Current weight",
        max_digits=3,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Measured in Kilograms (kg) (v2)",
        )

    clinical_jaundice = models.CharField(
        verbose_name='Does the baby look jaundice (yellow in colour)',
        max_length=3,
        choices=YES_NO,
        null=True,
        blank=True,
        help_text="Check whites of eyes. If yes, defer to 28 days (v2)",
        )

    anemia_neutropenia = models.CharField(
        verbose_name='Has known grade3/4 anemia, neutropenia or clinical evidence of anemia, neutropenia',
        max_length=3,
        choices=YES_NO,
        null=True,
        blank=True,
        help_text="If yes, defer to 28 days (v2)",
        )

    hiv_result_reference = models.CharField(
        max_length=25,
        verbose_name="2a. Sample identifier from HIV result (NEG)",
        validators=[
            RegexValidator('[A-Z]{2}[0-9]{5}|PENDING', 'Must be a valid BHP sample identifier OR the word PENDING'),
            ],
        help_text="If not yet tested, type 'PENDING'. Refer to protocol to understand when this is allowed.",
        null=True,
        blank=False,
        )

    ctx_contra = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="3. Any contraindication to Cotrimoxazole ",
        help_text="If yes, INELIGIBLE",
        validators=[
            eligible_if_no,
            ]
        )
    congen_anomaly = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="4. Known infant anomalies resulting in a high probability that the infant will not survive to 18 months.?",
        help_text="If yes, INELIGIBLE",
        validators=[
            eligible_if_no,
            ]
        )

    maternal_art_status = models.CharField(
        max_length=10,
        verbose_name="5a. Maternal ART Status",
        choices=RANDOMIZATION_MATERNAL_ART_STATUS,
        help_text="",
        )

    maternal_feeding_choice = models.CharField(
        max_length=2,
        verbose_name="5b. Feeding method / choice",
        choices=RANDOMIZATION_MATERNAL_FEEDING_CHOICE,
        help_text="",
        )
    #added v2 Q5bi only
    rando_bf_duration = models.CharField(
        verbose_name="5bi. Are you willing to be randomized for the breastfeeding duration?",
        max_length=15,
        choices=YES_NO_NA,
        null=True,
        blank=True,
        help_text="Must be answered if participant opts to breastfeed (v2 only)",
        )
    randomization_site = models.CharField(
        verbose_name="Randomization site",
        max_length=10,
        choices=RANDOMIZATION_SITE,
        )

    history = AuditTrail()

    def save(self, *args, **kwargs):
        #current_consent_version = ConsentHelper(self.infant_birth, exception_cls=ValidationError).get_current_consent_version()
        # TODO: not getting the correct current_consent_version so defaulting to 2 (2013-05-15)
        Eligibility().check(
            current_consent_version=2,  # defaulting to 2 (2013-05-15)!!
            dob=self.infant_birth.dob,
            ga=self.infant_birth.maternal_lab_del.ga,
            weight=self.weight,
            clinical_jaundice=self.clinical_jaundice,
            anemia_neutropenia=self.anemia_neutropenia,
            exception_cls=ValidationError,
            suppress_exception=False)
        
        super(InfantEligibility, self).save(*args, **kwargs)

    def post_save_delete_appointment(self):
        self.safe_delete_appointment('2015')

    def get_versioned_field_names(self, version_number):
        """Returns a list of field names by version number."""
        retval = []
        if version_number == 2:
            retval = ['clinical_jaundice', 'anemia_neutropenia', 'weight', 'rando_bf_duration']
        return retval

    def get_report_datetime(self):
        return self.get_registration_datetime()

    def get_registration_datetime(self):
        return self.infant_birth.maternal_lab_del.delivery_datetime

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.registered_subject.relative_identifier

    def __unicode__(self):
        return unicode(self.registered_subject)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infanteligibility_change', args=(self.id,))

    def get_infant_rando(self):
        InfantRando = models.get_model('mpepu_infant_rando', 'InfantRando')
        infant_rando = None
        if InfantRando.objects.filter(subject_identifier=self.registered_subject.subject_identifier).exists():
            infant_rando = InfantRando.objects.get(subject_identifier=self.registered_subject.subject_identifier)
        return infant_rando

    def feeding(self):
        infant_rando = self.get_infant_rando()
        retval = None
        if infant_rando:
            retval = infant_rando.feeding_choice
        return retval

    def duration(self):
        infant_rando = self.get_infant_rando()
        retval = None
        if infant_rando:
            retval = infant_rando.bf_duration
        return retval

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Eligibility"
        verbose_name_plural = "Infant Eligibility"
