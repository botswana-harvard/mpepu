import factory
from datetime import datetime
from edc.subject.registration.tests.factories import RegisteredSubjectFactory
from edc.base.model.tests.factories import BaseUuidModelFactory
from ..models import MaternalEligibilityAnte
from ..tests.factories import MaternalConsentFactory


class MaternalEligibilityAnteFactory(BaseUuidModelFactory):
    FACTORY_FOR = MaternalEligibilityAnte

    maternal_consent = factory.SubFactory(MaternalConsentFactory)
    registration_datetime = datetime.today()
    gestational_age = 27
    registered_subject = factory.SubFactory(RegisteredSubjectFactory)
