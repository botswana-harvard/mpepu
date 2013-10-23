from edc.dashboard.search.classes import BaseSearchByWord #, site_search
from .models import MaternalConsent


class MaternalSearchByWord(BaseSearchByWord):
    name = 'word'
    search_model = MaternalConsent
    order_by = '-created'
    template = 'maternalconsent_include.html'

    def contribute_to_context(self, context):
        context = super(BaseSearchByWord, self).contribute_to_context(context)
        # FIXME: this should not be hard coded, get it from the section class somehow.
        context.update({
            'subject_dashboard_url': 'subject_dashboard_url'})
        return context

#     section = SectionMaternalView
#     search_model = MaternalConsent
#     order_by = '-created'
#     template = 'maternalconsent_include.html'
# 
# site_search.register(MaternalSearchByWord)
