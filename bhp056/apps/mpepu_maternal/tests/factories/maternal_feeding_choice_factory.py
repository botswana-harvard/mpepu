import factory
from datetime import datetime
from edc.base.model.tests.factories import BaseUuidModelFactory
from apps.mpepu_maternal.models import FeedingChoice
from apps.mpepu_maternal.tests.factories import MaternalVisitFactory


class FeedingChoiceFactory(BaseUuidModelFactory):
    FACTORY_FOR = FeedingChoice

    maternal_visit = factory.SubFactory(MaternalVisitFactory)
    report_datetime = datetime.today()
    first_time_feeding = 'No'