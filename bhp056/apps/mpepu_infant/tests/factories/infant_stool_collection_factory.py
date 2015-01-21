import factory
from datetime import datetime

from edc.base.model.tests.factories import BaseUuidModelFactory

from apps.mpepu_infant.models import InfantStoolCollection

from .infant_visit_factory import InfantVisitFactory


class InfantStoolCollectionFactory(BaseUuidModelFactory):
    FACTORY_FOR = InfantStoolCollection

    infant_visit = factory.SubFactory(InfantVisitFactory)
    sample_obtained = 'No'
