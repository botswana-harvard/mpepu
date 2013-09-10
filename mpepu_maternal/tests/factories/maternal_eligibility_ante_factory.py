import factory
from datetime import datetime
from bhp_registration.tests.factories import RegisteredSubjectFactory
from bhp_base_model.tests.factories import BaseUuidModelFactory
from mpepu_maternal.models import MaternalEligibilityAnte
from mpepu_maternal.tests.factories import MaternalConsentFactory


class MaternalEligibilityAnteFactory(BaseUuidModelFactory):
    FACTORY_FOR = MaternalEligibilityAnte

    maternal_consent = factory.SubFactory(MaternalConsentFactory)
    registration_datetime = datetime.today()
    gestational_age = 27
    registered_subject = factory.SubFactory(RegisteredSubjectFactory)
