import factory
from edc.base.model.tests.factories import BaseUuidModelFactory
from edc.subject.haart.tests.factories import BaseHaartModificationFactory
from apps.mpepu_infant.models import InfantArvProphMod
from infant_arv_proph_factory import InfantArvProphFactory


class InfantArvProphModFactory(BaseHaartModificationFactory):
    FACTORY_FOR = InfantArvProphMod

    infant_arv_proph = factory.SubFactory(InfantArvProphFactory)
