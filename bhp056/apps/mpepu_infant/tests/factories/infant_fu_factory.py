import factory

from edc.base.model.tests.factories import BaseUuidModelFactory

from apps.mpepu_infant.models import InfantFu


class InfantFuFactory(BaseUuidModelFactory):
    FACTORY_FOR = InfantFu
    
    