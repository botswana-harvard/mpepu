import factory
from edc.subject.consent.tests.factories import BaseConsentFactory
from apps.mpepu_maternal.models import MaternalConsent


class MaternalConsentFactory(BaseConsentFactory):
    FACTORY_FOR = MaternalConsent
