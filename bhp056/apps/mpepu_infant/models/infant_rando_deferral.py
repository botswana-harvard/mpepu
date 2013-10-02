from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO
from mpepu_infant.models import InfantBirth
from base_infant_registered_subject_model import BaseInfantRegisteredSubjectModel


class InfantRandoDeferral(BaseInfantRegisteredSubjectModel):

    """Defer infant randomization if infant weight less than 2.5kg """

    infant_birth = models.OneToOneField(InfantBirth)

    weight = models.DecimalField(
        verbose_name="Current weight",
        max_digits=3,
        decimal_places=2,
        #validators=[MinValueValidator(0.50), MaxValueValidator(2.49)],
        help_text="Measured in Kilograms (kg) (v2)",
        )

    clinical_jaundice = models.CharField(
        verbose_name='Does the baby look jaundice (yellow in colour)',
        max_length=3,
        choices=YES_NO,
        help_text="Check whites of eyes. If yes, defer to 28 days (v2)",
        )

    anemia_neutropenia = models.CharField(
        verbose_name='Has known grade3/4 anemia, neutropenia or clinical evidence of anemia, neutropenia',
        max_length=3,
        choices=YES_NO,
        help_text="If yes, defer to 28 days (v2)",
        )

    history = AuditTrail()

    objects = models.Manager()

    def requires_appointment_2010(self, exception_cls=None):
        if not exception_cls:
            exception_cls = ValidationError
        Appointment = models.get_model('bhp_appointment', 'Appointment')
        if Appointment.objects.filter(registered_subject=self.registered_subject, visit_definition__code='2010'):
            appointment = Appointment.objects.get(registered_subject=self.registered_subject, visit_definition__code='2010')
        else:
            raise exception_cls('Infant randomization cannot be deferred. Unable to find the 2010 appointment.')
        return appointment

    def defer_appointment_2010(self):
        """Defers the rando 2010 appointment to 28 days from birth."""
        appointment = self.requires_appointment_2010()
        appointment.best_appt_datetime = datetime(self.infant_birth.dob.year, self.infant_birth.dob.month, self.infant_birth.dob.day) + relativedelta(days=28)
        appointment.appt_datetime = appointment.best_appt_datetime
        appointment.save()

    def save(self, *args, **kwargs):
        self.defer_appointment_2010()
        super(InfantRandoDeferral, self).save(*args, **kwargs)

    def get_registration_datetime(self):
        return datetime.combine(self.registered_subject.dob, time(0, 0))

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.registered_subject.relative_identifier

    def __unicode__(self):
        return unicode(self.registered_subject)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantrandodeferral_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = 'Infant Rando Deferral'
