import factory
from bhp_off_study.tests.factories import BaseOffStudyFactory
from mpepu_infant.models import InfantOffStudy


class InfantOffStudyFactory(BaseOffStudyFactory):
    FACTORY_FOR = InfantOffStudy
