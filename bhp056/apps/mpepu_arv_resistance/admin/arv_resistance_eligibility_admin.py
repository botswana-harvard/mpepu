from django.contrib import admin

from apps.mpepu_maternal.admin import MaternalVisitModelAdmin

from ..models import ArvResistanceEligibility


class ArvResistanceEligibilityAdmin(MaternalVisitModelAdmin):
    
    fields = (
        "maternal_visit",
        "report_datetime",
        "co_enrolled",
        "status_evidence",
        "lates_cd4",
        "who_illness",
        "stopped_arv",
        "incarcerated",
        )
    
    radio_fields = {
        "co_enrolled":admin.VERTICAL,
        "status_evidence":admin.VERTICAL,
        "who_illness":admin.VERTICAL,
        "stopped_arv":admin.VERTICAL,
        "incarcerated":admin.VERTICAL,
        }
    
admin.site.register(ArvResistanceEligibility, ArvResistanceEligibilityAdmin)
