from django.contrib import admin
from collections import OrderedDict

from edc.export.actions import export_as_csv_action
from edc.base.modeladmin.admin import BaseModelAdmin, BaseTabularInline
from edc.subject.registration.models import RegisteredSubject

from ..models import (InfantHaart, InfantOffDrug, InfantOffStudy, InfantPrerandoLoss, InfantSurvival, InfantNvpAdherence,
                      InfantArvProphMod, InfantArvProph, InfantStudyDrugInit, InfantDeath, InfantFu, InfantFuPhysical,
                      InfantFuDxItems, InfantFuDx, InfantFuDx2ProphItems, InfantFuDx2Proph, InfantFuD, InfantFuMed,
                      InfantFuNewMedItems, InfantFuNewMed, InfantStudyDrugItems, InfantStudyDrug, InfantCtxPlaceboAdh,
                      InfantFeeding, InfantVisit)
from ..forms import (InfantHaartForm, InfantOffDrugForm, InfantOffStudyForm, InfantPrerandoLossForm, InfantSurvivalForm,
                     InfantNvpAdherenceForm, InfantArvProphModForm, InfantArvProphForm, InfantStudyDrugInitForm,
                     InfantDeathForm, InfantFuForm, InfantFuPhysicalForm, InfantFuDxItemsForm, InfantFuDxForm,
                     InfantFuDx2ProphItemsForm, InfantFuDx2ProphForm, InfantFuDForm, InfantFuMedForm, InfantFuNewMedItemsForm,
                     InfantFuNewMedForm, InfantStudyDrugItemsForm, InfantStudyDrugForm, InfantCtxPlaceboAdhForm,
                     InfantFeedingForm)
from .infant_visit_model_admin import InfantVisitModelAdmin
from .registered_subject_model_admin import RegisteredSubjectModelAdmin
from .my_infant_fu_model_admin import MyInfantFuModelAdmin
from .my_infant_arv_proph_model_admin import MyInfantArvProphModelAdmin
from .off_study_model_admin import OffStudyModelAdmin


class InfantHaartAdmin(RegisteredSubjectModelAdmin):

    form = InfantHaartForm

    fields = (
        "registered_subject",
        "hiv_positive_date",
        "haart_initiated",
        "haart_date",
        "arv_status",
        "comment"
    )

    radio_fields = {
        "haart_initiated": admin.VERTICAL,
        "arv_status": admin.VERTICAL
    }

admin.site.register(InfantHaart, InfantHaartAdmin)


