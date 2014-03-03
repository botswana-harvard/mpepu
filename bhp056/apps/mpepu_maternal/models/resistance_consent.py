from django.core.exceptions import ValidationError
from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.subject.appointment_helper.models import BaseAppointmentMixin
from edc.subject.consent.mixins import ReviewAndUnderstandingFieldsMixin
from edc.subject.consent.mixins.bw import IdentityFieldsMixin
from edc.subject.consent.models import BaseConsent
from edc.subject.registration.models import RegisteredSubject
from edc.entry_meta_data.managers import EntryMetaDataManager
from ..models import MaternalConsent


class ResistanceConsent(BaseAppointmentMixin, BaseConsent):
    """Model for  resistance sub study consent for mothers."""

    registered_subject = models.OneToOneField(RegisteredSubject, editable=False, null=True)

    history = AuditTrail()

    def save_new_consent(self, using=None, subject_identifier=None):
        """Confirms if Maternal Consent instance exists"""
        if not MaternalConsent.objects.filter(first_name=self.first_name, identity=self.identity).exists():
            raise ValidationError('Cannot locate maternal consent with first_name={0} and identity={1}'.format(self.first_name, self.identity))
        else:
            maternal_consent = MaternalConsent.objects.get(first_name=self.first_name, identity=self.identity)
            subject_identifier = maternal_consent.subject_identifier
        return subject_identifier

    def get_registration_datetime(self):
        return self.consent_datetime

    def get_subject_type(self):
        return 'maternal'

    objects = models.Manager()

    entry_meta_data_manager = EntryMetaDataManager(RegisteredSubject)

    class Meta:
        app_label = 'mpepu_maternal'
        verbose_name = ' ARV Resistance Consent'

# add Mixin fields to abstract class
for field in IdentityFieldsMixin._meta.fields:
    if field.name not in [fld.name for fld in ResistanceConsent._meta.fields]:
        field.contribute_to_class(ResistanceConsent, field.name)

for field in ReviewAndUnderstandingFieldsMixin._meta.fields:
    if field.name not in [fld.name for fld in ResistanceConsent._meta.fields]:
        field.contribute_to_class(ResistanceConsent, field.name)
