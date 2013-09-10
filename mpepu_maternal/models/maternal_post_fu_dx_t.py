from django.db import models
from django.core.urlresolvers import reverse
from bhp_common.choices import YES_NO
from bhp_adverse.choices import GRADING_SCALE
from audit_trail.audit import AuditTrail
from mpepu.choices import DX
from mpepu_maternal.managers import MaternalPostFuDxTManager
from maternal_base_uuid_model import MaternalBaseUuidModel
from maternal_post_fu_dx import MaternalPostFuDx


class MaternalPostFuDxT(MaternalBaseUuidModel):

    """ Post-partum follow up of diagnosis (transactions). """

    maternal_post_fu = models.ForeignKey(MaternalPostFuDx)

    post_fu_dx = models.CharField(
        max_length=100,
        choices=DX,
        verbose_name="Diagnosis",
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
        )
    hospitalized = models.CharField(
        choices=YES_NO,
        max_length=3,
        verbose_name="Hospitalized",
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