import factory
from edc.base.model.tests.factories import BaseUuidModelFactory
from apps.mpepu_infant.tests.factories import InfantVisitFactory
from apps.mpepu_infant.models import InfantArvProph
from edc.subject.haart.choices import ARV_STATUS_WITH_NEVER


class InfantArvProphFactory(BaseUuidModelFactory):
    FACTORY_FOR = InfantArvProph

    infant_visit = factory.SubFactory(InfantVisitFactory)
    prophylatic_nvp = 'Yes'
    arv_status = ARV_STATUS_WITH_NEVER[0][0]
