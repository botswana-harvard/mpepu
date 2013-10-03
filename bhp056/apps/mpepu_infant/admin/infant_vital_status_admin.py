from django.contrib import admin
from ..classes import RegisteredSubjectModelAdmin
from ..models import InfantVitalStatus
from ..forms import InfantVitalStatusForm


class InfantVitalStatusAdmin(RegisteredSubjectModelAdmin):

    form = InfantVitalStatusForm

admin.site.register(InfantVitalStatus, InfantVitalStatusAdmin)
