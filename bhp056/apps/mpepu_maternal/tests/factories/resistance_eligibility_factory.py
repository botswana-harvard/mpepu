import factory
from apps.mpepu_maternal.models import ResistanceEligibility


class ResistanceEligibilityFactory(factory.Factory):
    FACTORY_FOR = ResistanceEligibility
    stopped_arv = 'No'
    incarcerated = 'No'
