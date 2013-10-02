import factory
from edc.subject.visit_tracking.tests.factories import BaseVisitTrackingFactory
from ..models import MaternalVisit


class MaternalVisitFactory(BaseVisitTrackingFactory):
    FACTORY_FOR = MaternalVisit
