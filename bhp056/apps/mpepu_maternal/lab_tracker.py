from edc.subject.lab_tracker.classes import lab_tracker
from edc.subject.lab_tracker.classes import HivLabTracker
from models import MaternalEligibilityPost, MaternalEligibilityAnte, MaternalConsent


class MaternalHivLabTracker(HivLabTracker):
    models = [
        (MaternalConsent, 'is_hiv_positive', 'consent_datetime'),
        (MaternalEligibilityPost, 'is_hiv_positive', 'registration_datetime'),
        (MaternalEligibilityAnte, 'is_hiv_positive', 'registration_datetime')
        ]
lab_tracker.register(MaternalHivLabTracker)
