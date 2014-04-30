import factory
from datetime import datetime

from edc.subject.registration.tests.factories import BaseRegistrationFactory
from edc.base.model.tests.factories import BaseUuidModelFactory

from apps.mpepu_maternal.models import MaternalPostReg

from edc.subject.registration.tests.factories.registered_subject_factory import RegisteredSubjectFactory


class MaternalPostRegFactory(BaseUuidModelFactory):
    FACTORY_FOR = MaternalPostReg
    
    registered_subject = factory.SubFactory(RegisteredSubjectFactory)    
    reg_datetime = datetime.today()