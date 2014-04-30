import factory
from datetime import datetime
from edc.subject.registration.tests.factories import RegisteredSubjectFactory
from edc.base.model.tests.factories import BaseUuidModelFactory
from apps.mpepu_maternal.models import MaternalEligibilityAnte
from apps.mpepu_maternal.tests.factories import MaternalConsentFactory


class MaternalEligibilityAnteFactory(BaseUuidModelFactory):
    FACTORY_FOR = MaternalEligibilityAnte

    maternal_consent = factory.SubFactory(MaternalConsentFactory)
#     registered_subject = factory.SubFactory(RegisteredSubjectFactory)
    registration_datetime = datetime.today()
    gestational_age = 27
    is_hiv_positive = 'Yes'
    agree_follow_up = 'Yes'
