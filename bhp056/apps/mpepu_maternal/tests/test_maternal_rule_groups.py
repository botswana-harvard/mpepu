from django.test import TestCase
from datetime import datetime, timedelta

from edc.core.bhp_content_type_map.models import ContentTypeMap
from edc.core.bhp_variables.tests.factories import StudySiteFactory
from edc.entry_meta_data.models import ScheduledEntryMetaData
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.subject.appointment.models import Appointment
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.registration.models import RegisteredSubject
from edc.subject.visit_schedule.classes import site_visit_schedules
from edc.subject.entry.models import Entry

from apps.mpepu_lab.lab_profiles import MpepuInfantProfile
from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration

from apps.mpepu_maternal.tests.factories import (MaternalConsentFactory, MaternalEligibilityPostFactory,
                                                 MaternalVisitFactory, MaternalEnrollFactory, MaternalArvPregFactory, 
                                                 MaternalArvPostFactory, FeedingChoiceFactory)
from apps.mpepu_infant.tests.factories import (InfantBirthFactory, InfantVisitFactory, InfantEligibilityFactory, 
                                               InfantBirthDataFactory, InfantArvProphFactory, InfantFuFactory,
                                               InfantStudyDrugFactory, InfantStoolCollectionFactory)
from apps.mpepu_infant_rando.tests import InfantRandomizationTests, RandoTestHelper
from apps.mpepu_infant_rando.models import InfantRando
from apps.mpepu_maternal.models import (MaternalConsent, MaternalLabDel, MaternalEligibilityPost, FeedingChoice,
                                        MaternalEligibilityPost, MaternalVisit, MaternalEnroll, 
                                        MaternalArvPreg, MaternalArvPost)
from apps.mpepu_maternal.rule_groups import *


