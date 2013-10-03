from django.contrib import admin
from edc.base.admin.admin import BaseTabularInline
from ..classes import RegisteredSubjectModelAdmin
from ..models import InfantVerbalAutopsyItems, InfantVerbalAutopsy
from ..forms import InfantVerbalAutopsyForm


class InfantVerbalAutopsyItemsInlineAdmin(BaseTabularInline):

    model = InfantVerbalAutopsyItems


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
