import factory
from datetime import datetime

from edc.subject.registration.tests.factories import RegisteredSubjectFactory
from edc.subject.registration.tests.factories import BaseRegistrationFactory
from apps.mpepu_maternal.models import MaternalEligibilityPost
from apps.mpepu_maternal.tests.factories import MaternalConsentFactory


class MaternalEligibilityPostFactory(BaseRegistrationFactory):
    FACTORY_FOR = MaternalEligibilityPost

    maternal_consent = factory.SubFactory(MaternalConsentFactory)
#     registered_subject = factory.SubFactory(RegisteredSubjectFactory)
    days_pnc = 20
    is_hiv_positive = 'Yes'
    agree_follow_up = 'Yes'
    is_cd4_low = 250
    feeding_choice = 'No'
    maternal_haart = 'Yes'
