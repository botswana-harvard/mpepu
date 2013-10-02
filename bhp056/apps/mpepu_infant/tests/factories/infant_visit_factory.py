import factory
from bhp_visit_tracking.tests.factories import BaseVisitTrackingFactory
from mpepu_infant.models import InfantVisit


class InfantVisitFactory(BaseVisitTrackingFactory):
    FACTORY_FOR = InfantVisit
