from django.contrib import admin

from edc.base.admin.admin import BaseModelAdmin
from edc.base.admin.admin import BaseTabularInline

from ..models import (InfantCnsAbnormalityItems, InfantFacialDefectItems, InfantCleftDisorderItems, InfantMouthUpGastrointestinalItems,
                                 InfantCardiovascularDisorderItems, InfantRespiratoryDefectItems, InfantLowerGastrointestinalItems, InfantFemaleGenitalAnomalyItems,
                                 InfantMaleGenitalAnomalyItems, InfantRenalAnomalyItems, InfantMusculoskeletalAbnormalItems,
                                 InfantSkinAbnormalItems, InfantTrisomiesChromosomeItems, InfantOtherAbnormalityItems, InfantCongenitalAnomalies, )
from ..forms import (InfantCongenitalAnomaliesForm, InfantCnsAbnormalityItemsForm, InfantFacialDefectItemsForm, InfantCleftDisorderItemsForm,
                     InfantMouthUpGastrointestinalItemsForm, InfantCardiovascularDisorderItemsForm, InfantRespiratoryDefectItemsForm, InfantLowerGastrointestinalItemsForm,
                     InfantFemaleGenitalAnomalyItemsForm, InfantMaleGenitalAnomalyItemsForm, InfantRenalAnomalyItemsForm, InfantMusculoskeletalAbnormalItemsForm, 
                     InfantOtherAbnormalityItemsForm, InfantTrisomiesChromosomeItemsForm, InfantSkinAbnormalItemsForm)
from .registered_subject_model_admin import RegisteredSubjectModelAdmin


class InfantCnsAbnormalityItemsAdmin(BaseModelAdmin):
    form = InfantCnsAbnormalityItemsForm
admin.site.register(InfantCnsAbnormalityItems, InfantCnsAbnormalityItemsAdmin)
  
    
class InfantCnsAbnormalityItemsInlineAdmin(BaseTabularInline):

    model = InfantCnsAbnormalityItems
    form = InfantCnsAbnormalityItemsForm


class InfantFacialDefectItemsAdmin(BaseModelAdmin):
    form = InfantFacialDefectItemsForm
admin.site.register(InfantFacialDefectItems, InfantFacialDefectItemsAdmin)
   
    
class InfantFacialDefectItemsInlineAdmin(BaseTabularInline):

    model = InfantFacialDefectItems
    form = InfantFacialDefectItemsForm


class InfantCleftDisorderItemsInlineAdmin(BaseTabularInline):

    model = InfantCleftDisorderItems
    form = InfantCleftDisorderItemsForm
    
    
class InfantCleftDisorderItemsAdmin(BaseModelAdmin):
    form = InfantCleftDisorderItemsForm
admin.site.register(InfantCleftDisorderItems, InfantCleftDisorderItemsAdmin)


class InfantMouthUpGastrointestinalItemsAdmin(BaseModelAdmin):
    form = InfantMouthUpGastrointestinalItemsForm
admin.site.register(InfantMouthUpGastrointestinalItems, InfantMouthUpGastrointestinalItemsAdmin)


class InfantMouthUpGastrointestinalItemsInlineAdmin(BaseTabularInline):

    model = InfantMouthUpGastrointestinalItems
    form = InfantMouthUpGastrointestinalItemsForm


class InfantCardiovascularDisorderItemsAdmin(BaseModelAdmin):
    form = InfantCardiovascularDisorderItemsForm
admin.site.register(InfantCardiovascularDisorderItems, InfantCardiovascularDisorderItemsAdmin)


class InfantCardiovascularDisorderItemsInlineAdmin(BaseTabularInline):

    model = InfantCardiovascularDisorderItems
    form = InfantCardiovascularDisorderItemsForm


class InfantRespiratoryDefectItemsAdmin(BaseModelAdmin):
    form = InfantRespiratoryDefectItemsForm
admin.site.register(InfantRespiratoryDefectItems, InfantRespiratoryDefectItemsAdmin)


class InfantRespiratoryDefectItemsInlineAdmin(BaseTabularInline):

    model = InfantRespiratoryDefectItems
    form = InfantRespiratoryDefectItemsForm


