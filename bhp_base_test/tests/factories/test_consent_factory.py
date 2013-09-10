import factory
from bhp_base_test.models import TestConsent, TestConsentWithMixin
from bhp_consent.tests.factories import BaseConsentFactory
#from bhp_registration.tests.factories import RegisteredSubjectFactory
from bhp_common.choices import IDENTITY_TYPE


class BaseTestConsentFactory(BaseConsentFactory):
    ABSTRACT_FACTORY = True

    #registered_subject = factory.SubFactory(RegisteredSubjectFactory)
    user_provided_subject_identifier = None
    identity = factory.Sequence(lambda n: '{0}2{1}'.format(str(n).rjust(4, '0'), str(n).rjust(4, '0')))
    identity_type = factory.Iterator(IDENTITY_TYPE, getter=lambda c: c[0])
    confirm_identity = factory.Sequence(lambda n: '{0}2{1}'.format(str(n).rjust(4, '0'), str(n).rjust(4, '0')))
    first_name = factory.Sequence(lambda n: 'ERIK{0}'.format(n))
    initials = factory.Sequence(lambda n: 'E{0}W'.format(n))

class TestConsentFactory(BaseConsentFactory):
    FACTORY_FOR = TestConsent


class TestConsentWithMixinFactory(BaseConsentFactory):
    FACTORY_FOR = TestConsentWithMixin
