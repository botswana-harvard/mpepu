from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.lab_tracker.classes import HivLabTracker
from .models import MaternalEligibilityPost, MaternalEligibilityAnte


class MaternalHivLabTracker(HivLabTracker):
    subject_type = 'maternal'
    trackers = [
        (MaternalEligibilityPost, 'is_hiv_positive', 'registration_datetime', ),
        (MaternalEligibilityAnte, 'is_hiv_positive', 'registration_datetime', )]
site_lab_tracker.register(MaternalHivLabTracker)
