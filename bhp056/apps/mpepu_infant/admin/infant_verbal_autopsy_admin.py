from django.contrib import admin
from edc.base.admin.admin import BaseTabularInline
from ..models import InfantVerbalAutopsyItems, InfantVerbalAutopsy
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
admin.site.register(InfantVerbalAutopsy, InfantVerbalAutopsyAdmin)
