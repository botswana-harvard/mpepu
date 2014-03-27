import factory

from edc.base.model.tests.factories import BaseUuidModelFactory

from apps.mpepu_infant.models import InfantFu

from .infant_visit_factory import InfantVisitFactory


class InfantFuFactory(BaseUuidModelFactory):
    FACTORY_FOR = InfantFu
    
    infant_visit = factory.SubFactory(InfantVisitFactory)
    physical_assessment = 'No'
    diarrhea_illness = 'No'
    has_dx = 'No'
