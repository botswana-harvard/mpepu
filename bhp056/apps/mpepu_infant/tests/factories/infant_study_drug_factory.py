import factory
from datetime import datetime

from edc.base.model.tests.factories import BaseUuidModelFactory
from edc.subject.visit_tracking.tests.factories import BaseVisitTrackingFactory

from apps.mpepu_infant.models import InfantFu, InfantFuPhysical, InfantFuDx, InfantStudyDrug

from .infant_visit_factory import InfantVisitFactory


class InfantStudyDrugFactory(BaseUuidModelFactory):
    FACTORY_FOR = InfantStudyDrug

    infant_visit = factory.SubFactory(InfantVisitFactory)
    on_placebo_status = 'Yes'
    drug_status = 'No modification'