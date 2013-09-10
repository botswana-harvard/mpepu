from bhp_registration.models import BaseRegisteredSubjectModel
from maternal_off_study_mixin import MaternalOffStudyMixin


class MaternalBaseRegisteredSubjectModel(MaternalOffStudyMixin, BaseRegisteredSubjectModel):

    class Meta:
        abstract = True
