from django.contrib import admin
from ..models import InfantVitalStatus
from ..forms import InfantVitalStatusForm
from .registered_subject_model_admin import RegisteredSubjectModelAdmin


class InfantVitalStatusAdmin(RegisteredSubjectModelAdmin):

    form = InfantVitalStatusForm

admin.site.register(InfantVitalStatus, InfantVitalStatusAdmin)
