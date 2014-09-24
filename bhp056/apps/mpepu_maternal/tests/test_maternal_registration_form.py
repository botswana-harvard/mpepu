from datetime import datetime, date, timedelta
from django.test import TestCase
from django.core.exceptions import ValidationError

from edc.core.bhp_variables.tests.factories import StudySiteFactory
from edc.core.identifier.models import Sequence
from edc.core.identifier.models import SubjectIdentifier
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.subject.appointment.models import Appointment
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.registration.models import RegisteredSubject
from edc.subject.visit_schedule.classes import site_visit_schedules

from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration
from apps.mpepu_lab.lab_profiles import MpepuMaternalProfile
from apps.mpepu_maternal.forms import MaternalEligibilityPostForm, MaternalEligibilityAnteForm, MaternalConsentForm
from apps.mpepu_maternal.models import MaternalConsent, MaternalVisit, MaternalEligibilityPost
from apps.mpepu_maternal.visit_schedule import MpepuMaternalPostNatalVisitSchedule, MpepuMaternalAnteNatalVisitSchedule, MpepuMaternalPostPartumVisitSchedule

from .factories import( MaternalConsentFactory, MaternalEligibilityPostFactory, MaternalEligibilityAnteFactory, MaternalPostRegFactory,
                        MaternalVisitFactory, MaternalLabDelFactory)


class MaternalRegistrationFormTests(TestCase):

    def setUp(self):
        try:
            site_lab_profiles.register(MpepuMaternalProfile())
        except AlreadyRegistered:
            pass
        MpepuAppConfiguration().prepare()
        site_lab_tracker.autodiscover()
        site_visit_schedules.autodiscover()
        site_visit_schedules.build_all()

    def test_consent_consent_reviewed(self):
        print "assert that if consent reviewed is No, consent should not save." 
        consent_form = MaternalConsentForm()
        consent_form.cleaned_data = {'gender':'F',
                                     'identity_type' : 'omang',
                                     'consent_reviewed':'No',
                                     'study_questions' : 'Yes',
                                     'assessment_score' : 'Yes',
                                     'consent_copy' : 'Yes'
                                     }
        self.assertRaisesMessage(ValidationError,'If consent reviewed is No, patient cannot be enrolled',consent_form.clean)

    def test_consent_identity_mismatch(self): 
        print "assert that if identity and confirm identity does not match, error will be raised."
        consent_form = MaternalConsentForm()
        consent_form.cleaned_data = {'identity':'identity',
                                     'confirm_identity':'confirm',
                                     'gender':'F',
                                     'identity_type' : 'omang',
                                     'consent_reviewed':'Yes',
                                     'study_questions' : 'Yes',
                                     'assessment_score' : 'Yes',
                                     'consent_copy' : 'Yes'
                                     }
        self.assertRaisesMessage(ValidationError,'Identity mismatch. Identity number must match the confirmation field.',consent_form.clean)

    def test_consent_assessment_score(self):
        print "assert that assessment score should at least be a passing score"
        consent_form = MaternalConsentForm()
        consent_form.cleaned_data = {'gender':'F',
                                     'identity_type' : 'omang',
                                     'consent_reviewed':'Yes',
                                     'study_questions' : 'Yes',
                                     'assessment_score' : 'No',
                                     'consent_copy' : 'Yes'
                                     }
        self.assertRaisesMessage(ValidationError,'Client assessment should at least be a passing score. If No, patient cannot be enrolled',consent_form.clean)

    def test_consent_study_questions(self):
        print "assert that study questions should at least be a passing score"
        consent_form = MaternalConsentForm()
        consent_form.cleaned_data = {'gender':'F',
                                    'identity_type' : 'omang',
                                    'consent_reviewed':'Yes',
                                    'study_questions' : 'No',
                                    'assessment_score' : 'No',
                                    'consent_copy' : 'Yes'
                                    }
        self.assertRaisesMessage(ValidationError,'If unable to answer questions from client and/or None, patient cannot be enrolled',consent_form.clean)

    def test_consent_dob(self):
        #TODO: This validation is not working
#         print "assert that the dob should not be greater than the consent date"
#         consent_form = MaternalConsentForm()
#         consent_form.cleaned_data = {'gender':'F',
#                                     'identity_type' : 'omang',
#                                     'consent_reviewed':'Yes',
#                                     'study_questions' : 'Yes',
#                                     'assessment_score' : 'Yes',
#                                     'consent_copy' : 'Yes',
#                                     'dob':date(date.today() + timedelta(years=5)),
#                                     }
#         self.assertRaises(ValidationError, consent_form.clean)
        print "assert that the dob should not be less than minimum consent age"
        consent_form = MaternalConsentForm()
        consent_form.cleaned_data = {'gender':'F',
                                    'identity_type' : 'omang',
                                    'consent_reviewed':'Yes',
                                    'study_questions' : 'Yes',
                                    'assessment_score' : 'Yes',
                                    'consent_copy' : 'Yes',
                                    'dob':date.today()
                                    }
        self.assertRaises(ValidationError, consent_form.clean)