from django.contrib import admin
from .infant_visit_model_admin import InfantVisitModelAdmin
from ..forms import InfantStoolCollectionForm
from ..models import InfantStoolCollection


class InfantStoolCollectionAdmin(InfantVisitModelAdmin):

    form = InfantStoolCollectionForm

    fields = (
        "infant_visit",
        "sample_obtained",
        "axi_temp",
        "past_diarrhea",
        "diarrhea_past_24hrs",
        "antibiotics_7days",
        "antibiotic_dose_24hrs",
    )
    radio_fields = {
        "sample_obtained": admin.VERTICAL,
        "past_diarrhea": admin.VERTICAL,
        "diarrhea_past_24hrs": admin.VERTICAL,
        "antibiotics_7days": admin.VERTICAL,
        "antibiotic_dose_24hrs": admin.VERTICAL,
    }
admin.site.register(InfantStoolCollection, InfantStoolCollectionAdmin)
