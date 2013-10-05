from datetime import datetime, time

from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.subject.off_study.models.base_off_study import BaseOffStudy


class InfantOffStudy(BaseOffStudy):

    history = AuditTrail()

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
        return datetime.combine(self.offstudy_date, time(0, 0))

    class Meta:
        verbose_name = "Infant Off-Study"
        verbose_name_plural = "Infant Off-Study"
        app_label = "mpepu_infant"
