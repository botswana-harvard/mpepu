from django.db.models import Q

from edc.dashboard.search.classes import BaseSearchByWord #, site_search

from .models import InfantBirth


class InfantSearchByWord(BaseSearchByWord):
    name = 'word'
    search_model = InfantBirth
#     order_by = '-created'
    template = 'infantbirth_include.html'

    @property
    def qset(self):
        #qset = self.qset_for_consent
        qset = (Q(registered_subject__subject_identifier__icontains=self.search_value) |
               Q(registered_subject__first_name__icontains=self.search_value))
        return qset

#     def contribute_to_context(self, context):
#         context = super(BaseSearchByWord, self).contribute_to_context(context)
#         # FIXME: this should not be hard coded, get it from the section class somehow.
#         context.update({
#             'subject_dashboard_url': 'subject_dashboard_url'})
#         return context

#     section = SectionInfantView
#     search_model = InfantBirth
#     order_by = '-created'
#     template = 'infantbirth_include.html'
# 
# site_search.register(InfantSearchByWord)
