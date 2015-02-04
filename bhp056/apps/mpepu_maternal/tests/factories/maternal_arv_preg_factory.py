import factory
from datetime import datetime
from edc.base.model.tests.factories import BaseUuidModelFactory
from apps.mpepu_maternal.models import MaternalArvPreg
from apps.mpepu_maternal.tests.factories import MaternalVisitFactory


class MaternalArvPregFactory(BaseUuidModelFactory):
    FACTORY_FOR = MaternalArvPreg

    maternal_visit = factory.SubFactory(MaternalVisitFactory)
    report_datetime = datetime.today()
    took_arv = 'No'
    sd_nvp = 'Yes'
    start_pp = 'No'