class MaternalRuleGroupsTests(TestCase):

    def setUp(self):
        try:
            site_lab_profiles.register(MpepuInfantProfile())
        except AlreadyRegistered:
            pass
        MpepuAppConfiguration().prepare()
        site_lab_tracker.autodiscover()
        site_visit_schedules.autodiscover()
        site_visit_schedules.build_all()
        study_site = StudySiteFactory()
        content_type_map = ContentTypeMap.objects.get(model='maternalconsent', app_label='mpepu_maternal')
        consent_catalogue = ConsentCatalogueFactory(content_type_map=content_type_map)
        consent_catalogue.add_for_app = 'mpepu_infant'
        consent_catalogue.save()

        delivery_days_ago = 20
        delivery_datetime = datetime.today() - timedelta(days=delivery_days_ago - 3)
        print "Consent a mother"
        self.maternal_consent = MaternalConsentFactory(study_site=study_site, 
                                    consent_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print "Consent: {}".format(self.maternal_consent)
        self.registered_subject = RegisteredSubject.objects.get(subject_identifier=
                                                                self.maternal_consent.subject_identifier)
        # check if mother is eligible
        self.maternal_eligibility = MaternalEligibilityPostFactory(maternal_consent=self.maternal_consent, 
                                        registered_subject=self.registered_subject, 
                                        registration_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        # get the 2000M visit
        self.m_appointment = Appointment.objects.get(registered_subject=
                                                     self.registered_subject, visit_definition__code='2000M')
        # create a maternal visit for the 2000M visit
        self.maternal_visit = MaternalVisitFactory(appointment=self.m_appointment, 
                                                   report_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        self.m_app_2010 = Appointment.objects.get(registered_subject=
                                                  self.registered_subject, visit_definition__code='2010M')
        # create a maternal visit for the 2000M visit
        self.m_visit_2010 = MaternalVisitFactory(appointment=self.m_app_2010, 
                                                 report_datetime=datetime.today() - timedelta(days=delivery_days_ago))

    def teardown(self):
        RegisteredSubject.objects.all().delete()
        MaternalConsent.objects.all().delete()
        Appointment.objects.all().delete()
        MaternalLabDel.objects.all().delete()
        MaternalEligibilityPost.objects.all().delete()
        MaternalVisit.objects.all().delete()
        MaternalEnroll.objects.all().delete()

    def test_maternal_enroll_rule_group1(self):
        """Test the that if prev_pregnancies is 0 on maternalenroll then maternalenrollob is not required"""
        print "Assert that maternalenrollob is new upon creation of a visit 2000M"
        entry = Entry.objects.get(visit_definition__code='2000M', model_name='maternalenrollob')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NEW')

        print "Assert that if previous pregnancies is indicated as 0, then MaternalEnrollOb is not required"
        maternal_enroll = MaternalEnrollFactory(maternal_visit=self.maternal_visit, prev_pregnancies=0)
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NOT_REQUIRED')

        print "Assert that if previous pregnancies is indicated > 0, then MaternalEnrollOb is not required, otherwise it is"
        maternal_enroll.prev_pregnancies=2
        maternal_enroll.save()
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NEW')

    def test_maternal_enroll_rule_group2(self):
        """Test that if previously on haart for own health is yes then maternalenrollarv is required, otherwise it is not"""
        print "Assert that MaternalEnrollArv is new upon creation of a visit 2000M"
        entry = Entry.objects.get(visit_definition__code='2000M', model_name='maternalenrollarv')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NEW')

        print "Assert that if previous pregnancies is indicated as No, then MaternalEnrollArv is not required"
        maternal_enroll = MaternalEnrollFactory(maternal_visit=self.maternal_visit, prior_health_haart='No')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NOT_REQUIRED')

        print "Assert that if previous pregnancies is indicated Yes, then MaternalEnrollArv is required"
        maternal_enroll.prior_health_haart='Yes'
        maternal_enroll.save()
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NEW')

    def test_maternal_enroll_rule_group3(self):
        """Test that if previously on haart for previous pregnancies is yes then maternalenrollarv is required, otherwise it is not"""
        print "Assert that maternalenrollclin is new upon creation of a visit 2000M"
        entry = Entry.objects.get(visit_definition__code='2000M', model_name='maternalenrollclin')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NEW')

        print "Assert that if arv for previous pregnancies is indicated as No, then maternalenrollclin is not required"
        maternal_enroll = MaternalEnrollFactory(maternal_visit=self.maternal_visit, prev_pregnancy_arv='No')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NOT_REQUIRED')

        print "Assert that if took arv for previous pregnancies is indicated Yes, then maternalenrollclin is required"
        maternal_enroll.prev_pregnancy_arv='Yes'
        maternal_enroll.save()
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NEW')

    def test_maternal_arv_preg_rule_group1(self):
        """Test that maternal arv """
        print "Assert that maternalarvpreghistory is new upon creation of a visit 2000M"
        entry = Entry.objects.get(visit_definition__code='2000M', model_name='maternalarvpreghistory')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NEW')

        print "Assert that if took arv during pregnancy is indicated as No, then maternalarvpreghistory is not required"
        maternal_arv = MaternalArvPregFactory(maternal_visit=self.maternal_visit, took_arv='No')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NOT_REQUIRED')

        print "Assert that if took arv during pregnancy is indicated Yes, then maternalarvpreghistory is required"
        maternal_arv.took_arv='Yes'
        maternal_arv.save()
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NEW')

    def test_maternal_arv_preg_rule_group2(self):
        """Test that maternal arv """
        print "Assert that maternalarvpphistory is new upon creation of a visit 2000M"
        entry = Entry.objects.get(visit_definition__code='2000M', model_name='maternalarvpphistory')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NEW')

        print "Assert that if started arv during immediate postpartum is indicated as No, then maternalarvpphistory is not required"
        maternal_arv = MaternalArvPregFactory(maternal_visit=self.maternal_visit, start_pp='No')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NOT_REQUIRED')

        print "Assert that if started arv during immediate postpartum is indicated Yes, then maternalarvpphistory is required"
        maternal_arv.start_pp='Yes'
        maternal_arv.save()
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NEW')

    def test_maternal_arv_post_rule_group(self):
        """Test that maternal arv """
        print "Assert that maternalarvpostadh is new upon creation of a visit 2010M"
        entry = Entry.objects.get(visit_definition__code='2010M', model_name='maternalarvpostadh')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.m_app_2010, entry=entry)
        self.assertEqual(meta_data.entry_status,'NEW')

        print "Assert that if was supposed to be on haart since last visit is indicated as No, then MaternalArvPostadh is not required"
        maternal_arv = MaternalArvPostFactory(maternal_visit=self.m_visit_2010, haart_last_visit='No')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.m_app_2010, entry=entry)
        self.assertEqual(meta_data.entry_status,'NOT_REQUIRED')

        print "Assert that if was supposed to be on haart since last visit is indicated Yes, then MaternalArvPostadh is required"
        maternal_arv.haart_last_visit='Yes'
        maternal_arv.save()
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.m_app_2010, entry=entry)
        self.assertEqual(meta_data.entry_status,'NEW')

    def test_maternal_feeding_choice_rule_group(self):
        """Test that maternal Feeding choice options """
        print "Assert that FeedingChoiceSectionOne is new upon creation of a visit 2000M"
        entry1 = Entry.objects.get(visit_definition__code='2000M', model_name='feedingchoicesectionone')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry1)
        self.assertEqual(meta_data.entry_status,'NEW')

        print "Assert that FeedingChoiceSectionTwo is new upon creation of a visit 2000M"
        entry2 = Entry.objects.get(visit_definition__code='2000M', model_name='feedingchoicesectiontwo')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry2)
        self.assertEqual(meta_data.entry_status,'NEW')

        print "Assert that FeedingChoiceSectionThree is new upon creation of a visit 2000M"
        entry3 = Entry.objects.get(visit_definition__code='2000M', model_name='feedingchoicesectionthree')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry3)
        self.assertEqual(meta_data.entry_status,'NEW')

        print "Assert that first time making a feeding choice is indicated as No, section 1, 2 and 3 are required"
        feeding_choice = FeedingChoiceFactory(maternal_visit=self.maternal_visit, first_time_feeding='No')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry1)
        self.assertEqual(meta_data.entry_status,'NEW')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry2)
        self.assertEqual(meta_data.entry_status,'NEW')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry3)
        self.assertEqual(meta_data.entry_status,'NEW')

        print "Assert that first time making a feeding choice is indicated as Yes, then only section 2 and 3 are required"
        feeding_choice.first_time_feeding='Yes'
        feeding_choice.save()
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry1)
        self.assertEqual(meta_data.entry_status,'NOT_REQUIRED')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry2)
        self.assertEqual(meta_data.entry_status,'NEW')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, 
                                                       appointment=self.maternal_visit.appointment, entry=entry3)
        self.assertEqual(meta_data.entry_status,'NEW')
