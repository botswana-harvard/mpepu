import factory
from datetime import date
from edc.base.model.tests.factories import BaseUuidModelFactory
from apps.mpepu_infant.tests.factories import InfantBirthFactory, InfantVisitFactory
from apps.mpepu_infant.models import InfantBirthData


class InfantBirthDataFactory(BaseUuidModelFactory):
    FACTORY_FOR = InfantBirthData

    infant_visit = factory.SubFactory(InfantVisitFactory)
    infant_birth = factory.SubFactory(InfantBirthFactory)
    infant_birth_weight = 4
    infant_length = 25
    head_circumference = 20
    apgar_score = 'No'
    congenital_anomalities = 'No'
