#from django.db import models
#from django.core.urlresolvers import reverse
#from edc.audit.audit_trail import AuditTrail
#from edc.base.model.validators import eligible_if_no
#from edc.choices.common import YES_NO
#from base_maternal_consent import BaseMaternalConsent
#
#
#class MaternalConsentV2(BaseMaternalConsent):
#
#    """Model for maternal consent and registration model for mothers."""
#    is_incarcerated = models.CharField(
#        verbose_name="Is the participant under involuntary incarceration?",
#        max_length=3,
#        choices=YES_NO,
#        validators=[eligible_if_no, ],
#        help_text="( if 'YES' STOP patient cannot be enrolled )",
#        )
#
#    history = AuditTrail()
#
#    class Meta:
#        verbose_name = "Maternal Consent V2"
#        app_label = 'mpepu_maternal'
#
#    def get_absolute_url(self):
#        return reverse('admin:mpepu_maternal_maternalconsentv2_change', args=(self.id,))
