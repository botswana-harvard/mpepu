import factory
from datetime import datetime
from edc.subject.visit_tracking.tests.factories import BaseVisitTrackingFactory
from apps.mpepu_maternal.models import MaternalVisit


class MaternalVisitFactory(BaseVisitTrackingFactory):
    FACTORY_FOR = MaternalVisit

    survival_status = 'ALIVE'
    date_last_alive = datetime.today()
