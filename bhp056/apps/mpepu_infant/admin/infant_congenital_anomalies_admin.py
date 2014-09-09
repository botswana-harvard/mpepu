from django.contrib import admin

from edc.base.modeladmin.admin import BaseModelAdmin
from edc.base.modeladmin.admin import BaseTabularInline

from ..models import (InfantCnsAbnormalityItems, InfantFacialDefectItems, InfantCleftDisorderItems, InfantMouthUpGastrointestinalItems,
                                 InfantCardiovascularDisorderItems, InfantRespiratoryDefectItems, InfantLowerGastrointestinalItems, InfantFemaleGenitalAnomalyItems,
                                 InfantMaleGenitalAnomalyItems, InfantRenalAnomalyItems, InfantMusculoskeletalAbnormalItems,
                                 InfantSkinAbnormalItems, InfantTrisomiesChromosomeItems, InfantOtherAbnormalityItems, InfantCongenitalAnomalies,
                                 InfantVisit)
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
    extra = 1


class InfantFacialDefectItemsAdmin(BaseModelAdmin):
    form = InfantFacialDefectItemsForm
admin.site.register(InfantFacialDefectItems, InfantFacialDefectItemsAdmin)


class InfantFacialDefectItemsInlineAdmin(BaseTabularInline):

    model = InfantFacialDefectItems
    form = InfantFacialDefectItemsForm
    extra = 1


class InfantCleftDisorderItemsInlineAdmin(BaseTabularInline):

    model = InfantCleftDisorderItems
    form = InfantCleftDisorderItemsForm
    extra = 1


class InfantCleftDisorderItemsAdmin(BaseModelAdmin):
    form = InfantCleftDisorderItemsForm
admin.site.register(InfantCleftDisorderItems, InfantCleftDisorderItemsAdmin)


class InfantMouthUpGastrointestinalItemsAdmin(BaseModelAdmin):
    form = InfantMouthUpGastrointestinalItemsForm
admin.site.register(InfantMouthUpGastrointestinalItems, InfantMouthUpGastrointestinalItemsAdmin)


class InfantMouthUpGastrointestinalItemsInlineAdmin(BaseTabularInline):

    model = InfantMouthUpGastrointestinalItems
    form = InfantMouthUpGastrointestinalItemsForm
    extra = 1


class InfantCardiovascularDisorderItemsAdmin(BaseModelAdmin):
    form = InfantCardiovascularDisorderItemsForm
admin.site.register(InfantCardiovascularDisorderItems, InfantCardiovascularDisorderItemsAdmin)


class InfantCardiovascularDisorderItemsInlineAdmin(BaseTabularInline):

    model = InfantCardiovascularDisorderItems
    form = InfantCardiovascularDisorderItemsForm
    extra = 1


class InfantRespiratoryDefectItemsAdmin(BaseModelAdmin):
    form = InfantRespiratoryDefectItemsForm
admin.site.register(InfantRespiratoryDefectItems, InfantRespiratoryDefectItemsAdmin)


class InfantRespiratoryDefectItemsInlineAdmin(BaseTabularInline):

    model = InfantRespiratoryDefectItems
    form = InfantRespiratoryDefectItemsForm
    extra = 1


class InfantLowerGastrointestinalItemsAdmin(BaseModelAdmin):
    form = InfantLowerGastrointestinalItemsForm
admin.site.register(InfantLowerGastrointestinalItems, InfantLowerGastrointestinalItemsAdmin)


class InfantLowerGastrointestinalItemsInlineAdmin(BaseTabularInline):

    model = InfantLowerGastrointestinalItems
    form = InfantLowerGastrointestinalItemsForm
    extra = 1


class InfantFemaleGenitalAnomalyItemsAdmin(BaseModelAdmin):
    form = InfantFemaleGenitalAnomalyItemsForm
admin.site.register(InfantFemaleGenitalAnomalyItems, InfantFemaleGenitalAnomalyItemsAdmin)


class InfantFemaleGenitalAnomalyItemsInlineAdmin(BaseTabularInline):

    model = InfantFemaleGenitalAnomalyItems
    form = InfantFemaleGenitalAnomalyItemsForm
    extra = 1


class InfantMaleGenitalAnomalyItemsAdmin(BaseModelAdmin):
    form = InfantMaleGenitalAnomalyItemsForm
admin.site.register(InfantMaleGenitalAnomalyItems, InfantMaleGenitalAnomalyItemsAdmin)


class InfantMaleGenitalAnomalyItemsInlineAdmin(BaseTabularInline):

    model = InfantMaleGenitalAnomalyItems
    form = InfantMaleGenitalAnomalyItemsForm
    extra = 1


class InfantRenalAnomalyItemsAdmin(BaseModelAdmin):
    form = InfantRenalAnomalyItemsForm
admin.site.register(InfantRenalAnomalyItems, InfantRenalAnomalyItemsAdmin)


class InfantRenalAnomalyItemsInlineAdmin(BaseTabularInline):

    model = InfantRenalAnomalyItems
    form = InfantRenalAnomalyItemsForm
    extra = 1


class InfantMusculoskeletalAbnormalItemsAdmin(BaseModelAdmin):
    form = InfantMusculoskeletalAbnormalItemsForm
admin.site.register(InfantMusculoskeletalAbnormalItems, InfantMusculoskeletalAbnormalItemsAdmin)


class InfantMusculoskeletalAbnormalItemsInlineAdmin(BaseTabularInline):

    model = InfantMusculoskeletalAbnormalItems
    form = InfantMusculoskeletalAbnormalItemsForm
    extra = 1


class InfantSkinAbnormalItemsAdmin(BaseModelAdmin):
    form = InfantSkinAbnormalItemsForm
admin.site.register(InfantSkinAbnormalItems, InfantSkinAbnormalItemsAdmin)


class InfantSkinAbnormalItemsInlineAdmin(BaseTabularInline):

    model = InfantSkinAbnormalItems
    form = InfantSkinAbnormalItemsForm
    extra = 1


class InfantTrisomiesChromosomeItemsAdmin(BaseModelAdmin):
    form = InfantTrisomiesChromosomeItemsForm
admin.site.register(InfantTrisomiesChromosomeItems, InfantTrisomiesChromosomeItemsAdmin)


class InfantTrisomiesChromosomeItemsInlineAdmin(BaseTabularInline):

    model = InfantTrisomiesChromosomeItems
    form = InfantTrisomiesChromosomeItemsForm
    extra = 1


class InfantOtherAbnormalityItemsAdmin(BaseModelAdmin):
    form = InfantOtherAbnormalityItemsForm
admin.site.register(InfantOtherAbnormalityItems, InfantOtherAbnormalityItemsAdmin)


class InfantOtherAbnormalityItemsInlineAdmin(BaseTabularInline):

    model = InfantOtherAbnormalityItems
    form = InfantOtherAbnormalityItemsForm
    extra = 1


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
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_visit":
            if request.GET.get('infant_visit'):
                kwargs["queryset"] = InfantVisit.objects.filter(id=request.GET.get('infant_visit'))

        return super(InfantCongenitalAnomaliesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(InfantCongenitalAnomalies, InfantCongenitalAnomaliesAdmin)
