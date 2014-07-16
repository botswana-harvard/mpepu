from django.contrib import admin
from collections import OrderedDict

from edc.export.actions import export_as_csv_action
from edc.subject.off_study.admin import BaseOffStudyModelAdmin

from ..models import MaternalOffStudy, MaternalVisit
from ..forms import MaternalOffStudyForm


class MaternalOffStudyAdmin(BaseOffStudyModelAdmin):
    form = MaternalOffStudyForm
    dashboard_type = 'maternal'
    visit_model_name = 'maternalvisit'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "maternal_visit":
            if request.GET.get('maternal_visit'):
                kwargs["queryset"] = MaternalVisit.objects.filter(id=request.GET.get('maternal_visit'))

        return super(MaternalOffStudyAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    actions = [export_as_csv_action(description="CSV Export of registered_subject",
        fields=[],
        delimiter=',',
        exclude=['created', 'modified', 'user_created', 'user_modified', 'revision', 'id', 'hostname_created', 'hostname_modified' ],
        extra_fields=OrderedDict(
            {'subject_identifier': 'registered_subject__subject_identifier',
             'gender': 'registered_subject__gender',
             'dob': 'registered_subject__dob',
             'registered': 'registered_subject__registration_datetime'}),
        )]
admin.site.register(MaternalOffStudy, MaternalOffStudyAdmin)
