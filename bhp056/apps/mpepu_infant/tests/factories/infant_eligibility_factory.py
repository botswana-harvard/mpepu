import factory
from datetime import date
from bhp_base_model.tests.factories import BaseUuidModelFactory
from bhp_registration.tests.factories import RegisteredSubjectFactory
from mpepu_maternal.tests.factories import MaternalLabDelFactory
from mpepu_infant.tests.factories import InfantBirthFactory
from mpepu_infant.models import InfantBirth, InfantEligibility


class InfantEligibilityFactory(BaseUuidModelFactory):
    FACTORY_FOR = InfantEligibility

    infant_birth = factory.SubFactory(InfantBirthFactory)
    hiv_status = 'Yes'
    weight = 4
    clinical_jaundice = 'No'
    anemia_neutropenia = 'No'
    hiv_result_reference = 'PENDING'
