from collections import OrderedDict

from edc.export.actions import export_as_csv_action
from edc.subject.consent.models import BaseConsentedUuidModel
from edc.subject.visit_tracking.admin import BaseVisitTrackingModelAdmin

from ..models import InfantVisit


class InfantVisitModelAdmin (BaseVisitTrackingModelAdmin):

    """Model Admin for models with a foreignkey to the infant visit model."""

    visit_model = InfantVisit
    visit_model_foreign_key = 'infant_visit'
    dashboard_type = 'infant'

    def get_actions(self, request):
        actions = super(InfantVisitModelAdmin, self).get_actions(request)
        if issubclass(self.model, BaseConsentedUuidModel):
            actions['export_as_csv_action'] = (
                export_as_csv_action(
                    delimiter=',',
                    exclude=['id', self.visit_model_foreign_key, 'revision','modified', 'created','hostname_created','hostname_modified', 'user_modified', 'user_created'],
                    extra_fields=OrderedDict(
                        {'subject_identifier': self.visit_model_foreign_key + '__appointment__registered_subject__subject_identifier',
                         'visit_report_datetime': '%s__report_datetime' % self.visit_model_foreign_key,
                         'gender': self.visit_model_foreign_key + '__appointment__registered_subject__gender',
                         'dob': self.visit_model_foreign_key + '__appointment__registered_subject__dob',
                         'visit_reason': self.visit_model_foreign_key + '__reason',
                         'visit_status': self.visit_model_foreign_key + '__appointment__appt_status',
                         'visit': self.visit_model_foreign_key + '__appointment__visit_definition__code',
                         'visit_instance': self.visit_model_foreign_key + '__appointment__visit_instance'}),
                    ),
                    'export_as_csv_action',
                    "Export to CSV with visit and demographics")
        return actions
