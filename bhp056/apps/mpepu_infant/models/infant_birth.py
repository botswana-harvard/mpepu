from datetime import timedelta

from django.db import models
from django.core.exceptions import ImproperlyConfigured
from django.core.validators import MinValueValidator, MaxValueValidator

from edc.audit.audit_trail import AuditTrail
from edc.base.model.fields.custom.custom_fields import InitialsField
from edc.choices.common import GENDER_UNDETERMINED
from edc.subject.consent.classes import ConsentHelper
from edc.base.model.validators import date_not_future
from edc.subject.appointment_helper.classes import AppointmentDateHelper
from edc.core.crypto_fields.fields import EncryptedFirstnameField

from apps.mpepu_maternal.models.maternal_lab_del import MaternalLabDel
from apps.mpepu_infant_rando.mixins import InfantEligibilityMixin

from .base_infant_registered_subject_model import BaseInfantRegisteredSubjectModel
from .infant_visit import InfantVisit


class InfantBirth(InfantEligibilityMixin, BaseInfantRegisteredSubjectModel):

    """MP008 - Infant Birth Record """

    maternal_lab_del = models.ForeignKey(MaternalLabDel,
        verbose_name="Mother's delivery record")
    first_name = EncryptedFirstnameField(
        #max_length = 250,
        verbose_name="Infant's first name",
        help_text="If infant name is unknown or not yet determined, use Baby + birth order + mother's last name, e.g. 'Baby1Malane'")
    initials = InitialsField()
    birth_order = models.IntegerField(
        verbose_name='Birth Order',
        help_text="For example, 1, 2, 3, .... Is also implied by infant identifier suffix.",
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(4), ])
    dob = models.DateField(
        verbose_name='Date of Birth',
        validators=[date_not_future, ],
        help_text="Must match labour and delivery report.")
    gender = models.CharField(
        max_length=10,
        choices=GENDER_UNDETERMINED)
    objects = models.Manager()
    history = AuditTrail()

    def get_report_datetime(self):
        return self.get_registration_datetime()

    def get_registration_datetime(self):
        return self.maternal_lab_del.delivery_datetime

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.registered_subject.relative_identifier

    def get_current_consent_version(self):
        """Confirms subject has a consent that covers data entry for this model."""
        return ConsentHelper(self).get_current_consent_version()

    def __unicode__(self):
        return '%s [%s] %s %s' % (self.registered_subject.subject_identifier, self.initials, self.dob, self.get_gender_display())

    #def get_absolute_url(self):
    #    return reverse('admin:mpepu_infant_infantbirth_change', args=(self.id,))

    def get_date_grouping_field(self):
        #set field for date-based grouping
        return 'dob'

    def post_save_recalculate_appt_date(self):
        """Finds the 2010 infant visit and changes the date to 13 days from 2000 visit if required.

        Called by a signal.

        Calculations are days NOT days of life.

        Most of this protects from the ApointmentDateHelper that will move an appointment
        backwards if it lands on a Saturday. Here we always want it to move forward.

        Criteria are : if ga >= 36, set to 13 days from delivery_datetime, otherwise 27 days (+1 on each for days of life)"""
        if self.maternal_lab_del.has_ga:
            Appointment = models.get_model('bhp_appointment', 'Appointment')
            if not Appointment.objects.filter(registered_subject=self.registered_subject, visit_definition__code='2010', visit_instance='0'):
                raise ImproperlyConfigured('Infant birth expects 2010 visit to exist. Check the visit definition.')
            appointment = Appointment.objects.get(registered_subject=self.registered_subject, visit_definition__code='2010', visit_instance='0')
            # do not change of visit form already completed
            if not InfantVisit.objects.filter(appointment__visit_definition__code='2010', appointment__registered_subject=self.registered_subject).exists():
                if self.maternal_lab_del.ga >= 36:
                    appointment.appt_datetime = self.confirm_eligibility_datetime(appointment.appt_datetime, self.maternal_lab_del.delivery_datetime, 13)
                    appointment.best_appt_datetime = appointment.appt_datetime
                    appointment.raw_save()
                else:
                    appointment.appt_datetime = self.confirm_eligibility_datetime(appointment.appt_datetime, self.maternal_lab_del.delivery_datetime, 27)
                    appointment.best_appt_datetime = appointment.appt_datetime
                    appointment.raw_save()
                    #appointment = Appointment.objects.get(registered_subject=self.registered_subject, visit_definition__code='2010', visit_instance='0')
                    #print '{0}, {1}'.format(appointment.appt_datetime.strftime("%A"), (appointment.appt_datetime - self.maternal_lab_del.delivery_datetime).days)
        return None

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Birth Record"
        unique_together = ['registered_subject', 'maternal_lab_del', ]
        unique_together = ['birth_order', 'maternal_lab_del', ]
        unique_together = ['first_name', 'maternal_lab_del', ]
        unique_together = ['initials', 'maternal_lab_del', ]
