from django.core.exceptions import ValidationError
from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.subject.appointment_helper.models import BaseAppointmentMixin
from edc.subject.consent.mixins.bw import IdentityFieldsMixin
from edc.subject.consent.models import BaseConsent
from edc.subject.registration.models import RegisteredSubject
from ..models import MaternalConsent, MaternalVisit


class ResistanceConsent(BaseAppointmentMixin, BaseConsent):
    """Model for  resistance sub study consent for mothers."""

    registered_subject = models.OneToOneField(RegisteredSubject, editable=False, null=True)

    history = AuditTrail()

    def save_new_consent(self, using=None, subject_identifier=None):
        """Confirms if Maternal Consent instance exists"""
        maternal_consent = MaternalConsent.objects.filter(first_name=self.first_name, identity=self.identity)
        if not maternal_consent.exists():
            raise ValidationError('Cannot locate maternal consent with first_name={0} and identity={1}'.format(self.first_name, self.identity))
        else:
            maternal_consent = MaternalConsent.objects.get(first_name=self.first_name, identity=self.identity)
            subject_identifier = maternal_consent.subject_identifier
        return subject_identifier

    def get_registration_datetime(self):
        return self.consent_datetime

    def get_subject_type(self):
        return 'maternal'

#     def post_save_resistance_study(self, *args, **kwargs):
#         """Adds a 2030R visit if the Resistance consent is saved.
#
#         Should not create the appointment if the Resistance Consent is not saved
#         """
#         if self.id:
#             Appointment = models.get_model('bhp_appointment', 'Appointment')
#             if Appointment.objects.filter(registered_subject=self.registered_subject, visit_definition__code='2030R', visit_instance='0'):
#                 if not ResistanceConsent.objects.filter(registered_subject=self.registered_subject).exists():
#                     raise ValidationError('Save failed. Ensure that the Resistance Consent is saved, if eligibility criteria is passed')
#             maternal_consent = MaternalConsent.objects.filter(registered_subject=self.registered_subject)
#             if not maternal_consent.exists():
#                 raise ValidationError('Save failed. MaternalConsent does not exist.')
#         super(ResistanceConsent, self).save(*args, **kwargs)

    class Meta:
        app_label = 'mpepu_maternal'
        verbose_name = 'ARV Resistance Consent'

# add Mixin fields to abstract class
for field in IdentityFieldsMixin._meta.fields:
    if field.name not in [fld.name for fld in ResistanceConsent._meta.fields]:
        field.contribute_to_class(ResistanceConsent, field.name)
#
# for field in ReviewAndUnderstandingFieldsMixin._meta.fields:
#     if field.name not in [fld.name for fld in ResistanceConsent._meta.fields]:
#         field.contribute_to_class(ResistanceConsent, field.name)
