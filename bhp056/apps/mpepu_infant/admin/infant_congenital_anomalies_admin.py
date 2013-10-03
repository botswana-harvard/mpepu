from django.contrib import admin
from edc.base.admin.admin import BaseTabularInline
from ..models import (InfantCnsAbnormalityItems, InfantFacialDefectItems, InfantCleftDisorderItems, InfantMouthUpGastrointestinalItems,
                                 InfantCardiovascularDisorderItems, InfantRespiratoryDefectItems, InfantLowerGastrointestinalItems, InfantFemaleGenitalAnomalyItems,
                                 InfantMaleGenitalAnomalyItems, InfantRenalAnomalyItems, InfantMusculoskeletalAbnormalItems,
                                 InfantSkinAbnormalItems, InfantTrisomiesChromosomeItems, InfantOtherAbnormalityItems, InfantCongenitalAnomalies)
from ..forms import InfantCongenitalAnomaliesForm
from .registered_subject_model_admin import RegisteredSubjectModelAdmin


class InfantCnsAbnormalityItemsInlineAdmin(BaseTabularInline):

    model = InfantCnsAbnormalityItems


class InfantFacialDefectItemsInlineAdmin(BaseTabularInline):

    model = InfantFacialDefectItems


class InfantCleftDisorderItemsInlineAdmin(BaseTabularInline):

    model = InfantCleftDisorderItems


class InfantMouthUpGastrointestinalItemsInlineAdmin(BaseTabularInline):

    model = InfantMouthUpGastrointestinalItems


class InfantCardiovascularDisorderItemsInlineAdmin(BaseTabularInline):

    model = InfantCardiovascularDisorderItems


class InfantRespiratoryDefectItemsInlineAdmin(BaseTabularInline):

    model = InfantRespiratoryDefectItems


class InfantLowerGastrointestinalItemsInlineAdmin(BaseTabularInline):

    model = InfantLowerGastrointestinalItems


class InfantFemaleGenitalAnomalyItemsInlineAdmin(BaseTabularInline):

    model = InfantFemaleGenitalAnomalyItems


class InfantMaleGenitalAnomalyItemsInlineAdmin(BaseTabularInline):

    model = InfantMaleGenitalAnomalyItems


class InfantRenalAnomalyItemsInlineAdmin(BaseTabularInline):

    model = InfantRenalAnomalyItems


class InfantMusculoskeletalAbnormalItemsInlineAdmin(BaseTabularInline):

    model = InfantMusculoskeletalAbnormalItems


class InfantSkinAbnormalItemsInlineAdmin(BaseTabularInline):

    model = InfantSkinAbnormalItems


class InfantTrisomiesChromosomeItemsInlineAdmin(BaseTabularInline):

    model = InfantTrisomiesChromosomeItems


class InfantOtherAbnormalityItemsInlineAdmin(BaseTabularInline):

    model = InfantOtherAbnormalityItems


class InfantCongenitalAnomaliesAdmin(RegisteredSubjectModelAdmin):

    form = InfantCongenitalAnomaliesForm
    inlines = [
        InfantCnsAbnormalityItemsInlineAdmin,
        InfantFacialDefectItemsInlineAdmin,
        InfantCleftDisorderItemsInlineAdmin,
        InfantMouthUpGastrointestinalItemsInlineAdmin,
        InfantCardiovascularDisorderItemsInlineAdmin,
        InfantRespiratoryDefectItemsInlineAdmin,
        InfantRespiratoryDefectItemsInlineAdmin,
        InfantLowerGastrointestinalItemsInlineAdmin,
        InfantFemaleGenitalAnomalyItemsInlineAdmin,
        InfantMaleGenitalAnomalyItemsInlineAdmin,
        InfantRenalAnomalyItemsInlineAdmin,
        InfantMusculoskeletalAbnormalItemsInlineAdmin,
        InfantSkinAbnormalItemsInlineAdmin,
        InfantTrisomiesChromosomeItemsInlineAdmin,
        InfantOtherAbnormalityItemsInlineAdmin]
admin.site.register(InfantCongenitalAnomalies, InfantCongenitalAnomaliesAdmin)
