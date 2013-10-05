import factory
from edc.subject.off_study.tests.factories import BaseOffStudyFactory
from ..models import MaternalOffStudy


class MaternalOffStudyFactory(BaseOffStudyFactory):
    FACTORY_FOR = MaternalOffStudy
