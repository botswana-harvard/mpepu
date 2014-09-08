from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.lab_tracker.classes import HivLabTracker
from edc.lab.lab_clinic_api.models import ResultItem


class InfantHivLabTracker(HivLabTracker):
    subject_type = 'infant'
    trackers = [(ResultItem, 'result_item_value', 'result_item_datetime'), ]
site_lab_tracker.register(InfantHivLabTracker)
