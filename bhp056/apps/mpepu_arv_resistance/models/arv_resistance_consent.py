from django.core.exceptions import ValidationError
from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.subject.appointment_helper.models import BaseAppointmentMixin
from edc.subject.consent.mixins import ReviewAndUnderstandingFieldsMixin
from edc.subject.consent.mixins.bw import IdentityFieldsMixin
from edc.subject.consent.models import BaseConsent
from edc.subject.registration.models import RegisteredSubject

from apps.mpepu_maternal.models import MaternalConsent


class ArvResistanceConsent(BaseAppointmentMixin, BaseConsent):
    """Model for ARV resistance sub study consent for mothers."""
    
    registered_subject = models.OneToOneField(RegisteredSubject,editable=False, null=True)

    history = AuditTrail()
   
    def save_new_consent(self, using=None,subject_identifier=None):
        """Confirms if Maternal Consent instance exists"""
        
        if not MaternalConsent.objects.filter(first_name=self.first_name, identity=self.identity).exists():
            raise ValidationError('Cannot locate maternal consent with first_name={0} and identity={1}'.format(self.first_name, self.identity))
        
        else:
            maternal_consent = MaternalConsent.objects.get(first_name=self.first_name, identity=self.identity)
            subject_identifier = maternal_consent.subject_identifier  
        return subject_identifier
    
    def __unicode__(self):
        return '%s: %s %s' % (self.subject_identifier, self.first_name, self.last_name)
    
    def get_registration_datetime(self):
        return self.consent_datetime
    
    def get_subject_type(self):
        return 'maternal'
    
#     def get_registered_subject(self):
#         return RegisteredSubject.objects.get(subject_identifier=self.subject_identifier)
#     
#     def get_subject_identifier(self):
#         return self.subject_identifier
    
    class Meta:
        app_label = 'mpepu_arv_resistance'
        verbose_name = 'ARV Resistance Consent'
        
# add Mixin fields to abstract class
for field in IdentityFieldsMixin._meta.fields:
    if field.name not in [fld.name for fld in ArvResistanceConsent._meta.fields]:
        field.contribute_to_class(ArvResistanceConsent, field.name)

for field in ReviewAndUnderstandingFieldsMixin._meta.fields:
    if field.name not in [fld.name for fld in ArvResistanceConsent._meta.fields]:
        field.contribute_to_class(ArvResistanceConsent, field.name)

            