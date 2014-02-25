from django.db import models
from datetime import datetime

from edc.subject.consent.models.base_consented_uuid_model import BaseConsentedUuidModel
from edc.base.model.validators import datetime_not_before_study_start, datetime_not_future, datetime_is_after_consent

from .infant_off_study_mixin import InfantOffStudyMixin


class InfantBaseUuidModel(InfantOffStudyMixin, BaseConsentedUuidModel):

    """ Base model for all infant models """
    
    report_datetime = models.DateTimeField(
        verbose_name="Visit Date and Time",
        validators=[
            datetime_not_before_study_start,
            datetime_is_after_consent,
            datetime_not_future,
            ],
        default=datetime.today()
        )

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.get_visit().appointment.registered_subject.relative_identifier

    def get_subject_identifier(self):
        return self.get_visit().appointment.registered_subject.subject_identifier

    def get_report_datetime(self):
        return self.report_datetime

    class Meta:
        abstract = True
