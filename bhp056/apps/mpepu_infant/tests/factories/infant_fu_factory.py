import factory
from datetime import datetime

from edc.base.model.tests.factories import BaseUuidModelFactory

from apps.mpepu_infant.models import InfantFu, InfantFuPhysical

from .infant_visit_factory import InfantVisitFactory


class InfantFuFactory(BaseUuidModelFactory):
    FACTORY_FOR = InfantFu

    infant_visit = factory.SubFactory(InfantVisitFactory)
    physical_assessment = 'Yes'
    diarrhea_illness = 'Yes'
    has_dx = 'Yes'
    report_datetime = datetime.today()


class InfantFuPhysicalFactory(BaseUuidModelFactory):
    FACTORY_FOR = InfantFuPhysical

    infant_fu = factory.SubFactory(InfantFu)
    infant_visit = factory.SubFactory(InfantVisitFactory)
    weight = 4
    height = 98
    head_circumference = 15
    has_abnormalities = 'No'
    was_hospitalized = 'Yes'
