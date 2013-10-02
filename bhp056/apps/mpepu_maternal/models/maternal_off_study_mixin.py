from bhp_off_study.mixins import OffStudyMixin
from maternal_off_study import MaternalOffStudy


class MaternalOffStudyMixin(OffStudyMixin):

    def get_off_study_cls(self):
        return MaternalOffStudy
