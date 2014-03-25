import factory
from edc.subject.consent.tests.factories import BaseConsentFactory
from apps.mpepu_maternal.models import ResistanceConsent


class ResistanceConsentFactory(BaseConsentFactory):
    FACTORY_FOR = ResistanceConsent
