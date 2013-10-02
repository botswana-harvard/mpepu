from django.contrib import admin

from .registered_subject_model_admin import RegisteredSubjectModelAdmin
from ..models import MaternalDeath
from ..forms import MaternalDeathForm


class MaternalDeathAdmin(RegisteredSubjectModelAdmin):

    form = MaternalDeathForm
    fields = (
        "registered_subject",
        "death_date",
        "death_cause_info",
        "death_cause_info_other",
        "perform_autopsy",
        "death_cause",
        "death_cause_category",
        "death_cause_other",
        "dx_code",
        "illness_duration",
        "death_medical_responsibility",
        "participant_hospitalized",
        "death_reason_hospitalized",
        "days_hospitalized",
        "comment")
    radio_fields = {
        "perform_autopsy": admin.VERTICAL,
        "participant_hospitalized": admin.VERTICAL}
admin.site.register(MaternalDeath, MaternalDeathAdmin)
