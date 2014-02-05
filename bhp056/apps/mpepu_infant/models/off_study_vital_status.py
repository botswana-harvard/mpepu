from datetime import datetime
from django.db import models

from edc.base.model.validators import datetime_not_before_study_start, datetime_not_future, datetime_is_after_consent
from edc.subject.registration.models import BaseRegisteredSubjectModel

from apps.mpepu_infant.choices import ALIVE_DEAD_UNKNOWN

class OffStudyVitalStatus(BaseRegisteredSubjectModel):
    
    report_datetime = models.DateTimeField(
        verbose_name="Visit Date and Time",
        validators=[
            datetime_not_before_study_start,
            datetime_is_after_consent,
            datetime_not_future,
            ],
        default=datetime.today()
        )
    
    survival_status = models.CharField(
        max_length=10,
        verbose_name="Survival status",
        choices=ALIVE_DEAD_UNKNOWN,
        null=True,
        blank=False)

    date_last_alive = models.DateField(
        verbose_name="Date last known alive",
        help_text="",
        null=True,
        blank=True
        )
    
    class Meta:
        app_label = 'Off-Study Vital Status Update'
    