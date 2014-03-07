import factory
from edc.subject.off_study.tests.factories import BaseOffStudyFactory
from apps.mpepu_infant.models import InfantOffStudy


class InfantOffStudyFactory(BaseOffStudyFactory):
    FACTORY_FOR = InfantOffStudy
