from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.base.model.fields.custom.custom_fields import OtherCharField
from edc.choices.common import GENDER_UNDETERMINED, NORMAL_ABNORMAL, NORMAL_ABNORMAL_NOEXAM, YES_NO_NOT_EVALUATED_NA

from .base_scheduled_visit_model import BaseScheduledVisitModel
from .infant_birth import InfantBirth


class InfantBirthExam(BaseScheduledVisitModel):

    """infant examiniation"""

    infant_birth = models.OneToOneField(InfantBirth)

    infant_exam_date = models.DateField(
        verbose_name="Date of infant examination",
        help_text="",
        )
    gender = models.CharField(
        max_length=15,
        choices=GENDER_UNDETERMINED,
        verbose_name="Gender? ",
        help_text="",
        )
    general_activity = models.CharField(
        max_length=15,
        choices=NORMAL_ABNORMAL,
        verbose_name="General Activity? ",
        help_text="Report general activity ON THE DAY of the exam.",
        )
    abnormal_activity = OtherCharField(
        verbose_name="If abnormal (specify)",
        blank=True,
        null=True,
        )
    physical_exam_result = models.CharField(
        max_length=15,
        choices=NORMAL_ABNORMAL_NOEXAM,
        verbose_name="What was the result of the Physical Exam? ",
        help_text="",
        )
    heent_exam = models.CharField(
        max_length=15,
        choices=YES_NO_NOT_EVALUATED_NA,
        verbose_name="Was HEENT Exam Normal? ",
        help_text="",
        default="N/A",
        )
    heent_no_other = models.TextField(
        verbose_name="If abnormal or not evaluated, specify",
        blank=True,
        null=True,
        )
    resp_exam = models.CharField(
        max_length=15,
        choices=YES_NO_NOT_EVALUATED_NA,
        verbose_name="Was Respiratory Exam Normal?",
        help_text="",
        default="N/A",
        )
    resp_exam_other = models.TextField(
        verbose_name="If abnormal or not evaluated, specify",
        blank=True,
        null=True,
        )
    cardiac_exam = models.CharField(
        max_length=15,
        choices=YES_NO_NOT_EVALUATED_NA,
        verbose_name="Was Cardiac Exam Normal?",
        help_text="",
        default="N/A",
        )
    cardiac_exam_other = models.TextField(
        verbose_name="If abnormal or not evaluated,(specify)",
        blank=True,
        null=True,
        )
    abdominal_exam = models.CharField(
        max_length=15,
        choices=YES_NO_NOT_EVALUATED_NA,
        verbose_name="Was Abdominal Exam Normal?",
        help_text="",
        default="N/A",
        )
    abdominal_exam_other = models.TextField(
        verbose_name="If abnormal or not evaluated, specify",
        blank=True,
        null=True,
        )
    skin_exam = models.CharField(
        max_length=15,
        choices=YES_NO_NOT_EVALUATED_NA,
        verbose_name="Was Skin Exam Normal?",
        help_text="",
        default="N/A",
        )
    skin_exam_other = models.TextField(
        max_length=15,
        verbose_name="If abnormal or not evaluated, specify",
        help_text="",
        blank=True,
        null=True,
        )
    macular_papular_rash = models.CharField(
        max_length=15,
        choices=YES_NO_NOT_EVALUATED_NA,
        verbose_name="Was any macular / papular rash observed?",
        help_text="",
        default="N/A",
        )
    neurologic_exam = models.CharField(
        max_length=15,
        choices=YES_NO_NOT_EVALUATED_NA,
        verbose_name="Was Neurological Exam Normal?",
        help_text="",
        default="N/A",
        )
    neuro_exam_other = models.TextField(
        verbose_name="If abnormal or not evaluated, specify",
        blank=True,
        null=True,
        )
    other_exam_info = models.TextField(
        max_length=250,
        verbose_name="Other infant exam information",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def __unicode__(self):
        return unicode(self.infant_birth)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantbirthexam_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Birth Record: Exam"
        verbose_name_plural = "Infant Birth Records: Exam"
