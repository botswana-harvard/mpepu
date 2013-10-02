from django.contrib import admin
from bhp_registration.models import RegisteredSubject
from mpepu_infant.classes import RegisteredSubjectModelAdmin
from mpepu_infant.models import InfantPreEligibility, InfantBirth
from mpepu_infant.forms import InfantPreEligibilityForm


class InfantPreEligibilityAdmin(RegisteredSubjectModelAdmin):
    """Confirms infant pre eligibility."""
    form = InfantPreEligibilityForm

    def __init__(self, *args, **kwargs):
        super(InfantPreEligibilityAdmin, self).__init__(*args, **kwargs)
        self.list_display = ('registered_subject', 'infant_birth', 'weight', 'clinical_jaundice', 'anemia_neutropenia')

    def save_model(self, request, obj, form, change):
        return super(InfantPreEligibilityAdmin, self).save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_birth":
            if request.GET.get('subject_identifier'):
                registered_subject = RegisteredSubject.objects.get(subject_identifier=request.GET.get('subject_identifier'))
                kwargs["queryset"] = InfantBirth.objects.filter(registered_subject=registered_subject)
            else:
                kwargs["queryset"] = InfantBirth.objects.none()

        return super(InfantPreEligibilityAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

#     def get_readonly_fields(self, request, obj=None):
#         if obj:  # In edit mode
#             return ('infant_birth', ) + self.readonly_fields
#         else:
#             return self.readonly_fields

    date_hierarchy = 'created'
    fields = (
        "registered_subject",
        "infant_birth",
        "weight",
        "clinical_jaundice",
        "anemia_neutropenia",
    )

    radio_fields = {
        "clinical_jaundice": admin.VERTICAL,
        "anemia_neutropenia": admin.VERTICAL,
    }

admin.site.register(InfantPreEligibility, InfantPreEligibilityAdmin)
