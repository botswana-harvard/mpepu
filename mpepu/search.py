from bhp_search.classes import BaseSearchByWord, search


class SearchByWord(BaseSearchByWord):

    def get_search_models_prep(self):

        return {'maternal': ('mpepu_maternal', 'maternalconsent'),
                'infant': ('mpepu_infant', 'infantbirth')}

search.register(SearchByWord)
