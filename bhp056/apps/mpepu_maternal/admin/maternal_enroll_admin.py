from django.contrib import admin

from edc.base.admin.admin import BaseTabularInline, BaseModelAdmin

from ..models import (MaternalEnroll, MaternalEnrollDem, MaternalEnrollOb, MaternalEnrollDx, MaternalEnrollMed,
                                   MaternalEnrollArv, MaternalEnrollClin)
from ..forms import (MaternalEnrollForm, MaternalEnrollDemForm, MaternalEnrollClinForm, MaternalEnrollObForm,
                                  MaternalEnrollMedForm, MaternalEnrollDxForm, MaternalEnrollArvForm)
from .maternal_visit_model_admin import MaternalVisitModelAdmin


class BaseMaternalEnrollAdmin(MaternalVisitModelAdmin):
    """ For other sections of MaternalEnroll; that is, related to MaternalEnroll model. """
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "maternal_enroll":
            kwargs["queryset"] = MaternalEnroll.objects.filter(maternal_visit__exact=request.GET.get('maternal_visit', 0))
        return super(BaseMaternalEnrollAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('maternal_enroll',) + self.readonly_fields
        else:
            return self.readonly_fields


class MaternalEnrollAdmin(MaternalVisitModelAdmin):

    form = MaternalEnrollForm
    fields = (
        "maternal_visit",
        "recruit_source",
        "recruit_source_other",
        "prev_pregnancies",
        "prior_health_haart",
        "prev_pregnancy_arv",
        "weight",
        "height")
    radio_fields = {
        "recruit_source": admin.VERTICAL,
        "prior_health_haart": admin.VERTICAL,
        "prev_pregnancy_arv": admin.VERTICAL}
admin.site.register(MaternalEnroll, MaternalEnrollAdmin)


class MaternalEnrollDemAdmin(BaseMaternalEnrollAdmin):
    form = MaternalEnrollDemForm
    fields = (
        "maternal_visit",
        "maternal_enroll",
        "marital_status",
        "marital_status_other",
        "ethnicity",
        "ethnicity_other",
        "highest_education",
        "current_occupation",
        "current_occupation_other",
        "provides_money",
        "provides_money_other",
        "money_earned",
        "money_earned_other",
        "own_phone",
        "water_source",
        "house_electrified",
        "house_fridge",
        "cooking_method",
        "hh_goods",
        "toilet_facility",
        "toilet_facility_other",
        "house_people_number",
        "house_type",
        "know_hiv_status")
    radio_fields = {
        "marital_status": admin.VERTICAL,
        "ethnicity": admin.VERTICAL,
        "highest_education": admin.VERTICAL,
        "current_occupation": admin.VERTICAL,
        "provides_money": admin.VERTICAL,
        "money_earned": admin.VERTICAL,
        "own_phone": admin.VERTICAL,
        "water_source": admin.VERTICAL,
        "house_electrified": admin.VERTICAL,
        "house_fridge": admin.VERTICAL,
        "cooking_method": admin.VERTICAL,
        "toilet_facility": admin.VERTICAL,
        "house_type": admin.VERTICAL,
        "know_hiv_status": admin.VERTICAL}
    filter_horizontal = ("hh_goods",)
admin.site.register(MaternalEnrollDem, MaternalEnrollDemAdmin)


class MaternalEnrollObAdmin(BaseMaternalEnrollAdmin):
    form = MaternalEnrollObForm
    fields = (
        "maternal_visit",
        "maternal_enroll",
        "pregs_24wks_or_more",
        "lost_before_24wks",
        "lost_after_24wks",
        "live_children",
        "children_died_b4_5yrs")
admin.site.register(MaternalEnrollOb, MaternalEnrollObAdmin)


class MaternalEnrollDxInlineAdmin(BaseTabularInline):

    model = MaternalEnrollDx


class MaternalEnrollMedAdmin(BaseMaternalEnrollAdmin):

    form = MaternalEnrollMedForm
    fields = (
        "maternal_visit",
        "maternal_enroll",
        "has_chronic_cond",
        "chronic_cond",
        "chronic_cond_other",
        "who_diagnosis")
    radio_fields = {
        "has_chronic_cond": admin.VERTICAL,
        "who_diagnosis": admin.VERTICAL}
    filter_horizontal = ("chronic_cond",)
    inlines = [MaternalEnrollDxInlineAdmin, ]
admin.site.register(MaternalEnrollMed, MaternalEnrollMedAdmin)


class MaternalEnrollDxAdmin(BaseModelAdmin):

    form = MaternalEnrollDxForm
    fields = (
        "maternal_enroll_med",
        "diagnosis",
        "diagnosis_year")
admin.site.register(MaternalEnrollDx, MaternalEnrollDxAdmin)


class MaternalEnrollArvAdmin(BaseMaternalEnrollAdmin):

    form = MaternalEnrollArvForm
    fields = (
        "maternal_visit",
        "maternal_enroll",
        "haart_start_date",
        "is_date_estimated",
        "preg_on_haart",
        "haart_changes",
        "prior_preg",
        "prior_arv",
        "prior_arv_other")
    radio_fields = {
        "preg_on_haart": admin.VERTICAL,
        "prior_preg": admin.VERTICAL,
        "is_date_estimated": admin.VERTICAL}
    filter_horizontal = ("prior_arv", )
admin.site.register(MaternalEnrollArv, MaternalEnrollArvAdmin)


class MaternalEnrollClinAdmin(BaseMaternalEnrollAdmin):

    form = MaternalEnrollClinForm
    fields = (
        "maternal_visit",
        "maternal_enroll",
        "prev_preg_azt",
        "prev_sdnvp_labour",
        "prev_preg_haart",
        "cd4_count",
        "cd4_date",
        "is_date_estimated",
        "comment",)
    radio_fields = {
        "prev_preg_azt": admin.VERTICAL,
        "prev_sdnvp_labour": admin.VERTICAL,
        "prev_preg_haart": admin.VERTICAL,
        "is_date_estimated": admin.VERTICAL}
admin.site.register(MaternalEnrollClin, MaternalEnrollClinAdmin)
