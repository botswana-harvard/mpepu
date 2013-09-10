from bhp_off_study.mixins import OffStudyMixin
from infant_off_study import InfantOffStudy


class InfantOffStudyMixin(OffStudyMixin):

    def get_off_study_cls(self):
        return InfantOffStudy
