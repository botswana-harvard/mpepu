from datetime import datetime, date, timedelta
from django.test import TestCase

from edc.core.bhp_variables.tests.factories import StudySiteFactory
from edc.entry_meta_data.models import ScheduledEntryMetaData
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.subject.appointment.models import Appointment
from edc.subject.entry.models import Entry
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.visit_schedule.classes import site_visit_schedules

from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration
from apps.mpepu_lab.lab_profiles import MpepuMaternalProfile
from apps.mpepu_maternal.forms import MaternalEligibilityPostForm, MaternalEligibilityAnteForm, MaternalConsentForm
from apps.mpepu_maternal.models import MaternalConsent, MaternalVisit, MaternalEligibilityPost
from apps.mpepu_maternal.visit_schedule import MpepuMaternalPostNatalVisitSchedule, MpepuMaternalAnteNatalVisitSchedule, MpepuMaternalPostPartumVisitSchedule

from .factories import( MaternalConsentFactory, MaternalEligibilityPostFactory, MaternalEligibilityAnteFactory, MaternalPostRegFactory,
                        MaternalVisitFactory, MaternalLabDelFactory, MaternalPostFuFactory)


class MaternalMetaDataTests(TestCase):
    def setUp(self):
        try:
            site_lab_profiles.register(MpepuMaternalProfile())
        except AlreadyRegistered:
            pass
        MpepuAppConfiguration()
        site_lab_tracker.autodiscover()
        site_visit_schedules.autodiscover()
        site_visit_schedules.build_all()
        study_site = StudySiteFactory()
        print "Consenting a mother"
        MaternalConsent.objects.all().delete()
        self.maternal_consent1 = MaternalConsentFactory(study_site=study_site)
        print "Maternal Consent: {}".format(self.maternal_consent1)
        print "check if mother is eligible"
        self.post_elibility1 = MaternalEligibilityPostFactory(maternal_consent=self.maternal_consent1, registered_subject=self.maternal_consent1.registered_subject)
        print "Consent second mother"
        self.maternal_consent2 = MaternalConsentFactory(study_site=study_site)
        print "Maternal Consent: {}".format(self.maternal_consent2)
        print "check if mother is eligible"
        self.post_elibility2 = MaternalEligibilityPostFactory(maternal_consent=self.maternal_consent2, registered_subject=self.maternal_consent2.registered_subject)
        print "Consent third mother"
        self.maternal_consent3 = MaternalConsentFactory(study_site=study_site)
        print "Maternal Consent: {}".format(self.maternal_consent3)
        print "check if mother is eligible"
        self.post_elibility3 = MaternalEligibilityPostFactory(maternal_consent=self.maternal_consent3, registered_subject=self.maternal_consent3.registered_subject)

    def test_meta_data_same_bid_diff_already_created_visits(self):
        form = 'maternalpostfu'
        visits = ['2010M','2020M','2030M', '2060M','2090M','2120M','2150M','2180M']
        for visit in visits:
            appointment = Appointment.objects.get(registered_subject=self.maternal_consent1.registered_subject,visit_definition__code=visit)
            visit = MaternalVisitFactory(appointment=appointment)
            print 'assert that {} entry status is NEW for visit {}'.format(form, visit)
            entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
            meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=self.maternal_consent1.registered_subject, entry=entry)
            self.assertEqual(meta_data.entry_status, 'NEW')

        print 'key maternal post natal followup for 2020'
        app_2020 = Appointment.objects.get(registered_subject=self.maternal_consent1.registered_subject,visit_definition__code='2020M')
        visit_2020 = MaternalVisit.objects.get(appointment=app_2020)
        maternal_post_fu = MaternalPostFuFactory(maternal_visit=visit_2020)
        print 'Maternal Post Fu {}'.format(maternal_post_fu)

        for visit in visits:
            appointment = Appointment.objects.get(registered_subject=self.maternal_consent1.registered_subject,visit_definition__code=visit)
            visit = MaternalVisit.objects.get(appointment=appointment)
            entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
            meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=self.maternal_consent1.registered_subject, entry=entry)
            if appointment.visit_definition.code=='2020M':
                print 'assert that {} entry status is KEYED for visit {}'.format(form, visit)
                self.assertEqual(meta_data.entry_status, 'KEYED')
            else:
                print 'assert that {} entry status is NEW for visit {}'.format(form, visit)
                self.assertEqual(meta_data.entry_status, 'NEW')

    def test_meta_data_same_bid_diff_visit(self):
        form = 'maternalpostfu'

        app_2010 =Appointment.objects.get(registered_subject=self.maternal_consent1.registered_subject,visit_definition__code='2010M')
        visit_2010 = MaternalVisitFactory(appointment=app_2010)
        print 'assert that maternalpostfu entry status is NEW for for 2010M visit'
        entry = Entry.objects.get(model_name=form, visit_definition_id=app_2010.visit_definition_id)
        meta_data = ScheduledEntryMetaData.objects.get(appointment=app_2010, registered_subject=self.maternal_consent1.registered_subject, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')
        print 'key maternal post natal followup for 2010'
        app_2010 = Appointment.objects.get(registered_subject=self.maternal_consent1.registered_subject,visit_definition__code='2010M')
        visit_2010 = MaternalVisit.objects.get(appointment=app_2010)
        maternal_post_fu = MaternalPostFuFactory(maternal_visit=visit_2010)
        print 'assert that maternalpostfu entry status is now KEYED for for 2010M visit'
        entry = Entry.objects.get(model_name=form, visit_definition_id=app_2010.visit_definition_id)
        meta_data = ScheduledEntryMetaData.objects.get(appointment=app_2010, registered_subject=self.maternal_consent1.registered_subject, entry=entry)
        self.assertEqual(meta_data.entry_status, 'KEYED')
        print 'Maternal Post Fu {}'.format(maternal_post_fu)
        visits = ['2020M','2030M', '2060M','2090M','2120M','2150M','2180M']
        for visit in visits:
            appointment = Appointment.objects.get(registered_subject=self.maternal_consent1.registered_subject,visit_definition__code=visit)
            visit = MaternalVisitFactory(appointment=appointment)
            entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
            meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=self.maternal_consent1.registered_subject, entry=entry)
            if appointment.visit_definition.code=='2010M':
                print 'assert that {} entry status is KEYED for visit {}'.format(form, visit)
                self.assertEqual(meta_data.entry_status, 'KEYED')
            else:
                print 'assert that {} entry status is NEW for visit {}'.format(form, visit)
                self.assertEqual(meta_data.entry_status, 'NEW')

    def test_meta_data_diff_bid_same_form_same_visit(self):
        delivery_days_ago = 20
        delivery_datetime = datetime.today() - timedelta(days=delivery_days_ago - 3)
        form = 'maternallabdel'
        print "fill first mothers visit"
        m1_app_2000 = Appointment.objects.get(registered_subject=self.maternal_consent1.registered_subject,visit_definition__code='2000M')
        m1_visit_2000 = MaternalVisitFactory(appointment=m1_app_2000)
        print 'assert that maternallabdel entry stataus is NEW for first mother'
        entry = Entry.objects.get(model_name=form, visit_definition_id=m1_app_2000.visit_definition_id)
        meta_data = ScheduledEntryMetaData.objects.get(appointment=m1_app_2000, registered_subject=self.maternal_consent1.registered_subject, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')
        m1_maternal_lab_del = MaternalLabDelFactory(maternal_visit=m1_visit_2000,
                                                         live_infants=1,
                                                         live_infants_to_register=1,
                                                         delivery_datetime=delivery_datetime,
                                                         has_ga='Yes',
                                                         ga=37,
                                                         )
        print 'assert that maternallabdel entry status is now KEYED for first mother'
        entry = Entry.objects.get(model_name=form, visit_definition_id=m1_app_2000.visit_definition_id)
        meta_data = ScheduledEntryMetaData.objects.get(appointment=m1_app_2000, registered_subject=self.maternal_consent1.registered_subject, entry=entry)
        self.assertEqual(meta_data.entry_status, 'KEYED')
 
        print "fill in second mothers visit"
        m2_app_2000 = Appointment.objects.get(registered_subject=self.maternal_consent2.registered_subject,visit_definition__code='2000M')
        m2_visit_2000 = MaternalVisitFactory(appointment=m2_app_2000)
        print 'assert that maternallabdel entry stataus is NEW for second mother'
        entry = Entry.objects.get(model_name=form, visit_definition_id=m2_app_2000.visit_definition_id)
        meta_data = ScheduledEntryMetaData.objects.get(appointment=m2_app_2000, registered_subject=self.maternal_consent2.registered_subject, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')
        m2_maternal_lab_del = MaternalLabDelFactory(maternal_visit=m2_visit_2000,
                                                         live_infants=1,
                                                         live_infants_to_register=1,
                                                         delivery_datetime=delivery_datetime,
                                                         has_ga='Yes',
                                                         ga=37,
                                                         )
        print 'assert that entry status is now KEYED for second mother'
        entry = Entry.objects.get(model_name=form, visit_definition_id=m2_app_2000.visit_definition_id)
        meta_data = ScheduledEntryMetaData.objects.get(appointment=m2_app_2000, registered_subject=self.maternal_consent2.registered_subject, entry=entry)
        self.assertEqual(meta_data.entry_status, 'KEYED')
 
        print "fill in third mothers visit"
        m3_app_2000 = Appointment.objects.get(registered_subject=self.maternal_consent3.registered_subject,visit_definition__code='2000M')
        m3_visit_2000 = MaternalVisitFactory(appointment=m3_app_2000)
        print 'assert that maternallabdel entry stataus is NEW for second mother'
        entry = Entry.objects.get(model_name=form, visit_definition_id=m3_app_2000.visit_definition_id)
        meta_data = ScheduledEntryMetaData.objects.get(appointment=m3_app_2000, registered_subject=self.maternal_consent3.registered_subject, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')
        m3_maternal_lab_del = MaternalLabDelFactory(maternal_visit=m3_visit_2000,
                                                         live_infants=1,
                                                         live_infants_to_register=1,
                                                         delivery_datetime=delivery_datetime,
                                                         has_ga='Yes',
                                                         ga=37,
                                                         )
        print 'assert that entry status is now KEYED for second mother'
        entry = Entry.objects.get(model_name=form, visit_definition_id=m3_app_2000.visit_definition_id)
        meta_data = ScheduledEntryMetaData.objects.get(appointment=m3_app_2000, registered_subject=self.maternal_consent3.registered_subject, entry=entry)
        self.assertEqual(meta_data.entry_status, 'KEYED')