class InfantLowerGastrointestinalItemsAdmin(BaseModelAdmin):
    form = InfantLowerGastrointestinalItemsForm
admin.site.register(InfantLowerGastrointestinalItems, InfantLowerGastrointestinalItemsAdmin)


class InfantLowerGastrointestinalItemsInlineAdmin(BaseTabularInline):

    model = InfantLowerGastrointestinalItems
    form = InfantLowerGastrointestinalItemsForm


class InfantFemaleGenitalAnomalyItemsAdmin(BaseModelAdmin):
    form = InfantFemaleGenitalAnomalyItemsForm
admin.site.register(InfantFemaleGenitalAnomalyItems, InfantFemaleGenitalAnomalyItemsAdmin)


class InfantFemaleGenitalAnomalyItemsInlineAdmin(BaseTabularInline):

    model = InfantFemaleGenitalAnomalyItems
    form = InfantFemaleGenitalAnomalyItemsForm


class InfantMaleGenitalAnomalyItemsAdmin(BaseModelAdmin):
    form = InfantMaleGenitalAnomalyItemsForm
admin.site.register(InfantMaleGenitalAnomalyItems, InfantMaleGenitalAnomalyItemsAdmin)


class InfantMaleGenitalAnomalyItemsInlineAdmin(BaseTabularInline):

    model = InfantMaleGenitalAnomalyItems
    form = InfantMaleGenitalAnomalyItemsForm


class InfantRenalAnomalyItemsAdmin(BaseModelAdmin):
    form = InfantRenalAnomalyItemsForm
admin.site.register(InfantRenalAnomalyItems, InfantRenalAnomalyItemsAdmin)


class InfantRenalAnomalyItemsInlineAdmin(BaseTabularInline):

    model = InfantRenalAnomalyItems
    form = InfantRenalAnomalyItemsForm


class InfantMusculoskeletalAbnormalItemsAdmin(BaseModelAdmin):
    form = InfantMusculoskeletalAbnormalItemsForm
admin.site.register(InfantMusculoskeletalAbnormalItems, InfantMusculoskeletalAbnormalItemsAdmin)


class InfantMusculoskeletalAbnormalItemsInlineAdmin(BaseTabularInline):

    model = InfantMusculoskeletalAbnormalItems
    form = InfantMusculoskeletalAbnormalItemsForm


class InfantSkinAbnormalItemsAdmin(BaseModelAdmin):
    form = InfantSkinAbnormalItemsForm
admin.site.register(InfantSkinAbnormalItems, InfantSkinAbnormalItemsAdmin)


class InfantSkinAbnormalItemsInlineAdmin(BaseTabularInline):

    model = InfantSkinAbnormalItems
    form = InfantSkinAbnormalItemsForm


class InfantTrisomiesChromosomeItemsAdmin(BaseModelAdmin):
    form = InfantTrisomiesChromosomeItemsForm
admin.site.register(InfantTrisomiesChromosomeItems, InfantTrisomiesChromosomeItemsAdmin)


class InfantTrisomiesChromosomeItemsInlineAdmin(BaseTabularInline):

    model = InfantTrisomiesChromosomeItems
    form = InfantTrisomiesChromosomeItemsForm


class InfantOtherAbnormalityItemsAdmin(BaseModelAdmin):
    form = InfantOtherAbnormalityItemsForm
admin.site.register(InfantOtherAbnormalityItems, InfantOtherAbnormalityItemsAdmin)


class InfantOtherAbnormalityItemsInlineAdmin(BaseTabularInline):

    model = InfantOtherAbnormalityItems
    form = InfantOtherAbnormalityItemsForm


class InfantCongenitalAnomaliesAdmin(RegisteredSubjectModelAdmin):

    form = InfantCongenitalAnomaliesForm
    inlines = [
        InfantCnsAbnormalityItemsInlineAdmin,
        InfantFacialDefectItemsInlineAdmin,
        InfantCleftDisorderItemsInlineAdmin,
        InfantMouthUpGastrointestinalItemsInlineAdmin,
        InfantCardiovascularDisorderItemsInlineAdmin,
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
