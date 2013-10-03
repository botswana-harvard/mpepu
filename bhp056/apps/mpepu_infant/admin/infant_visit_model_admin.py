from edc.subject.visit_tracking.admin import BaseVisitTrackingModelAdmin
from ..models import InfantVisit


class InfantVisitModelAdmin (BaseVisitTrackingModelAdmin):

    """Model Admin for models with a foreignkey to the infant visit model."""

    visit_model = InfantVisit
    visit_model_foreign_key = 'infant_visit'
    dashboard_type = 'infant'
