from django.contrib import admin
from mpepu_maternal.models import MaternalOffStudy
from mpepu_maternal.forms import MaternalOffStudyForm
from bhp_off_study.admin import BaseOffStudyModelAdmin


class MaternalOffStudyAdmin(BaseOffStudyModelAdmin):
    form = MaternalOffStudyForm
    dashboard_type = 'maternal'
    visit_model_name = 'maternalvisit'
admin.site.register(MaternalOffStudy, MaternalOffStudyAdmin)
