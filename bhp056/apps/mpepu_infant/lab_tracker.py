from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.lab_tracker.classes import HivLabTracker
from models import InfantHivStatus


class InfantHivLabTracker(HivLabTracker):
    subject_type = 'infant'
    models = [(InfantHivStatus, 'recent_hiv_result', 'recent_hiv_date', )]
site_lab_tracker.register(InfantHivLabTracker)
