from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.lab_tracker.classes import HivLabTracker
from models import InfantEligibility


class InfantHivLabTracker(HivLabTracker):
    subject_type = 'infant'
    trackers = [(InfantEligibility, 'hiv_status', 'registration_datetime', )]
site_lab_tracker.register(InfantHivLabTracker)
