from datetime import datetime, time

from django.core.urlresolvers import reverse
from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.base.model.validators import datetime_not_before_study_start, datetime_not_future, datetime_is_after_consent
from edc.subject.off_study.models.base_off_study import BaseOffStudy
from edc.entry_meta_data.managers import EntryMetaDataManager

from .infant_visit import InfantVisit


class InfantOffStudy(BaseOffStudy):

    history = AuditTrail()

    infant_visit = models.OneToOneField(InfantVisit)

    report_datetime = models.DateTimeField(
        verbose_name="Visit Date and Time",
        validators=[
            datetime_not_before_study_start,
            datetime_is_after_consent,
            datetime_not_future,
            ],
        default=datetime.today()
        )

    def __unicode__(self):
        return "%s" % (self.registered_subject.subject_identifier)

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.registered_subject.relative_identifier

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantoffstudy_change', args=(self.id,))

    def get_date_grouping_field(self):
        #set field for date-based grouping
        return 'offstudy_date'

    def get_report_datetime(self):
        return self.report_datetime

    entry_meta_data_manager = EntryMetaDataManager(InfantVisit)

    class Meta:
        verbose_name = "Infant Off-Study"
        verbose_name_plural = "Infant Off-Study"
        app_label = "mpepu_infant"
