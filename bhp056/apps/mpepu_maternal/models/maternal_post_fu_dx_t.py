from django.core.urlresolvers import reverse
from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO
from edc.subject.adverse_event.choices import GRADING_SCALE

from apps.mpepu.choices import DX

from ..managers import MaternalPostFuDxTManager
from .maternal_base_uuid_model import MaternalBaseUuidModel
from .maternal_post_fu_dx import MaternalPostFuDx


class MaternalPostFuDxT(MaternalBaseUuidModel):

    """ Post-partum follow up of diagnosis (transactions). """

    maternal_post_fu = models.ForeignKey(MaternalPostFuDx)

    post_fu_dx = models.CharField(
        max_length=100,
        choices=DX,
        verbose_name="Diagnosis",
        blank=True,
        null=True,
        help_text="",
        )
    post_fu_specify = models.CharField(
        max_length=100,
        verbose_name="Diagnosis specification",
        help_text="",
        blank=True,
        null=True,
        )
    grade = models.IntegerField(
        max_length=3,
        choices=GRADING_SCALE,
        verbose_name="Grade",
        blank=True,
        null=True,
        )
    hospitalized = models.CharField(
        choices=YES_NO,
        max_length=3,
        verbose_name="Hospitalized",
        blank=True,
        null=True,
        help_text="",
        )

    history = AuditTrail()

    objects = MaternalPostFuDxTManager()

    def natural_key(self):
        return (self.post_fu_dx, ) + self.maternal_post_fu.natural_key()

    def get_visit(self):
        return self.maternal_post_fu.get_visit()

    def get_report_datetime(self):
        return self.maternal_post_fu.get_report_datetime()

    def get_subject_identifier(self):
        return self.maternal_post_fu.get_subject_identifier()

    def __unicode__(self):
        return unicode(self.get_visit())

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalpostfudxt_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Postnatal Follow-Up: DxT"
