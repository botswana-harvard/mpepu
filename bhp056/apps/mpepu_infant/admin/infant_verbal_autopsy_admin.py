from django.contrib import admin
from bhp_base_admin.admin import BaseTabularInline
from mpepu_infant.classes import RegisteredSubjectModelAdmin
from mpepu_infant.models import InfantVerbalAutopsyItems, InfantVerbalAutopsy
from mpepu_infant.forms import InfantVerbalAutopsyForm


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
