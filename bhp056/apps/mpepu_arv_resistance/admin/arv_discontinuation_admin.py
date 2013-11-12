from django.contrib import admin

from apps.mpepu_maternal.admin import MaternalVisitModelAdmin

from ..models import ArvResistanceDiscontinuation


class ArvResistanceDiscontinuationAdmin(MaternalVisitModelAdmin):
    
    fields = (
        "maternal_visit",
        "regimen",
        "date_arv_started",
        "discontinued_by",
        "stopped_once",
        "last_arv_date",
        "last_ftc_date",
        "last_tdf_date",
        "last_3tc_date",
        "as_prescribed",
        "info_source",
    )
    radio_fields =  {'regimen': admin.VERTICAL,
                     'discontinued_by':admin.VERTICAL,
                     'stopped_once':admin.VERTICAL,
                     'as_prescribed':admin.VERTICAL}
admin.site.register(ArvResistanceDiscontinuation, ArvResistanceDiscontinuationAdmin)
