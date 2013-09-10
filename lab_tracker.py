from bhp_lab_tracker.classes import lab_tracker
from bhp_lab_tracker.classes import HivLabTracker
from models import InfantHivStatus


class InfantHivLabTracker(HivLabTracker):
    models = [(InfantHivStatus, 'recent_hiv_result', 'recent_hiv_date')]
lab_tracker.register(InfantHivLabTracker)
