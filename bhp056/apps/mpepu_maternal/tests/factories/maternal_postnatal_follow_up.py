import factory

from edc.subject.registration.tests.factories import BaseRegistrationFactory
from edc.base.model.tests.factories import BaseUuidModelFactory

from apps.mpepu_maternal.models import MaternalPostFu
from apps.mpepu_maternal.tests.factories import MaternalVisitFactory

from edc.subject.registration.tests.factories.registered_subject_factory import RegisteredSubjectFactory


class MaternalPostFuFactory(BaseUuidModelFactory):
    FACTORY_FOR = MaternalPostFu

    maternal_visit = factory.SubFactory(MaternalVisitFactory)
    mother_weight = 'Yes'
    enter_weight = 65
    bp = '120/80'
    breastfeeding = 'No'
    has_chronic_cond = 'No'
    started_ctx = 'No'