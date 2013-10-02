import factory
from datetime import datetime
from bhp_base_model.tests.factories import BaseUuidModelFactory
from ..models import MaternalLabDel
from ..tests.factories import MaternalVisitFactory
from apps.mpepu.choices import LABOUR_MODE_OF_DELIVERY, LABOUR_HOURS, DELIVERY_HOSPITAL


class MaternalLabDelFactory(BaseUuidModelFactory):
    FACTORY_FOR = MaternalLabDel

    maternal_visit = factory.SubFactory(MaternalVisitFactory)
    delivery_datetime = datetime.today()
    del_time_is_est = 'No'
    labour_hrs = LABOUR_HOURS[0][0]
    del_mode = LABOUR_MODE_OF_DELIVERY[0][0]
    has_ga = 'Yes'
    ga = 27
    del_hosp = DELIVERY_HOSPITAL[0][0]
    has_urine_tender = 'No'
    labr_max_temp = 36
    has_chorioamnionitis = 'No'
    has_del_comp = 'No'
    live_infants = 3
    live_infants_to_register = 2
    still_borns = 1
    still_born_has_congen_abn = 'No'
    still_born_congen_abn = 'No'
