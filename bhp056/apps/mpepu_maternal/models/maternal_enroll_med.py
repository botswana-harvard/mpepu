from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.base.model.fields.custom.custom_fields import OtherCharField
from edc.choices.common import YES_NO

from apps.mpepu_list.models.maternal_enroll import ChronicCond

from .base_scheduled_visit_model import BaseScheduledVisitModel
from .maternal_enroll import MaternalEnroll


class MaternalEnrollMed(BaseScheduledVisitModel):

    """Model for Maternal Enrollment: Med History"""

    maternal_enroll = models.OneToOneField(MaternalEnroll)

    has_chronic_cond = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="Does the mother have any significant chronic condition(s) that were diagnosed prior to the current pregnancy and that remain ongoing?",
        )
    chronic_cond = models.ManyToManyField(ChronicCond,
        verbose_name="Chronic Diagnosis. Tick all that apply",
        help_text="",
        )
    chronic_cond_other = OtherCharField(
        max_length=35,
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )
    who_diagnosis = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="Prior to the current pregnancy, was the participant ever diagnosed with a WHO Stage III or IV illness?",
        help_text="Please use the WHO Staging Guidelines. if 'YES' complete table below",
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % (self.maternal_enroll)

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalenrollmentmedhistory_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Enrollment: Med History"
