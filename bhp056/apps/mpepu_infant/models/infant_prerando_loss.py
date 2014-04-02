from django.db import models
from django.core.urlresolvers import reverse

from edc.base.model.fields.custom.custom_fields import OtherCharField
from edc.audit.audit_trail import AuditTrail

from apps.mpepu.choices import INFANT_PRE_RANDO_LOSS_REASON

from .base_infant_registered_subject_model import BaseInfantRegisteredSubjectModel


class InfantPrerandoLoss(BaseInfantRegisteredSubjectModel):

#    report_datetime = models.DateTimeField(
#        verbose_name='Report date/time',
#        null=True)

    reason_loss = models.TextField(
        max_length=250,
        verbose_name="Describe the reason that the infant who consented did not undergo randomization",
        )
    loss_code = models.CharField(
        verbose_name="Please code the primary reason for pre- randomization loss to follow up:",
        max_length=25,
        choices=INFANT_PRE_RANDO_LOSS_REASON,
        help_text="See Study Protocol for definition of 'Loss to follow up'. If \'refused\', explain in comments below",
        )
    reason_loss_other = OtherCharField(
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )
    comment = models.TextField(
        max_length=250,
        verbose_name="Comments (Please provide any additional information pertinent to the response given in  question 3)",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def __unicode__(self):
        return unicode(self.registered_subject)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantprerandoloss_change', args=(self.id,))

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.registered_subject.relative_identifier

    def get_report_datetime(self):
        return self.created

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Pre-Rando Loss"
