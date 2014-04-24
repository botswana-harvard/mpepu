from datetime import datetime, date, timedelta
from django.test import TestCase
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError


from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.registration.models import RegisteredSubject
from edc.core.identifier.models import SubjectIdentifier
from edc.testing.tests.factories.test_consent_factory import BaseConsentFactory
from edc.core.bhp_variables.tests.factories import StudySiteFactory
from edc.core.bhp_content_type_map.models import ContentTypeMap
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.core.bhp_content_type_map.classes import ContentTypeMapHelper
from edc.subject.visit_schedule.classes import site_visit_schedules
from edc.subject.registration.tests.factories import RegisteredSubjectFactory
from edc.subject.appointment.models import Appointment
from edc.core.identifier.exceptions import IdentifierError
from edc.core.identifier.models import Sequence


from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration
from apps.mpepu_lab.lab_profiles import MpepuMaternalProfile
from apps.mpepu_maternal.models import MaternalConsent, MaternalVisit, MaternalEligibilityPost
from apps.mpepu_maternal.visit_schedule import MpepuMaternalPostNatalVisitSchedule, MpepuMaternalAnteNatalVisitSchedule, MpepuMaternalPostPartumVisitSchedule
from apps.mpepu_maternal.forms import MaternalEligibilityPostForm, MaternalEligibilityAnteForm
from apps.mpepu_infant.tests.factories import InfantVisitFactory, InfantBirthFactory

from .factories import( MaternalConsentFactory, MaternalEligibilityPostFactory, MaternalEligibilityAnteFactory, MaternalPostRegFactory,
                        MaternalVisitFactory, MaternalLabDelFactory)


class MaternalEnrollmentTests(TestCase):

    def setUp(self):
        try:
            site_lab_profiles.register(MpepuMaternalProfile())
        except AlreadyRegistered:
            pass
        MpepuAppConfiguration()
        site_lab_tracker.autodiscover()
        site_visit_schedules.autodiscover()
        site_visit_schedules.build_all()
