from bhp_search.classes import BaseSearchByWord


class SearchByWord(BaseSearchByWord):

    def get_search_prep_models(self):

        return {'maternalconsent': ('mpepu_maternal', 'maternalconsent'),
                'infantbirth': ('mpepu_infant', 'infantbirth')}
