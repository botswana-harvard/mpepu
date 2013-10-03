from django.contrib import admin
from edc.subject.registration.models import RegisteredSubject
from ..models import InfantRandoDeferral, InfantBirth
from ..classes import RegisteredSubjectModelAdmin
from ..forms import InfantRandoDeferralForm


class InfantRandoDeferralAdmin(RegisteredSubjectModelAdmin):
    form = InfantRandoDeferralForm
    date_hierarchy = 'created'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_birth":
            if request.GET.get('subject_identifier'):
                registered_subject = RegisteredSubject.objects.get(subject_identifier=request.GET.get('subject_identifier'))
                kwargs["queryset"] = InfantBirth.objects.filter(registered_subject=registered_subject)
            else:
                kwargs["queryset"] = InfantBirth.objects.none()

        return super(InfantRandoDeferralAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(InfantRandoDeferral, InfantRandoDeferralAdmin)
