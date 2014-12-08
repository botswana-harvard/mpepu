from datetime import datetime, time
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.base.model.fields.custom.custom_fields import OtherCharField
from edc.base.model.validators import (datetime_not_before_study_start, datetime_not_future, datetime_is_after_consent, 
                                       date_not_future)
from edc.entry_meta_data.managers import EntryMetaDataManager

from .infant_visit import InfantVisit
from ..choices import INFANT_OFF_DRUG_REASON
from .base_infant_registered_subject_model import BaseInfantRegisteredSubjectModel


class InfantOffDrug(BaseInfantRegisteredSubjectModel):

    report_datetime = models.DateTimeField(
        verbose_name="Visit Date and Time",
        validators=[
            datetime_not_before_study_start,
            datetime_is_after_consent,
            datetime_not_future,
            ],
        default=datetime.today()
        )

    last_dose_date = models.DateField(
        verbose_name="Date of last dose of CTX or placebo (Today's date if stopping today):",
        help_text="",
        validators=[
            date_not_future, ],
        )
    reason_off = models.CharField(
        verbose_name="Reason for permanently discontinuing study drug (CTX or placebo): ",
        max_length=25,
        choices=INFANT_OFF_DRUG_REASON,
        help_text="")
    reason_off_other = OtherCharField(
        max_length=35,
        verbose_name="if other specify...",
        blank=True,
        null=True)

    history = AuditTrail()

    infant_visit = models.OneToOneField(InfantVisit)

    entry_meta_data_manager = EntryMetaDataManager(InfantVisit)

    def get_report_datetime(self):
        return self.report_datetime

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.registered_subject.relative_identifier

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantoffdrug_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Off-Drug (CTX or Placebo)"
        verbose_name_plural = "Infant Off-Drug (CTX or Placebo)"
