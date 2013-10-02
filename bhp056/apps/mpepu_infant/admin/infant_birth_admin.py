from django.contrib import admin
from edc.subject.registration.models import RegisteredSubject
from mpepu_infant.classes import InfantVisitModelAdmin, RegisteredSubjectModelAdmin
from ..models import MaternalLabDel
from mpepu_infant.models import InfantBirth, InfantBirthArv, InfantBirthData, InfantBirthExam, InfantBirthFeed
from mpepu_infant.forms import InfantBirthForm, InfantBirthArvForm, InfantBirthDataForm, InfantBirthExamForm, InfantBirthFeedForm


class InfantBirthAdmin(RegisteredSubjectModelAdmin):

    form = InfantBirthForm

    def save_model(self, request, obj, form, change):

        # update initials, etc for register_subject record, now that you have them
        registered_subject = obj.registered_subject
        registered_subject.initials = obj.initials
        registered_subject.gender = obj.gender
        registered_subject.dob = obj.dob
        registered_subject.is_dob_estimated = '-'
        registered_subject.save()
        return super(InfantBirthAdmin, self).save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "maternal_lab_del":
            if request.GET.get('subject_identifier'):
                maternal_subject_identifier = RegisteredSubject.objects.get(subject_identifier=request.GET.get('subject_identifier')).relative_identifier
                kwargs["queryset"] = MaternalLabDel.objects.filter(maternal_visit__appointment__registered_subject__subject_identifier=maternal_subject_identifier)
            else:
                kwargs["queryset"] = MaternalLabDel.objects.none()

        return super(InfantBirthAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    fields = (
        "registered_subject",
        "maternal_lab_del",
        "first_name",
        "initials",
        "birth_order",
        "dob",
        "gender"
    )

    list_display = ('registered_subject', 'first_name', 'initials', 'dob', 'gender', 'created', 'modified')

    radio_fields = {
        "gender": admin.VERTICAL
    }

    filter_horizontal = (

    )

    search_fields = ('registered_subject__subject_identifier', 'first_name', 'initials', 'registered_subject__sid',)

    list_filter = ('gender',)

admin.site.register(InfantBirth, InfantBirthAdmin)


class InfantBirthArvAdmin(InfantVisitModelAdmin):

    form = InfantBirthArvForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_birth":
            if request.GET.get('subject_identifier'):
                kwargs["queryset"] = InfantBirth.objects.filter(registered_subject__subject_identifier=request.GET.get('subject_identifier'))
            else:
                kwargs["queryset"] = InfantBirth.objects.none()
        return super(InfantBirthArvAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    fields = (
        "infant_visit",
        "infant_birth",
        "azt_after_birth",
        "azt_dose_date",
        "azt_additional_dose",
        "sdnvp_after_birth",
        "nvp_dose_date",
        "additional_nvp_doses",
        "azt_discharge_supply",
        "nvp_discharge_supply",
        "infant_arv_comments"
    )

    radio_fields = {
        "azt_after_birth": admin.VERTICAL,
        "azt_additional_dose": admin.VERTICAL,
        "sdnvp_after_birth": admin.VERTICAL,
        "additional_nvp_doses": admin.VERTICAL,
        "azt_discharge_supply": admin.VERTICAL,
        "nvp_discharge_supply": admin.VERTICAL
    }

    filter_horizontal = (

    )

admin.site.register(InfantBirthArv, InfantBirthArvAdmin)


class InfantBirthDataAdmin(InfantVisitModelAdmin):

    form = InfantBirthDataForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_birth":
            if request.GET.get('subject_identifier'):
                kwargs["queryset"] = InfantBirth.objects.filter(registered_subject__subject_identifier=request.GET.get('subject_identifier'))
            else:
                kwargs["queryset"] = InfantBirth.objects.none()
        return super(InfantBirthDataAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    fields = (
        "infant_visit",
        "infant_birth",
        "infant_birth_weight",
        "infant_length",
        "head_circumference",
        "apgar_score",
        "apgar_score_min_1",
        "apgar_score_min_5",
        "apgar_score_min_10",
        "congenital_anomalities",
        "other_birth_info"
    )

    radio_fields = {
        "apgar_score": admin.VERTICAL,
        "congenital_anomalities": admin.VERTICAL
    }

    filter_horizontal = (

    )

admin.site.register(InfantBirthData, InfantBirthDataAdmin)


class InfantBirthExamAdmin(InfantVisitModelAdmin):

    form = InfantBirthExamForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_birth":
            if request.GET.get('subject_identifier'):
                kwargs["queryset"] = InfantBirth.objects.filter(registered_subject__subject_identifier=request.GET.get('subject_identifier'))
            else:
                kwargs["queryset"] = InfantBirth.objects.none()
        return super(InfantBirthExamAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    fields = (
        "infant_visit",
        "infant_birth",
        "infant_exam_date",
        "gender",
        "general_activity",
        "abnormal_activity",
        "physical_exam_result",
        "heent_exam",
        "heent_no_other",
        "resp_exam",
        "resp_exam_other",
        "cardiac_exam",
        "cardiac_exam_other",
        "abdominal_exam",
        "abdominal_exam_other",
        "skin_exam",
        "skin_exam_other",
        "macular_papular_rash",
        "neurologic_exam",
        "neuro_exam_other",
        "other_exam_info"
    )

    radio_fields = {
        "gender": admin.VERTICAL,
        "general_activity": admin.VERTICAL,
        "physical_exam_result": admin.VERTICAL,
        "heent_exam": admin.VERTICAL,
        "resp_exam": admin.VERTICAL,
        "cardiac_exam": admin.VERTICAL,
        "abdominal_exam": admin.VERTICAL,
        "skin_exam": admin.VERTICAL,
        "macular_papular_rash": admin.VERTICAL,
        "neurologic_exam": admin.VERTICAL
    }

    filter_horizontal = (

    )

admin.site.register(InfantBirthExam, InfantBirthExamAdmin)


class InfantBirthFeedAdmin(InfantVisitModelAdmin):

    form = InfantBirthFeedForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_birth":
            if request.GET.get('subject_identifier'):
                kwargs["queryset"] = InfantBirth.objects.filter(registered_subject__subject_identifier=request.GET.get('subject_identifier'))
            else:
                kwargs["queryset"] = InfantBirth.objects.none()
        return super(InfantBirthFeedAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    fields = (
        "infant_visit",
        "infant_birth",
        "feeding_after_delivery",
        "vaccination",
        "comments"
    )

    radio_fields = {
        "feeding_after_delivery": admin.VERTICAL,

    }

    filter_horizontal = (
        "vaccination",

    )
admin.site.register(InfantBirthFeed, InfantBirthFeedAdmin)
