from datetime import datetime, time
from django.db import models
from django.core.urlresolvers import reverse
from audit_trail.audit import AuditTrail
from bhp_base_model.validators import datetime_not_before_study_start, datetime_not_future
from mpepu_infant.models import InfantVisit
from base_infant_registered_subject_model import BaseInfantRegisteredSubjectModel


class InfantVitalStatus(BaseInfantRegisteredSubjectModel):

    infant_visit = models.ForeignKey(InfantVisit, null=True)

    report_datetime = models.DateTimeField(
        verbose_name="Today's date",
        null=True,
        blank=False,
        validators=[
            datetime_not_before_study_start,
            datetime_not_future,
            ],
        )

    history = AuditTrail()

    objects = models.Manager()

    def get_registration_datetime(self):
        return datetime.combine(self.registered_subject.dob, time(0, 0))

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.registered_subject.relative_identifier

    def __unicode__(self):
        return unicode(self.registered_subject)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantvitalstatus_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Vital Status"
        verbose_name_plural = "Infant Vital Status"
