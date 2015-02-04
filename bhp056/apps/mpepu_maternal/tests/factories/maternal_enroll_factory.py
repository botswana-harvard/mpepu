import factory
from datetime import datetime
from edc.base.model.tests.factories import BaseUuidModelFactory
from apps.mpepu_maternal.models import MaternalEnroll
from apps.mpepu_maternal.tests.factories import MaternalVisitFactory


class MaternalEnrollFactory(BaseUuidModelFactory):
    FACTORY_FOR = MaternalEnroll

    maternal_visit = factory.SubFactory(MaternalVisitFactory)
    report_datetime = datetime.today()
    recruit_source = 'BHP recruiter'
    recruitment_clinic = 'PHH'
    prev_pregnancies = 2
    prior_health_haart = 'No'
    prev_pregnancy_arv = 'No'
    weight = 50.3
    height = 120.1
    bp = '120/80'