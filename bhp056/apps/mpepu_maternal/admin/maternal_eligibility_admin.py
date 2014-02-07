from django.contrib import admin

from edc.subject.registration.models import RegisteredSubject

from ..admin import RegisteredSubjectModelAdmin
from ..models import MaternalConsent, MaternalEligibilityAnte, MaternalEligibilityPost
from ..forms import MaternalEligibilityAnteForm, MaternalEligibilityPostForm


class MaternalEligibilityAnteAdmin(RegisteredSubjectModelAdmin):

    form = MaternalEligibilityAnteForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "maternal_consent":
            if request.GET.get('registered_subject'):
                maternal_subject_identifier = RegisteredSubject.objects.get(id=request.GET.get('registered_subject')).subject_identifier
                kwargs["queryset"] = MaternalConsent.objects.filter(subject_identifier=maternal_subject_identifier)

        return super(MaternalEligibilityAnteAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('maternal_consent',)
    fields = (
        'registered_subject',
        'maternal_consent',
        'registration_datetime',
        'gestational_age',
        'is_hiv_positive',
        'agree_follow_up',
        'is_cd4_low',
        'feeding_choice',
        'maternal_haart')
    radio_fields = {
        "is_hiv_positive": admin.VERTICAL,
        "agree_follow_up": admin.VERTICAL,
        "feeding_choice": admin.VERTICAL,
        "maternal_haart": admin.VERTICAL}

admin.site.register(MaternalEligibilityAnte, MaternalEligibilityAnteAdmin)


class MaternalEligibilityPostAdmin(RegisteredSubjectModelAdmin):

    form = MaternalEligibilityPostForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "maternal_consent":
            if request.GET.get('registered_subject'):
                maternal_subject_identifier = RegisteredSubject.objects.get(id=request.GET.get('registered_subject')).subject_identifier
                kwargs["queryset"] = MaternalConsent.objects.filter(subject_identifier=maternal_subject_identifier)

        return super(MaternalEligibilityPostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('maternal_consent', )
    fields = (
        'registered_subject',
        'maternal_consent',
        'registration_datetime',
        'days_pnc',
        'is_hiv_positive',
        'agree_follow_up',
        'is_cd4_low',
        'feeding_choice',
        'maternal_haart')

    radio_fields = {
        "is_hiv_positive": admin.VERTICAL,
        "agree_follow_up": admin.VERTICAL,
        "feeding_choice": admin.VERTICAL,
        "maternal_haart": admin.VERTICAL}


admin.site.register(MaternalEligibilityPost, MaternalEligibilityPostAdmin)
