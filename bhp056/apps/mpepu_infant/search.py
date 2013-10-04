from edc.dashboard.search.classes import BaseSearchByWord, site_search
from .models import InfantBirth
from .section import SectionInfantView


class InfantSearchByWord(BaseSearchByWord):

    section = SectionInfantView
    search_model = InfantBirth
    order_by = '-created'
    template = 'infantbirth_include.html'

site_search.register(InfantSearchByWord)
