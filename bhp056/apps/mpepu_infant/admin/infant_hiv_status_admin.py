from django.contrib import admin
from ..classes import InfantVisitModelAdmin
from ..models import InfantHivStatus
from ..forms import InfantHivStatusForm


class InfantHivStatusAdmin(InfantVisitModelAdmin):

    form = InfantHivStatusForm
    fields = (
        "infant_visit",
        "recent_hiv_result",
        "recent_hiv_date",
        "recent_hiv_date_est",
        "test_place",
        "result_record",
        "date_first_pos",
        "infant_haart",
        "infant_haart_date",
    )
    radio_fields = {
        "recent_hiv_result": admin.VERTICAL,
        "recent_hiv_date_est": admin.VERTICAL,
        "result_record": admin.VERTICAL,
        "infant_haart": admin.VERTICAL
    }
admin.site.register(InfantHivStatus, InfantHivStatusAdmin)
