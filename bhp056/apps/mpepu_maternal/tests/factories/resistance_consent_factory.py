import factory
from edc.subject.consent.tests.factories import BaseConsentFactory
from apps.mpepu_maternal.models import ResistanceConsent
from .maternal_consent_factory import MaternalConsentFactory


class ResistanceConsentFactory(BaseConsentFactory):
    FACTORY_FOR = ResistanceConsent

#     maternal_consent = factory.SubFactory(MaternalConsentFactory)
