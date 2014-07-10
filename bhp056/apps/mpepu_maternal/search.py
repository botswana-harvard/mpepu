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
# 
#     def get_search_result(self, request, **kwargs):
#         """Returns a queryset using the search term as a filter."""
#         from edc.subject.consent.models import BaseConsent
#         from django.db.models import Q
#         model = self.get_search_model_cls()
#         search_form = self.get_search_form(self.get_search_form_data())
#         if search_form.is_valid():
#             qset_filter = Q()
#             qset_exclude = Q()
#             self.set_search_term(search_form.cleaned_data.get('search_term'))
#             if self.get_qset_by_filter_keyword():
#                 qset_filter, qset_exclude = self.get_qset_by_filter_keyword()
#             elif self.get_qset_by_search_term_pattern():
#                 qset_filter, qset_exclude = self.get_qset_by_search_term_pattern()
# #             elif 'registered_subject' in dir(model()):
# #                 qset_filter = self.get_qset_for_registered_subject()
#             elif issubclass(model, BaseConsent):
#                 qset_filter = self.get_qset_for_consent()
#             else:
#                 qset_filter = self.get_qset_for_generic_model()
#             search_result = model.objects.filter(qset_filter).exclude(qset_exclude).order_by('-modified', '-created')
#         return search_result
#     

#     section = SectionMaternalView
#     search_model = MaternalConsent
#     order_by = '-created'
#     template = 'maternalconsent_include.html'
# 
# site_search.register(MaternalSearchByWord)
