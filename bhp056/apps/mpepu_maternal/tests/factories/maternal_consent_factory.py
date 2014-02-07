import factory
from bhp_botswana.tests.factories import BaseConsentFactory
from ..models import MaternalConsent


class MaternalConsentFactory(BaseConsentFactory):
    FACTORY_FOR = MaternalConsent
