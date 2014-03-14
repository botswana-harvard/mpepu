import factory
from edc.base.model.tests.factories import BaseUuidModelFactory
from apps.mpepu_infant.tests.factories import InfantBirthFactory
from apps.mpepu_infant.models import InfantPreEligibility


class InfantPreEligibilityFactory(BaseUuidModelFactory):
    FACTORY_FOR = InfantPreEligibility

    infant_birth = factory.SubFactory(InfantBirthFactory)
    weight = 4
    clinical_jaundice = 'No'
    anemia_neutropenia = 'No'
