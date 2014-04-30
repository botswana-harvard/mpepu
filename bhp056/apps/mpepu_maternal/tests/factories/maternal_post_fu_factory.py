import factory

from edc.base.model.tests.factories import BaseUuidModelFactory

from apps.mpepu_maternal.models import MaternalPostFu, MaternalPostFuDx
from apps.mpepu_maternal.tests.factories import MaternalVisitFactory


class MaternalPostFuFactory(BaseUuidModelFactory):
    FACTORY_FOR = MaternalPostFu

    maternal_visit = factory.SubFactory(MaternalVisitFactory)
    mother_weight = 'Yes'
    enter_weight = 65
    bp = '120/80'
    breastfeeding = 'No'
    has_chronic_cond = 'No'
    started_ctx = 'No'


class MaternalPostFuDxFactory(BaseUuidModelFactory):
    FACTORY_FOR = MaternalPostFuDx

    maternal_post_fu = factory.SubFactory(MaternalPostFuFactory)
    maternal_visit = factory.SubFactory(MaternalVisitFactory)
    mother_hospitalized = 'No'
    new_diagnoses = 'No'
    who_clinical_stage = 'No'