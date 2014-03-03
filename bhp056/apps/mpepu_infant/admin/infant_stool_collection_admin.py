from django.contrib import admin
from .infant_visit_model_admin import InfantVisitModelAdmin
from ..forms import InfantStoolCollectionForm
from ..models import InfantStoolCollection


class InfantStoolCollectionAdmin(InfantVisitModelAdmin):

    form = InfantStoolCollectionForm

    fields = (
        "infant_visit",
        "sample_obtained",
        "stool_texture",
        "axi_temp",
        "past_illness",
        "currently_ill",
        "illness_classification",
        "stools_past_24hrs",
        "diarrhoea_bloody",
        "continuous_loose_stools",
    )
    radio_fields = {
        "sample_obtained": admin.VERTICAL,
        "stool_texture": admin.VERTICAL,
        "past_illness": admin.VERTICAL,
        "currently_ill": admin.VERTICAL,
        "illness_classification": admin.VERTICAL,
        "stools_past_24hrs": admin.VERTICAL,
        "diarrhoea_bloody": admin.VERTICAL,
        "continuous_loose_stools": admin.VERTICAL,
    }
admin.site.register(InfantStoolCollection, InfantStoolCollectionAdmin)
