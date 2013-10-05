from edc.subject.off_study.mixins.off_study_mixin import OffStudyMixin

from .maternal_off_study import MaternalOffStudy


class MaternalOffStudyMixin(OffStudyMixin):

    def get_off_study_cls(self):
        return MaternalOffStudy
