from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter


class FeedingChoiceListFilter(SimpleListFilter):
    title = _('Feeding Choice')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'feeding_choice'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('BF', _('BF')),
            ('FF', _('FF')),
            ('(None)', _('(None)')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        from ..mpepu_infant_rando.models import InfantRando
        if self.used_parameters.get('feeding_choice', None):
            if self.value == '(None)':
                subject_identifiers = InfantRando.objects.exclude(feeding_choice__in=['BF', 'FF']).values('subject_identifier')
            else:
                subject_identifiers = InfantRando.objects.filter(feeding_choice=self.value()).values('subject_identifier')
            queryset = queryset.filter(registered_subject__subject_identifier__in=subject_identifiers)
        return queryset


class FeedingDurationListFilter(SimpleListFilter):
    title = _('Feeding Duration')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'feeding_duration'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('6months', _('6m')),
            ('12months', _('12m')),
            ('(None)', _('(None)')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        from ..mpepu_infant_rando.models import InfantRando
        if self.used_parameters.get('feeding_duration', None):
            if self.value == '(None)':
                subject_identifiers = InfantRando.objects.exclude(bf_duration__in=['12months', '6months']).values('subject_identifier')
            else:
                subject_identifiers = InfantRando.objects.filter(bf_duration=self.value()).values('subject_identifier')
            queryset = queryset.filter(registered_subject__subject_identifier__in=subject_identifiers)
        return queryset

#v4 added filter to enable users to find out which parents where willing/ unwilling to be randomized
class UnwillingToRandoListFilter(SimpleListFilter):
    title = _('Willingness to Randomize')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'willingness_rando'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
            ('N/A', 'Not applicable'),
            ('(None)', ('(None)')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        from ..mpepu_infant.models import InfantEligibility
        if self.used_parameters.get('willingness_rando', None):
            if self.value == '(None)':
                subject_identifiers = InfantEligibility.objects.exclude(rando_bf_duration__in=['Yes', 'No', 'N/A']).values('subject_identifier')
            else:
                subject_identifiers = InfantEligibility.objects.filter(rando_bf_duration=self.value()).values('subject_identifier')
            queryset = queryset.filter(registered_subject__subject_identifier__in=subject_identifiers)
        return queryset
