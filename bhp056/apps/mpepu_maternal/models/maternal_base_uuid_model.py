from django.db import models

from edc.subject.consent.models import BaseConsentedUuidModel
from edc.base.model.validators import datetime_not_before_study_start, datetime_not_future, datetime_is_after_consent

from .maternal_off_study import MaternalOffStudy
from .maternal_off_study_mixin import MaternalOffStudyMixin


class MaternalBaseUuidModel(MaternalOffStudyMixin, BaseConsentedUuidModel):

    """ Base model for all maternal models """
    
    report_datetime = models.DateTimeField(
        verbose_name="Visit Date and Time",
        validators=[
            datetime_not_before_study_start,
            datetime_is_after_consent,
            datetime_not_future,
            ],
        )

    def get_off_study_cls(self):
        return MaternalOffStudy

    class Meta:
        abstract = True
