from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from edc.audit.audit_trail import AuditTrail
from edc.subject.adverse_event.choices import GRADING_SCALE_34
from edc.choices.common import YES_NO
from edc.base.model.validators import datetime_not_before_study_start, datetime_not_future, datetime_is_after_consent

from .base_scheduled_visit_model import BaseScheduledVisitModel
from .infant_fu import InfantFu


class InfantFuD(BaseScheduledVisitModel):

    infant_fu = models.ForeignKey(InfantFu)

    diarrhea_grade = models.IntegerField(
        verbose_name="what was the grade of the diarrhea?",
        max_length=2,
        choices=GRADING_SCALE_34,
        help_text="only grade 3 or 4 allowed",
        validators=[
            MinValueValidator(3),
            MaxValueValidator(4),
            ]
        )
    
    d_onset_date = models.DateTimeField(
        verbose_name="Onset Date and Time",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future,
            ],
        )
    
    health_facility = models.CharField(
        verbose_name="Was the infant seen at the health facility for this diagnosis?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )
    
    hospitalized = models.CharField(
        verbose_name="Was the infant hospitalized?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )
    
    bloody_diarrhea = models.CharField(
        verbose_name="Was it bloody?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )
    
    fever_present = models.CharField(
        verbose_name="Was fever present?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )
    
    diarrhea_episodes = models.CharField(
        verbose_name="Number of separate episodes of diarrhea since last attended visit",
        max_length=3,
        help_text="an episode must be separated by at least 2 diarrhea free days(1,2,3,4,5,unknown) use -1 for unknown",
        )

    history = AuditTrail()

    objects = models.Manager()

    def __unicode__(self):
        return unicode(self.infant_fu.infant_visit)

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant FollowUp: Diarrhea"
