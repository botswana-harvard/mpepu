import factory
from datetime import datetime
from edc.subject.registration.tests.factories import BaseRegistrationFactory

from edc.base.model.tests.factories import BaseUuidModelFactory
from apps.mpepu_maternal.models import MaternalEligibilityPost
from apps.mpepu_maternal.tests.factories import MaternalConsentFactory


class MaternalEligibilityPostFactory(BaseRegistrationFactory):
    FACTORY_FOR = MaternalEligibilityPost

    days_pnc = 20
    is_hiv_positive = 'Yes'
    agree_follow_up = 'Yes'
    maternal_consent = factory.SubFactory(MaternalConsentFactory)
