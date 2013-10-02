from django.db import models
from audit_trail.audit import AuditTrail
from django.core.urlresolvers import reverse
from base_maternal_consent import BaseMaternalConsent


class MaternalConsent(BaseMaternalConsent):

    """Model for maternal consent and registration model for mothers."""

    history = AuditTrail()

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
