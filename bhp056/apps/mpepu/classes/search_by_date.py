from bhp_search.classes import BaseSearchByDate
from ..models import MaternalConsent
from mpepu_infant.models import InfantBirth


class SearchByDate(BaseSearchByDate):

    def __init__(self, **kwargs):

        super(SearchByDate, self).__init__(**kwargs)
        self.search_model.update({
              'maternalconsent': MaternalConsent,
              'infantbirth': InfantBirth})