class InfantOffDrugAdmin(RegisteredSubjectModelAdmin):

    form = InfantOffDrugForm

    fields = (
        "registered_subject",
        "infant_visit",
        "report_datetime",
        "last_dose_date",
        "reason_off",
        "reason_off_other"
    )
    radio_fields = {
        "reason_off": admin.VERTICAL
    }

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_visit":
            if request.GET.get('infant_visit'):
                kwargs["queryset"] = InfantVisit.objects.filter(id=request.GET.get('infant_visit'))

        return super(InfantOffDrugAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(InfantOffDrug, InfantOffDrugAdmin)


class InfantOffStudyAdmin(OffStudyModelAdmin):

    form = InfantOffStudyForm
    fields = (
        "registered_subject",
        "infant_visit",
        "report_datetime",
        "offstudy_date",
        "reason",
        "reason_other",
        "has_scheduled_data",
        "comment",
    )
    radio_fields = {
        "has_scheduled_data": admin.VERTICAL}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_visit":
            if request.GET.get('infant_visit'):
                kwargs["queryset"] = InfantVisit.objects.filter(id=request.GET.get('infant_visit'))

        return super(InfantOffStudyAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    actions = [export_as_csv_action(description="CSV Export of Off Study",
        fields=[],
        delimiter=',',
        exclude=['created', 'modified', 'user_created', 'user_modified', 'revision', 'id', 'hostname_created', 'hostname_modified' ],
        extra_fields=OrderedDict(
            {'subject_identifier': 'registered_subject__subject_identifier',
             'gender': 'registered_subject__gender',
             'dob': 'registered_subject__dob',
             'registered': 'registered_subject__registration_datetime'}),
        )]
admin.site.register(InfantOffStudy, InfantOffStudyAdmin)


class InfantPrerandoLossAdmin(RegisteredSubjectModelAdmin):

    form = InfantPrerandoLossForm
    fields = (
        "registered_subject",
        "infant_visit",
        "reason_loss",
        "loss_code",
        "reason_loss_other",
        "comment"
    )
    radio_fields = {
        "loss_code": admin.VERTICAL
    }

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_visit":
            if request.GET.get('infant_visit'):
                kwargs["queryset"] = InfantVisit.objects.filter(id=request.GET.get('infant_visit'))

        return super(InfantPrerandoLossAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(InfantPrerandoLoss, InfantPrerandoLossAdmin)


class InfantSurvivalAdmin(RegisteredSubjectModelAdmin):

    form = InfantSurvivalForm
    fields = (
        "registered_subject",
        "infant_visit",
        "infant_survival_status",
        "info_provider",
        "info_provider_other",
        "comment"
    )
    radio_fields = {
        "infant_survival_status": admin.VERTICAL,
        "info_provider": admin.VERTICAL
    }

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_visit":
            if request.GET.get('infant_visit'):
                kwargs["queryset"] = InfantVisit.objects.filter(id=request.GET.get('infant_visit'))

        return super(InfantSurvivalAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(InfantSurvival, InfantSurvivalAdmin)


class InfantNvpAdherenceAdmin(MyInfantArvProphModelAdmin):

    form = InfantNvpAdherenceForm
    fields = (
        "infant_visit",
        "infant_arv_proph",
        "days_missed",
        "reason_missed",
        "reason_missed_other"
    )
    radio_fields = {
        "reason_missed": admin.VERTICAL
    }
admin.site.register(InfantNvpAdherence, InfantNvpAdherenceAdmin)


class InfantArvProphModInlineAdmin(BaseTabularInline):
    model = InfantArvProphMod
    form = InfantArvProphModForm
    extra = 1


class InfantArvProphAdmin(InfantVisitModelAdmin):

    form = InfantArvProphForm
    fields = (
        "infant_visit",
        "prophylatic_nvp",
        "arv_status"
    )
    radio_fields = {
        "arv_status": admin.VERTICAL,
        "prophylatic_nvp": admin.VERTICAL,
    }
    inlines = [InfantArvProphModInlineAdmin, ]
admin.site.register(InfantArvProph, InfantArvProphAdmin)


class InfantArvProphModAdmin(BaseModelAdmin):

    form = InfantArvProphModForm
    fields = (
        "arv_code",
        "dose_status",
        "modification_date",
        "modification_code",
    )
admin.site.register(InfantArvProphMod, InfantArvProphModAdmin)


class InfantStudyDrugInitAdmin(InfantVisitModelAdmin):

    form = InfantStudyDrugInitForm
    fields = (
        "infant_visit",
        "initiated",
        "first_dose_date",
        "reason_not_init",
        "reason_not_init_other",
        "reason_not_survive",
    )
    radio_fields = {
        "initiated": admin.VERTICAL,
        "reason_not_init": admin.VERTICAL
    }
admin.site.register(InfantStudyDrugInit, InfantStudyDrugInitAdmin)


class InfantDeathAdmin(RegisteredSubjectModelAdmin):

    def __init__(self, *args, **kwargs):
        super(InfantDeathAdmin, self).__init__(*args, **kwargs)
        self.list_filter.insert(0, 'registered_subject')
        self.list_display = ('registered_subject', 'created', 'modified', 'user_created', 'user_modified')
        self.date_hierarchy = 'death_date'
    form = InfantDeathForm

    fields = (
        "registered_subject",
        "infant_visit",
        "death_date",
        "death_cause_info",
        "death_cause_info_other",
        "perform_autopsy",
        "death_cause",
        "death_cause_category",
        "death_cause_other",
        "dx_code",
        "illness_duration",
        "death_medical_responsibility",
        "participant_hospitalized",
        "death_reason_hospitalized",
        "death_reason_hospitalized_other",
        "days_hospitalized",
        "study_drug_relate",
        "infant_nvp_relate",
        "haart_relate",
        "trad_med_relate",
        "comment",
    )
    radio_fields = {
        "death_reason_hospitalized": admin.VERTICAL,
        "death_medical_responsibility": admin.VERTICAL,
        "death_cause_info": admin.VERTICAL,
        "death_cause_category": admin.VERTICAL,
        "perform_autopsy": admin.VERTICAL,
        "participant_hospitalized": admin.VERTICAL,
        "study_drug_relate": admin.VERTICAL,
        "infant_nvp_relate": admin.VERTICAL,
        "haart_relate": admin.VERTICAL,
        "trad_med_relate": admin.VERTICAL
    }

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_visit":
            if request.GET.get('infant_visit'):
                kwargs["queryset"] = InfantVisit.objects.filter(id=request.GET.get('infant_visit'))

        return super(InfantDeathAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(InfantDeath, InfantDeathAdmin)


class InfantFuAdmin(InfantVisitModelAdmin):

    def __init__(self, *args):
        super(InfantFuAdmin, self).__init__(*args)

    form = InfantFuForm
    fields = (
        "infant_visit",
        "physical_assessment",
        "diarrhea_illness",
        "has_dx",
    )
    radio_fields = {
        "physical_assessment": admin.VERTICAL,
        "diarrhea_illness": admin.VERTICAL,
        "has_dx": admin.VERTICAL,
    }
admin.site.register(InfantFu, InfantFuAdmin)


class InfantFuPhysicalAdmin(MyInfantFuModelAdmin):

    form = InfantFuPhysicalForm
    fields = (
        "infant_visit",
        "infant_fu",
        "weight",
        "height",
        "head_circumference",
        "has_abnormalities",
        "abnormalities",
        "was_hospitalized",
        "days_hospitalized",
    )
    radio_fields = {
        "has_abnormalities": admin.VERTICAL,
        "was_hospitalized": admin.VERTICAL,
    }
admin.site.register(InfantFuPhysical, InfantFuPhysicalAdmin)


class InfantFuDxItemsInlineAdmin(BaseTabularInline):

    model = InfantFuDxItems
    form = InfantFuDxItemsForm
    extra = 1


class InfantFuDxAdmin(MyInfantFuModelAdmin):

    form = InfantFuDxForm

    inlines = [InfantFuDxItemsInlineAdmin, ]

admin.site.register(InfantFuDx, InfantFuDxAdmin)


class InfantFuDxItemsAdmin(BaseModelAdmin):
    form = InfantFuDxItemsForm
admin.site.register(InfantFuDxItems, InfantFuDxItemsAdmin)


class InfantFuDx2ProphItemsInlineAdmin(BaseTabularInline):
    model = InfantFuDx2ProphItems
    form = InfantFuDx2ProphItemsForm
    extra = 1


class InfantFuDx2ProphAdmin(MyInfantFuModelAdmin):

    form = InfantFuDx2ProphForm
    fields = (
        "infant_visit",
        "infant_fu",
        "who_diagnosis",
        "wcs_dx_ped",
        "has_dx")
    radio_fields = {
        "has_dx": admin.VERTICAL,
        "who_diagnosis": admin.VERTICAL}
    filter_horizontal = ("wcs_dx_ped", )
    inlines = [InfantFuDx2ProphItemsInlineAdmin, ]
    """registeredsubject"""

admin.site.register(InfantFuDx2Proph, InfantFuDx2ProphAdmin)


class InfantFuDx2ProphItemsAdmin(BaseModelAdmin):
    form = InfantFuDx2ProphItemsForm

admin.site.register(InfantFuDx2ProphItems, InfantFuDx2ProphItemsAdmin)


class InfantFuDAdmin(MyInfantFuModelAdmin):
    form = InfantFuDForm
    radio_fields = {
        "health_facility": admin.VERTICAL,
        "hospitalized": admin.VERTICAL,
        "bloody_diarrhea": admin.VERTICAL,
        "fever_present": admin.VERTICAL}
admin.site.register(InfantFuD, InfantFuDAdmin)


class InfantFuMedAdmin(MyInfantFuModelAdmin):
    form = InfantFuMedForm
    fields = (
        "infant_visit",
        "infant_fu",
        "vaccines_received",
        "vaccination",
        "comments")
    radio_fields = {"vaccines_received": admin.VERTICAL}
    filter_horizontal = ("vaccination", )
admin.site.register(InfantFuMed, InfantFuMedAdmin)


class InfantFuNewMedItemsInlineAdmin(BaseTabularInline):
    model = InfantFuNewMedItems
    form = InfantFuNewMedItemsForm
    extra = 1


class InfantFuNewMedAdmin(MyInfantFuModelAdmin):
    form = InfantFuNewMedForm
    fields = (
        "infant_visit",
        "infant_fu",
        "new_medications",
        "other_medications")
    radio_fields = {"new_medications": admin.VERTICAL}
    inlines = [InfantFuNewMedItemsInlineAdmin, ]
admin.site.register(InfantFuNewMed, InfantFuNewMedAdmin)


class InfantFuNewMedItemsAdmin(BaseModelAdmin):
    form = InfantFuNewMedItemsForm

admin.site.register(InfantFuNewMedItems, InfantFuNewMedItemsAdmin)


class InfantStudyDrugItemsAdmin(BaseModelAdmin):
    form = InfantStudyDrugItemsForm
    list_display = ('inf_study_drug', 'dose_status', 'ingestion_date', 'modification_reason', 'modified')
    search_fields = ('inf_study_drug__infant_visit__appointment__registered_subject__subject_identifier', 'dose_status', 'modification_reason',)

admin.site.register(InfantStudyDrugItems, InfantStudyDrugItemsAdmin)


class InfantStudyDrugItemsInlineAdmin(BaseTabularInline):
    model = InfantStudyDrugItems
    form = InfantStudyDrugItemsForm
    extra = 1


class InfantStudyDrugAdmin(InfantVisitModelAdmin):

    form = InfantStudyDrugForm
    fields = (
       "infant_visit",
       "on_placebo_status",
       "drug_status")
    radio_fields = {
       "drug_status": admin.VERTICAL,
       "on_placebo_status": admin.VERTICAL}
    inlines = [InfantStudyDrugItemsInlineAdmin, ]
admin.site.register(InfantStudyDrug, InfantStudyDrugAdmin)


class InfantCtxPlaceboAdhAdmin(InfantVisitModelAdmin):
    form = InfantCtxPlaceboAdhForm
    fields = (
       "infant_visit",
       "day_missed_drug",
       "reason_missed",
       "reason_missed_other")
    radio_fields = {"reason_missed": admin.VERTICAL}
admin.site.register(InfantCtxPlaceboAdh, InfantCtxPlaceboAdhAdmin)


class InfantFeedingAdmin(InfantVisitModelAdmin):

    form = InfantFeedingForm
    fields = (
        "infant_visit",
        "last_att_sche_visit",
        "other_feeding",
        "formula_intro_occur",
        "formula_date",
        "formula",
        "water",
        "juice",
        "cow_milk",
        "cow_milk_yes",
        "other_milk",
        "other_milk_animal",
        "milk_boiled",
        "fruits_veg",
        "cereal_porridge",
        "solid_liquid",
        "rehydration_salts",
        "water_used",
        "water_used_other",
        "reason_rcv_formula",
        "reason_rcv_fm_other",
        "ever_breastfeed",
        "complete_weaning",
        "weaned_completely",
        "most_recent_bm",
        "times_breastfed",
        "comments")
    radio_fields = {
        "other_feeding": admin.VERTICAL,
        "formula_intro_occur": admin.VERTICAL,
        "reason_rcv_formula": admin.VERTICAL,
        "water_used": admin.VERTICAL,
        "formula": admin.VERTICAL,
        "water": admin.VERTICAL,
        "juice": admin.VERTICAL,
        "cow_milk": admin.VERTICAL,
        "cow_milk_yes": admin.VERTICAL,
        "other_milk": admin.VERTICAL,
        "milk_boiled": admin.VERTICAL,
        "fruits_veg": admin.VERTICAL,
        "cereal_porridge": admin.VERTICAL,
        "solid_liquid": admin.VERTICAL,
        "rehydration_salts": admin.VERTICAL,
        "ever_breastfeed": admin.VERTICAL,
        "complete_weaning": admin.VERTICAL,
        "weaned_completely": admin.VERTICAL,
        "times_breastfed": admin.VERTICAL}

admin.site.register(InfantFeeding, InfantFeedingAdmin)
