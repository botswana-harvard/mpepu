from django import forms
from django.contrib import admin

from edc.subject.registration.models import RegisteredSubject

from apps.mpepu_infant_rando.models import InfantRando
from apps.mpepu_maternal.models import MaternalLabDel

from ..models import InfantEligibility, InfantBirth
from ..forms import InfantEligibilityForm
from ..filters import FeedingChoiceListFilter, FeedingDurationListFilter, UnwillingToRandoListFilter
from .registered_subject_model_admin import RegisteredSubjectModelAdmin


class InfantEligibilityAdmin(RegisteredSubjectModelAdmin):
    """Confirms infant eligibility and handles infant randomization."""
    form = InfantEligibilityForm

    list_filter = (UnwillingToRandoListFilter, FeedingChoiceListFilter, FeedingDurationListFilter, 'created', 'modified', 'user_created', 'user_modified')
    list_display = ('registered_subject', 'infant_birth', 'randomization_site', 'feeding', 'duration', 'created', 'modified', 'user_created', 'user_modified')

    def save_model(self, request, obj, form, change):
        """Saves and randomizes."""
        if not change:
            # if no record in InfantRando "claimed" by this infant, run the randomization
            if not InfantRando.objects.filter(subject_identifier=obj.registered_subject.subject_identifier):
                infant_rando = InfantRando.objects.randomize(infant_eligibility=obj)
                if not infant_rando:
                    raise forms.ValidationError('Randomization failed. Unable to fetch record from infant_rando list with given criteria.')
        return super(InfantEligibilityAdmin, self).save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_birth":
            if request.GET.get('registered_subject'):
#                 registered_subject = RegisteredSubject.objects.get(subject_identifier=request.GET.get('subject_identifier'))
                kwargs["queryset"] = InfantBirth.objects.filter(registered_subject=request.GET.get('registered_subject'))
            else:
                kwargs["queryset"] = InfantBirth.objects.none()

        return super(InfantEligibilityAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    #override to disallow subject to be changed
    def get_readonly_fields(self, request, obj=None):
        if obj:  # In edit mode
            return ('infant_birth', 'hiv_status', 'ctx_contra', 'congen_anomaly', 'arv_72hrs', 'feeding_method',) + self.readonly_fields
        else:
            return self.readonly_fields

    date_hierarchy = 'created'
    fields = (
        "registered_subject",
        "infant_birth",
        "weight",
        "clinical_jaundice",
        "anemia_neutropenia",
        "hiv_status",
        "hiv_result_reference",
        "ctx_contra",
        "congen_anomaly",
        "maternal_art_status",
        "maternal_feeding_choice",
        "rando_bf_duration",
        "randomization_site"
    )

    radio_fields = {
        "hiv_status": admin.VERTICAL,
        "ctx_contra": admin.VERTICAL,
        "congen_anomaly": admin.VERTICAL,
        "maternal_art_status": admin.VERTICAL,
        "maternal_feeding_choice": admin.VERTICAL,
        "rando_bf_duration": admin.VERTICAL,
        "randomization_site": admin.VERTICAL,
        "clinical_jaundice": admin.VERTICAL,
        "anemia_neutropenia": admin.VERTICAL,
    }
    #v4 added filter to enable users to find out which parents where willing/ unwilling to be randomized
    #list_filter = ('rando_bf_duration',)

admin.site.register(InfantEligibility, InfantEligibilityAdmin)
