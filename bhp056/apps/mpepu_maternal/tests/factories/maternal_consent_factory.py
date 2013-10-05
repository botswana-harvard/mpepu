import factory
from bhp_botswana.tests.factories import BaseBwConsentFactory
from ..models import MaternalConsent


class MaternalConsentFactory(BaseBwConsentFactory):
    FACTORY_FOR = MaternalConsent
