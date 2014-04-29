import factory

from edc.base.model.tests.factories import BaseUuidModelFactory

from apps.mpepu_maternal.models import MaternalArvPost, MaternalArvPostAdh
from apps.mpepu_maternal.tests.factories import MaternalVisitFactory


class MaternalArvPostFactory(BaseUuidModelFactory):
    FACTORY_FOR = MaternalArvPost

    maternal_visit = factory.SubFactory(MaternalVisitFactory)
    haart_last_visit = 'No'


class MaternalArvPostAdhFactory(BaseUuidModelFactory):
    FACTORY_FOR = MaternalArvPostAdh

    maternal_arv_post = factory.SubFactory(MaternalArvPostFactory)
    missed_doses = 0
