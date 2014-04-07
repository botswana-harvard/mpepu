from datetime import datetime

from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

from edc.audit.audit_trail import AuditTrail

from ..managers import MaternalEnrollDxManager
from .maternal_base_uuid_model import MaternalBaseUuidModel
from .maternal_enroll_med import MaternalEnrollMed


class MaternalEnrollDx(MaternalBaseUuidModel):

    """ Model for Maternal Enrollment: Dx History viewable based on question 5a."""

    maternal_enroll_med = models.ForeignKey(MaternalEnrollMed)

    diagnosis = models.CharField(
        max_length=50,
        verbose_name="Diagnosis",
        help_text="",
        null=True,
        blank=True,
        )
    diagnosis_year = models.IntegerField(
        verbose_name="Year",
        validators=[MinValueValidator(1947), MaxValueValidator(datetime.today().year), ],
        null=True,
        blank=True,
        )

    history = AuditTrail()

    objects = MaternalEnrollDxManager()

    def natural_key(self):
        return (self.diagnosis, ) + self.maternal_enroll_med.natural_key()

    def get_report_datetime(self):
        return self.get_visit().get_report_datetime()

    def get_subject_identifier(self):
        return self.get_visit().get_subject_identifier()

    def get_visit(self):
        return self.maternal_enroll_med.maternal_visit

    def __unicode__(self):
        return unicode(self.get_visit())

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalenrolldx_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Enrollment: Dx History"
