from edc.subject.consent.models import BaseConsentedUuidModel

from .maternal_off_study import MaternalOffStudy
from .maternal_off_study_mixin import MaternalOffStudyMixin


class MaternalBaseUuidModel(MaternalOffStudyMixin, BaseConsentedUuidModel):

    """ Base model for all maternal models """

    def get_off_study_cls(self):
        return MaternalOffStudy

    class Meta:
        abstract = True
