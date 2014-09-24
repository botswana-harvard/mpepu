from django.contrib import admin

from edc.base.modeladmin.admin import BaseTabularInline

from ..models import InfantVerbalAutopsyItems, InfantVerbalAutopsy, InfantVisit
from ..forms import InfantVerbalAutopsyForm
from .registered_subject_model_admin import RegisteredSubjectModelAdmin


class InfantVerbalAutopsyItemsInlineAdmin(BaseTabularInline):

    model = InfantVerbalAutopsyItems
    extra = 1


class InfantVerbalAutopsyAdmin(RegisteredSubjectModelAdmin):

    form = InfantVerbalAutopsyForm
    inlines = [
        InfantVerbalAutopsyItemsInlineAdmin,
        ]

    filter_horizontal = ("source",)
    radio_fields = {
        "sign_symptoms": admin.VERTICAL,
    }

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_visit":
            if request.GET.get('infant_visit'):
                kwargs["queryset"] = InfantVisit.objects.filter(id=request.GET.get('infant_visit'))

        return super(InfantVerbalAutopsyAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(InfantVerbalAutopsy, InfantVerbalAutopsyAdmin)
