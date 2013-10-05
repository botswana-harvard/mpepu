from django.contrib import admin

from ..models import MaternalOffStudy
from ..forms import MaternalOffStudyForm
from edc.subject.off_study.admin import BaseOffStudyModelAdmin


class MaternalOffStudyAdmin(BaseOffStudyModelAdmin):
    form = MaternalOffStudyForm
    dashboard_type = 'maternal'
    visit_model_name = 'maternalvisit'
admin.site.register(MaternalOffStudy, MaternalOffStudyAdmin)
