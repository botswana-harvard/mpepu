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
from apps.mpepu_infant.tests.factories import InfantBirthFactory

from .factories import( MaternalConsentFactory, MaternalEligibilityPostFactory, MaternalEligibilityAnteFactory, MaternalPostRegFactory,
                        MaternalVisitFactory, MaternalLabDelFactory)


class MaternalRegistrationTests(TestCase):

    def setUp(self):
        try:
            site_lab_profiles.register(MpepuMaternalProfile())
        except AlreadyRegistered:
            pass
        MpepuAppConfiguration()
        site_lab_tracker.autodiscover()
        site_visit_schedules.autodiscover()
        site_visit_schedules.build_all()

    def test_maternal_consent(self):
        print """Test Consenting a mother"""
        MaternalConsent.objects.all().delete()
        study_site = StudySiteFactory(site_code=2)
        maternal_consent = MaternalConsentFactory(study_site=study_site)
        print "Maternal Consent: {}".format(maternal_consent)
        print "Maternal Consent subject identifier: {}".format(maternal_consent.subject_identifier)
        print 'confirm maternal subject identifier in bhp_identifier.models.SubjectIdentifier'
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier=maternal_consent.subject_identifier))
        print "registered subject of maternal consent: {}".format(maternal_consent.registered_subject)
        print "assert there is one maternal consent saved"
        self.assertEquals(MaternalConsent.objects.count(),1)
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print "assert registered subject was created and updated successfully for the subject consent"
        self.assertEqual(registered_subject, maternal_consent.registered_subject)
        print 'setup up another mother'
        maternal_consent = MaternalConsentFactory(study_site=study_site)
        print 'consent a mother: {}'.format(maternal_consent)
        print 'assert there are two consents'
        self.assertEquals(MaternalConsent.objects.count(),2)
        print 'confirm maternal subject identifier in bhp_identifier.models.SubjectIdentifier'
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier=maternal_consent.subject_identifier))
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print "assert registered subject was created and updated successfully for the subject consent"
        self.assertEqual(registered_subject, maternal_consent.registered_subject)

        print "assert that creating a consent with an identity that already exists fails"
        try:
            MaternalConsentFactory(identity=maternal_consent.identity)
            print "Failed to throw exception"
        except:
            print "Exception thrown as excepted."
        #TODO: DOB future date doesnt work quite right, can consent for birth date of today
        print "assert that if dob not future"
        try:
            MaternalConsentFactory(dob=date.today()+timedelta(years=5))
            print "Failed to throw exception"
        except:
            print "Exception thrown as excepted."
        print "assert if participant is not literate and no witness is given, maternal consent should not save"
        try:
            MaternalConsentFactory(is_literate='No')
            print "Failed to throw exception"
        except:
            print "Exception thrown as excepted."
        print " assert that if participant is under involuntary incarceration then participant cannot be consented" 
        try:
            MaternalConsentFactory(is_incarcerated='Yes')
            print "Failed to throw exception"
        except:
            print "Exception thrown as excepted."
        print "assert that if participant has not completed the assessment of understanding with a passing score then they cannot be consented"
        print "assert that if participant is not given a consent copy then they cannot be consented."
        try:
            MaternalConsentFactory(consent_copy='No')
            print "Failed to throw exception"
        except:

            print "Exception thrown as excepted." 

    def test_post_partum_enroll(self):
        print """Test the post partum registration of a mother"""
        MaternalConsent.objects.all().delete()
        print "consent a mother"
        consent = MaternalConsentFactory()
        print consent.registered_subject
        print "check if mother is eligible"
        post_elibility = MaternalEligibilityPostFactory(maternal_consent=consent, registered_subject=consent.registered_subject)
        print "assert that 2000M appointment was created"
        appointment = Appointment.objects.get(registered_subject=consent.registered_subject, visit_definition__code='2000M')
        self.assertEqual(appointment.visit_definition.code, '2000M')
        all_appointments = Appointment.objects.all()
        print "assert that 8 appointments were created, i.e. 2000M, 2010M,2020M,2030M,2060M,2090M,2120M,2150M and 2180ME"
        self.assertEqual(all_appointments.count(),9)
        print "set up a maternal visit for this mother"
        visit = MaternalVisitFactory(appointment=appointment)
        print"create a maternallabdel: registering 1 of 1 infants"
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=visit, live_infants=1, live_infants_to_register=1)
        print maternal_lab_del
        print 'confirm infant subject identifier in bhp_identifier.models.SubjectIdentifier and follows derived format {0}'.format('{0}-10'.format(consent.subject_identifier))
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier='{0}-10'.format(consent.subject_identifier)))
        print "consent a mother"
        consent = MaternalConsentFactory()
        print consent.registered_subject

    def test_ante_natal_enroll(self):
        print """Test ante Natal Registration of a mother"""
        MaternalConsent.objects.all().delete()
        print "consent a mother"
        consent = MaternalConsentFactory()
        print "check if mother is eligible "
        ante_eligibility = MaternalEligibilityAnteFactory(maternal_consent=consent, registered_subject=consent.registered_subject)
        print "Maternal Eligibility {}".format(ante_eligibility)
        print "assert that 1000M appointment was created"
        appointment = Appointment.objects.get(registered_subject=consent.registered_subject, visit_definition__code='1000M')
        self.assertEqual(appointment.visit_definition.code, '1000M')
        all_appointments = Appointment.objects.all()
        print "assert that only one appointment was created, i.e. 1000M"
        self.assertEqual(all_appointments.count(),1)
        print "set up a maternal visit for this mother"
        visit = MaternalVisitFactory(appointment=appointment)
        print"create a maternallabdel: registering 1 of 1 infants"
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=visit, live_infants=1, live_infants_to_register=1)
        print maternal_lab_del
        print 'confirm infant subject identifier in bhp_identifier.models.SubjectIdentifier and follows derived format {0}'.format('{0}-10'.format(consent.subject_identifier))
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier='{0}-10'.format(consent.subject_identifier)))

    def test_maternal_lab_del(self):
        print """Test maternal labour and delivery"""
        MaternalConsent.objects.all().delete()
        study_site = StudySiteFactory(site_code=2)
        print "consent a mother"
        consent = MaternalConsentFactory(study_site=study_site)
        print consent.registered_subject
        print "check if mother is eligible"
        post_elibility = MaternalEligibilityPostFactory(maternal_consent=consent, registered_subject=consent.registered_subject)
        print "assert that 2000M appointment was created"
        appointment = Appointment.objects.get(registered_subject=consent.registered_subject, visit_definition__code='2000M')
        self.assertEqual(appointment.visit_definition.code, '2000M')
        all_appointments = Appointment.objects.all()
        print "assert that 8 appointments were created, i.e. 2000M, 2010M,2020M,2030M,2060M,2090M,2120M,2150M and 2180ME"
        self.assertEqual(all_appointments.count(),9)
        print "set up a maternal visit for this mother"
        visit = MaternalVisitFactory(appointment=appointment)
        print"create a maternallabdel: registering 1 of 1 infants"
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=visit, live_infants=1, live_infants_to_register=1)
        print "assert that only one infant was created"
        infants = RegisteredSubject.objects.filter(relative_identifier=consent.registered_subject.subject_identifier)
        self.assertEquals(infants.count(), 1)
        print "setup a new mother"
        consent = MaternalConsentFactory(study_site=study_site)
        print consent.registered_subject
        print "check if mother is eligible"
        post_elibility = MaternalEligibilityPostFactory(maternal_consent=consent, registered_subject=consent.registered_subject)
        print "assert that 2000M appointment was created"
        appointment = Appointment.objects.get(registered_subject=consent.registered_subject, visit_definition__code='2000M')
        self.assertEqual(appointment.visit_definition.code, '2000M')
        print "set up a maternal visit for this mother"
        visit = MaternalVisitFactory(appointment=appointment)
        print 'create a maternal lab-del: registering 2 of 1 infant'
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=visit, live_infants=2, live_infants_to_register=1)
        print maternal_lab_del
        print 'confirm infant subject identifier in bhp_identifier.models.SubjectIdentifier and follows derived format {0}'.format('{0}-10'.format(consent.subject_identifier))
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier='{0}-10'.format(consent.subject_identifier)))

        print 'setup up another mother'
        print 'consent a mother'
        maternal_consent = MaternalConsentFactory(study_site=study_site)
        print maternal_consent.subject_identifier
        print 'confirm maternal subject identifier in bhp_identifier.models.SubjectIdentifier'
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier=maternal_consent.subject_identifier))
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'enroll mother ante natal'
        maternal_eligibility_ante = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject)
        print 'setup a maternal visit for this mother'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        maternal_visit = MaternalVisitFactory(appointment=appointment)
        print 'create a maternal lab-del: registering 2 of 2 infant'
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit, live_infants=2, live_infants_to_register=2)
        print maternal_lab_del
        print 'confirm infant subject identifier in bhp_identifier.models.SubjectIdentifier and follows derived format {0} and {1}'.format('{0}-25'.format(maternal_consent.subject_identifier), '{0}-35'.format(maternal_consent.subject_identifier))
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier='{0}-25'.format(maternal_consent.subject_identifier)))
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier='{0}-35'.format(maternal_consent.subject_identifier)))

        print 'setup up another mother'
        print 'consent a mother'
        maternal_consent = MaternalConsentFactory(study_site=study_site)
        print maternal_consent.subject_identifier
        print 'confirm maternal subject identifier in bhp_identifier.models.SubjectIdentifier'
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier=maternal_consent.subject_identifier))
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'enroll mother ante natal'
        maternal_eligibility_ante = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject)
        print 'setup a maternal visit for this mother'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        maternal_visit = MaternalVisitFactory(appointment=appointment)
        print 'create a maternal lab-del: registering 2 of 3 infant'
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit, live_infants=3, live_infants_to_register=2)
        print maternal_lab_del
        print 'confirm infant subject identifier in bhp_identifier.models.SubjectIdentifier and follows derived format \n{0} and \n{1}.'.format(
            '{0}-36'.format(maternal_consent.subject_identifier),
            '{0}-46'.format(maternal_consent.subject_identifier))
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier='{0}-36'.format(maternal_consent.subject_identifier)))
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier='{0}-46'.format(maternal_consent.subject_identifier)))

        print 'setup up another mother'
        print 'consent a mother'
        maternal_consent = MaternalConsentFactory(study_site=study_site)
        print maternal_consent.subject_identifier
        print 'confirm maternal subject identifier in bhp_identifier.models.SubjectIdentifier'
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier=maternal_consent.subject_identifier))
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'enroll mother ante natal'
        maternal_eligibility_ante = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject)
        print 'setup a maternal visit for this mother'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        maternal_visit = MaternalVisitFactory(appointment=appointment)
        print 'create a maternal lab-del: registering 4 of 4 infant'
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit, live_infants=4, live_infants_to_register=4)
        print maternal_lab_del
        print 'confirm infant subject identifier in bhp_identifier.models.SubjectIdentifier and follows derived format \n{0}\n{1}\n{2}\n{3}.'.format(
            '{0}-47'.format(maternal_consent.subject_identifier),
            '{0}-57'.format(maternal_consent.subject_identifier),
            '{0}-67'.format(maternal_consent.subject_identifier),
            '{0}-77'.format(maternal_consent.subject_identifier),)
        self.assertIsNotNone(SubjectIdentifier.objects.get(identifier='{0}-47'.format(maternal_consent.subject_identifier)))
        self.assertIsNotNone(SubjectIdentifier.objects.get(identifier='{0}-57'.format(maternal_consent.subject_identifier)))
        self.assertIsNotNone(SubjectIdentifier.objects.get(identifier='{0}-67'.format(maternal_consent.subject_identifier)))
        self.assertIsNotNone(SubjectIdentifier.objects.get(identifier='{0}-77'.format(maternal_consent.subject_identifier)))

        print "confirm sequence table is sequential"
        x = 1
        for obj in Sequence.objects.all().order_by('id'):
            self.assertEqual(obj.id, x)
            x += 1
        print 'confirm sequence was only used for maternal identifiers'
        self.assertEqual(MaternalConsent.objects.all().count(), Sequence.objects.all().count())

        print 'confirm sequence is 0 for infant identifiers based on RegisteredSubject and bhp_identifier.models.SubjectIdentifier'
        self.assertEqual(RegisteredSubject.objects.filter(relative_identifier__isnull=False).count(), SubjectIdentifier.objects.filter(sequence_number=0).count())
        print 'confirm subject_type for infants and mothers'
        self.assertEqual(RegisteredSubject.objects.filter(relative_identifier__isnull=False, subject_type__icontains='infant').count(), SubjectIdentifier.objects.filter(sequence_number=0).count())
        self.assertEqual(RegisteredSubject.objects.filter(relative_identifier__isnull=True, subject_type__icontains='maternal').count(), SubjectIdentifier.objects.exclude(sequence_number=0).count())
        print 'maternal consents'
        for rs in MaternalConsent.objects.all():
            print rs.subject_identifier, rs.subject_type
        print 'subject identifier model'
        for subject_identifier in SubjectIdentifier.objects.all():
            print subject_identifier.identifier, subject_identifier.sequence_number, subject_identifier.device_id
        print 'registered_subject'
        for rs in RegisteredSubject.objects.all():
            print rs.subject_identifier, rs.subject_type

