import factory
from datetime import datetime, date

from edc.subject.consent.tests.factories import BaseConsentFactory
from edc.subject.registration.tests.factories import RegisteredSubjectFactory

from apps.mpepu_maternal.models import MaternalConsent


class MaternalConsentFactory(BaseConsentFactory):
    FACTORY_FOR = MaternalConsent

    identity = factory.Sequence(lambda n: 'identity{0}'.format(n))
    gender = 'F'
