from django.contrib import admin
from mpepu_infant.classes import RegisteredSubjectModelAdmin
from mpepu_infant.models import InfantVitalStatus
from mpepu_infant.forms import InfantVitalStatusForm


class InfantVitalStatusAdmin(RegisteredSubjectModelAdmin):

    form = InfantVitalStatusForm

admin.site.register(InfantVitalStatus, InfantVitalStatusAdmin)
