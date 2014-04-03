from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.base.model.fields.custom.custom_fields import OtherCharField

from apps.mpepu.choices import ALIVE_DECEASED, INFO_PROVIDER

from .base_infant_registered_subject_model import BaseInfantRegisteredSubjectModel


class InfantSurvival(BaseInfantRegisteredSubjectModel):

    infant_survival_status = models.CharField(
        verbose_name="Survival Status of the participant at 18 months of age? ",
        choices=ALIVE_DECEASED,
        max_length=25,
        help_text="",
        )
    info_provider = models.CharField(
        verbose_name="Who provided this information? ",
        choices=INFO_PROVIDER,
        max_length=25,
        help_text="",
        )
    info_provider_other = OtherCharField(
        max_length=35,
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )
    comment = OtherCharField(
        max_length=35,
        verbose_name="Comment",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def __unicode__(self):
        return self.registered_subject.subject_identifier

    def get_report_datetime(self):
        return self.registered_subject.registration_datetime

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.registered_subject.relative_identifier

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantsurvival_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Survival"
