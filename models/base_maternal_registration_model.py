from bhp_registration.models import BaseRegistrationModel
from mpepu_maternal.managers import MaternalRegistrationModelManager
from maternal_off_study_mixin import MaternalOffStudyMixin
from maternal_off_study import MaternalOffStudy


class BaseMaternalRegistrationModel(MaternalOffStudyMixin, BaseRegistrationModel):

    objects = MaternalRegistrationModelManager()

    def get_off_study_cls(self):
        return MaternalOffStudy

    class Meta:
        abstract = True
