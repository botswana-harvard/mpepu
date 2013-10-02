from bhp_search.classes import BaseSearchByWeek
from ..models import MaternalConsent
from mpepu_infant.models import InfantBirth


class SearchByWeek(BaseSearchByWeek):

    def __init__(self, **kwargs):

        super(SearchByWeek, self).__init__(**kwargs)
        self.search_model.update({
              'maternalconsent': MaternalConsent,
              'infantbirth': InfantBirth})
