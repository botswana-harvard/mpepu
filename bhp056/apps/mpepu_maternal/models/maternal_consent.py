from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.subject.registration.models import RegisteredSubject

from .base_maternal_consent import BaseMaternalConsent


class MaternalConsent(BaseMaternalConsent):

    """Model for maternal consent and registration model for mothers."""

    history = AuditTrail()
 
    registered_subject = models.OneToOneField(RegisteredSubject,
        editable=False,
        null=True,
        help_text='')

    def get_registered_subject(self):
        reg_subject = None
        subject = RegisteredSubject.objects.filter(subject_identifier=self.subject_identifier)
        if subject:
            reg_subject = subject[0]
        return reg_subject

#     @property
#     def registered_subject(self):
#         return self.get_registered_subject()

    def dispatch_container_lookup(self):
        return None

    @classmethod
    def get_consent_update_model(self):
        return models.get_model('bhp_consent', 'MaternalConsentUpdate')

    class Meta:
        verbose_name = "Maternal Consent"
        app_label = 'mpepu_maternal'

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalconsent_change', args=(self.id,))
