from django.contrib import admin
from bhp_appointment.admin import BaseAppointmentModelAdmin
from mpepu_lab.models import InfantRequisition
from mpepu_infant.models import InfantVisit
from mpepu_infant.forms import InfantVisitForm


class InfantVisitAdmin(BaseAppointmentModelAdmin):

    form = InfantVisitForm
    dashboard_type = 'infant'
    requisition_model = InfantRequisition

    list_filter = ('created',)

    search_fields = (
        'appointment__registered_subject__subject_identifier',
        'appointment__registered_subject__registration_identifier',
        'appointment__registered_subject__first_name',
        'appointment__registered_subject__identity',
        )

    fields = (
        "appointment",
        "report_datetime",
        "reason",
        "reason_missed",
        "study_status",
        "info_source",
        "info_source_other",
        "survival_status",
        "date_last_alive",
        "information_provider",
        "information_provider_other",
        "comments"
        )

    radio_fields = {
        "study_status": admin.VERTICAL,
        "survival_status": admin.VERTICAL,
        "information_provider": admin.VERTICAL,
        }

admin.site.register(InfantVisit, InfantVisitAdmin)
