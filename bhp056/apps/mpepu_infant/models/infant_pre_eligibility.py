from datetime import date

from django.db import models
from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO
from edc.subject.consent.classes import ConsentHelper
from edc.subject.appointment.models import Appointment

from apps.mpepu_infant_rando.mixins import InfantEligibilityMixin
from apps.mpepu_infant_rando.classes import Eligibility

from .infant_birth import InfantBirth
from .infant_eligibility import InfantEligibility
from .base_infant_registered_subject_model import BaseInfantRegisteredSubjectModel
from .infant_visit import InfantVisit


class InfantPreEligibility(InfantEligibilityMixin, BaseInfantRegisteredSubjectModel):

    """ Determine pre eligibility of an infant to the study.
    """

    infant_birth = models.OneToOneField(InfantBirth)

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

    history = AuditTrail()

    def save(self, *args, **kwargs):
        if not self.id:
            if InfantEligibility.objects.filter(infant_birth=self.infant_birth).exists():
                raise ValidationError('Save failed. InfantEligibility already submitted.')
            if not InfantVisit.objects.filter(appointment__registered_subject=self.registered_subject, appointment__visit_definition__code='2000').exists():
                raise ValidationError('Save failed. InfantVisit 2000 must be submitted before InfantPreEligibility.')
            if InfantVisit.objects.filter(appointment__registered_subject=self.registered_subject, appointment__visit_definition__code='2010').exists():
                raise ValidationError('Save failed. InfantVisit 2010 exists but should NOT have been submitted before InfantPreEligibility.')
            if abs((date.today() - self.infant_birth.dob).days) < 13:
                raise ValidationError('Save failed. Infant must be 14 days of life or older to verify eligibility.')
            #current_consent_version = ConsentHelper(self.infant_birth, exception_cls=ValidationError).get_current_consent_version()
            if Eligibility().check(
                    current_consent_version=2,  # TODO: defaulting to 2 (2013-05-15)!!
                    dob=self.infant_birth.dob,
                    ga=self.infant_birth.maternal_lab_del.ga,
                    weight=self.weight,
                    clinical_jaundice=self.clinical_jaundice,
                    anemia_neutropenia=self.anemia_neutropenia,
                    exception_cls=ValidationError,
                    suppress_exception=True):
                raise ValidationError('Save failed. Infant is eligible! Complete the InfantEligibility form instead of InfantPreEligibility. Perhaps catch this in forms module.')
        super(InfantPreEligibility, self).save(*args, **kwargs)

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

    def get_current_consent_version(self):
        """Confirms subject has a consent that covers data entry for this model."""
        return ConsentHelper(self).get_current_consent_version()

    def __unicode__(self):
        return unicode(self.registered_subject)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantpreeligibility_change', args=(self.id,))

    def post_save_recalculate_appt_date(self):
        """Adds a 2015 visit if pre-eligibility is saved.

        Should not create an appointment if infant is not yet 13 days old or is older than 33 days (14-34 days of life).

        Called by a signal.

        Calculations are days NOT days of life.
        """
        if abs((date.today() - self.infant_birth.dob).days) >= 13 and abs((date.today() - self.infant_birth.dob).days) <= 33:
            #allowing this 2015 visit to be created whether or not the gestational age is known
            if self.infant_birth.maternal_lab_del.has_ga == 'no' or self.infant_birth.maternal_lab_del.has_ga == 'yes':
                Appointment = models.get_model('bhp_appointment', 'Appointment')
                if not Appointment.objects.filter(registered_subject=self.registered_subject, visit_definition__code='2015', visit_instance='0'):
                    raise ImproperlyConfigured('Infant pre-eligibility expects 2015 appointment to exist. Check the visit definition.')
                appointment = Appointment.objects.get(registered_subject=self.registered_subject, visit_definition__code='2015', visit_instance='0')
                # do not change of visit form already completed
                if not InfantVisit.objects.filter(appointment__visit_definition__code='2015', appointment__registered_subject=self.registered_subject).exists():
                    appointment.appt_datetime = self.confirm_eligibility_datetime(appointment.appt_datetime, self.infant_birth.maternal_lab_del.delivery_datetime, 27)
                    appointment.best_appt_datetime = appointment.appt_datetime
                    appointment.raw_save()
        else:
            self.safe_delete_appointment('2015')
        return None

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Pre Eligibility"
        verbose_name_plural = "Infant Pre Eligibility"
