from edc.subject.off_study.mixins.off_study_mixin import OffStudyMixin

from .infant_off_study import InfantOffStudy


class InfantOffStudyMixin(OffStudyMixin):

    def get_off_study_cls(self):
        return InfantOffStudy
