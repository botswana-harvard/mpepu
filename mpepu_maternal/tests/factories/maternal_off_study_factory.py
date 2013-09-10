import factory
from bhp_off_study.tests.factories import BaseOffStudyFactory
from mpepu_maternal.models import MaternalOffStudy


class MaternalOffStudyFactory(BaseOffStudyFactory):
    FACTORY_FOR = MaternalOffStudy
