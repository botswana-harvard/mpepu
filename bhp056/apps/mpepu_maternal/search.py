from edc.dashboard.search.classes import BaseSearchByWord, site_search
from .models import MaternalConsent
from .section import SectionMaternalView


class MaternalSearchByWord(BaseSearchByWord):

    section = SectionMaternalView
    search_model = MaternalConsent
    order_by = '-created'
    template = 'maternalconsent_include.html'

site_search.register(MaternalSearchByWord)
