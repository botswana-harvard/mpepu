from edc.subject.consent.models.base_consented_uuid_model import BaseConsentedUuidModel

from .infant_off_study_mixin import InfantOffStudyMixin


class InfantBaseUuidModel(InfantOffStudyMixin, BaseConsentedUuidModel):

    """ Base model for all maternal models """

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.get_visit().appointment.registered_subject.relative_identifier

    def get_subject_identifier(self):
        return self.get_visit().appointment.registered_subject.subject_identifier

    def get_report_datetime(self):
        return self.get_visit().report_datetime

    class Meta:
        abstract = True
