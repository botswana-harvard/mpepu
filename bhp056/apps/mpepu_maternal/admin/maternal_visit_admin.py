from django.contrib import admin
from bhp_appointment.admin import BaseAppointmentModelAdmin
from mpepu_lab.models import MaternalRequisition
from mpepu_maternal.models import MaternalVisit
from mpepu_maternal.forms import MaternalVisitForm


class MaternalVisitAdmin(BaseAppointmentModelAdmin):

    form = MaternalVisitForm
    visit_model_instance_field = 'maternal_visit'
    requisition_model = MaternalRequisition
    dashboard_type = 'maternal'

    list_display = (
        'appointment',
        'report_datetime',
        'reason',
        "info_source",
        'created',
        'user_created',
    )

    list_filter = (
        'report_datetime',
        'reason',
        'appointment__appt_status',
        'appointment__visit_definition__code',
        )

    search_fields = (
        'appointment__registered_subject__subject_identifier',
        'appointment__registered_subject__registration_identifier',
        'appointment__registered_subject__first_name',
        'appointment__registered_subject__identity',
        )

    fields = (
        "appointment",
        "report_datetime",
        "info_source",
        "info_source_other",
        "reason",
        "reason_missed",
        "comments"
        )

admin.site.register(MaternalVisit, MaternalVisitAdmin)
