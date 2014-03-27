import factory
from apps.mpepu_maternal.models import ResistanceEligibility
from .maternal_visit_factory import MaternalVisitFactory


class ResistanceEligibilityFactory(factory.Factory):
    FACTORY_FOR = ResistanceEligibility

    maternal_visit = factory.SubFactory(MaternalVisitFactory)
    stopped_arv = 'No'
    incarcerated = 'No'
