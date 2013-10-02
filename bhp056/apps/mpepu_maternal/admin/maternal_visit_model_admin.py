from bhp_visit_tracking.admin import BaseVisitTrackingModelAdmin
from mpepu_maternal.models import MaternalVisit


class MaternalVisitModelAdmin (BaseVisitTrackingModelAdmin):

    """Model Admin for models with a foreignkey to the maternal visit model."""

    visit_model = MaternalVisit
    visit_model_foreign_key = 'maternal_visit'
    dashboard_type = 'maternal'
