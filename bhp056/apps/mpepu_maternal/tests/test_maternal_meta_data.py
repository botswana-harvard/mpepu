from datetime import datetime, date, timedelta
from django.test import TestCase

from edc.core.bhp_variables.tests.factories import StudySiteFactory
from edc.entry_meta_data.models import ScheduledEntryMetaData
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.subject.appointment.models import Appointment
from edc.subject.entry.models import Entry
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.registration.models import RegisteredSubject
from edc.subject.visit_schedule.classes import site_visit_schedules

from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration
from apps.mpepu_lab.lab_profiles import MpepuMaternalProfile
from apps.mpepu_maternal.models import MaternalConsent, MaternalVisit, MaternalEligibilityPost
from apps.mpepu_maternal.visit_schedule import MpepuMaternalPostNatalVisitSchedule, MpepuMaternalAnteNatalVisitSchedule, MpepuMaternalPostPartumVisitSchedule

from .factories import( MaternalConsentFactory, MaternalEligibilityPostFactory, MaternalEligibilityAnteFactory, MaternalPostRegFactory,
                        MaternalVisitFactory, MaternalLabDelFactory, MaternalPostFuFactory, MaternalArvPostFactory, MaternalPostFuDxFactory,
                        MaternalArvPostAdhFactory)


class MaternalMetaDataTests(TestCase):
    def setUp(self):
        try:
            site_lab_profiles.register(MpepuMaternalProfile())
        except AlreadyRegistered:
            pass
        MpepuAppConfiguration().prepare()
        site_lab_tracker.autodiscover()
        site_visit_schedules.autodiscover()
        site_visit_schedules.build_all()
        study_site = StudySiteFactory()
        MaternalConsent.objects.all().delete()
        self.maternal_consent1 = MaternalConsentFactory(study_site=study_site)
        print "Maternal Consent: {}".format(self.maternal_consent1)
        self.registered_subject1 = RegisteredSubject.objects.get(subject_identifier=self.maternal_consent1.subject_identifier)
        self.post_elibility1 = MaternalEligibilityPostFactory(maternal_consent=self.maternal_consent1, registered_subject=self.registered_subject1)
        self.maternal_consent2 = MaternalConsentFactory(study_site=study_site)
        print "Maternal Consent: {}".format(self.maternal_consent2)
        self.registered_subject2 = RegisteredSubject.objects.get(subject_identifier=self.maternal_consent2.subject_identifier)
        self.post_elibility2 = MaternalEligibilityPostFactory(maternal_consent=self.maternal_consent2, registered_subject=self.registered_subject2)
        self.maternal_consent3 = MaternalConsentFactory(study_site=study_site)
        print "Maternal Consent: {}".format(self.maternal_consent3)
        self.registered_subject3 = RegisteredSubject.objects.get(subject_identifier=self.maternal_consent3.subject_identifier)
        self.post_elibility3 = MaternalEligibilityPostFactory(maternal_consent=self.maternal_consent3, registered_subject=self.registered_subject3)

    def test_registration_forms_status(self):
        print """Assert that entry status is New for registration forms upon creation"""
        forms = ['maternalenroll', 'maternalenrolldem', 'maternalenrollmed', 'maternalenrollob', 'maternalenrollclin', 'maternalenrollarv', 
                 'maternalarvpreg', 'maternalarvpreghistory', 'maternalarvpphistory', 'maternallabdel', 'maternallabdelmed', 'maternallabdeldx',
                 'maternallabdelclinic', 'maternallocator', 'feedingchoice', 'feedingchoicesectionone', 'feedingchoicesectiontwo', 'feedingchoicesectionthree']
        appointment = Appointment.objects.get(registered_subject=self.registered_subject1,visit_definition__code='2000M')
        visit = MaternalVisitFactory(appointment=appointment)
        for form in forms:
            print 'assert that {} entry status is NEW for visit {}'.format(form, visit)
            entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
            meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=self.registered_subject1, entry=entry)
            self.assertEqual(meta_data.entry_status, 'NEW')

    def test_postpartum_forms_status(self):
        print """Assert that entry status is New for  post partum forms upon creation for all visits"""
        forms = ['maternalpostfu', 'maternalpostfudx', 'maternalarvpost', 'maternalarvpostadh']
        visits = ['2010M','2020M','2030M', '2060M','2090M','2120M','2150M','2180M']
        for visit in visits:
            appointment = Appointment.objects.get(registered_subject=self.registered_subject1,visit_definition__code=visit)
            visit = MaternalVisitFactory(appointment=appointment)
            for form in forms:
                print 'assert that {} entry status is NEW for visit {}'.format(form, visit)
                entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
                meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=self.registered_subject1, entry=entry)
                self.assertEqual(meta_data.entry_status, 'NEW')

    def test_additional_forms_status(self):
        print """Assert that entry status is NOT REQUIRED for additional forms upon creation for all visits"""
        forms = ['maternaldeath', 'maternaloffstudy']
        visits = ['2000M', '2010M','2020M','2030M', '2060M','2090M','2120M','2150M','2180M']
        for visit in visits:
            appointment = Appointment.objects.get(registered_subject=self.registered_subject1,visit_definition__code=visit)
            visit = MaternalVisitFactory(appointment=appointment)
            for form in forms:
                print 'assert that {} entry status is NOT_REQUIRED for visit {}'.format(form, visit)
                entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
                meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=self.registered_subject1, entry=entry)
                if visit.appointment.visit_definition.code != '2180' and form != 'maternaloffstudy':
                    self.assertEqual(meta_data.entry_status, 'NOT_REQUIRED')

    def test_status_after_keying(self):
        print """Assert that entry status is KEYED for postpartum visits after model has been saved"""
        forms = ['maternalpostfu', 'maternalpostfudx', 'maternalarvpost', 'maternalarvpostadh']
        visits = ['2010M','2020M','2030M', '2060M','2090M','2120M','2150M','2180M']
        for visit in visits:
            appointment = Appointment.objects.get(registered_subject=self.registered_subject1,visit_definition__code=visit)
            visit = MaternalVisitFactory(appointment=appointment)
            maternal_post_fu=MaternalPostFuFactory(maternal_visit=visit)
            MaternalPostFuDxFactory(maternal_post_fu=maternal_post_fu, maternal_visit=visit)
            maternal_arv_post=MaternalArvPostFactory(maternal_visit=visit)
            MaternalArvPostAdhFactory(maternal_arv_post=maternal_arv_post, maternal_visit=visit)
            for form in forms:
                print 'assert that {} entry status is KEYED for visit {}'.format(form, visit)
                entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
                meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=self.registered_subject1, entry=entry)
                self.assertEqual(meta_data.entry_status, 'KEYED')

    def test_status_on_update_existing_meta_data(self):
        print 'Assert that updating metadata for one model, will not affect existing metadata for same model but different visits.'
        form = 'maternalpostfu'
        visits = ['2010M','2020M','2030M', '2060M','2090M','2120M','2150M','2180M']
        for visit in visits:
            appointment = Appointment.objects.get(registered_subject=self.registered_subject1,visit_definition__code=visit)
            visit = MaternalVisitFactory(appointment=appointment)
        app_2020 = Appointment.objects.get(registered_subject=self.registered_subject1,visit_definition__code='2020M')
        visit_2020 = MaternalVisit.objects.get(appointment=app_2020)
        maternal_post_fu = MaternalPostFuFactory(maternal_visit=visit_2020)
        for visit in visits:
            appointment = Appointment.objects.get(registered_subject=self.registered_subject1,visit_definition__code=visit)
            visit = MaternalVisit.objects.get(appointment=appointment)
            entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
            meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=self.registered_subject1, entry=entry)
            if appointment.visit_definition.code=='2020M':
                print 'assert that {} entry status is KEYED for visit {}'.format(form, visit)
                self.assertEqual(meta_data.entry_status, 'KEYED')
            else:
                print 'assert that {} entry status is NEW for visit {}'.format(form, visit)
                self.assertEqual(meta_data.entry_status, 'NEW')
 
    def test_status_on_update_create_meta_data(self):
        print """Assert that updating meta data for one model, will not affect created metadata for same model but different visits"""
        form = 'maternalpostfu'
        app_2010 =Appointment.objects.get(registered_subject=self.registered_subject1,visit_definition__code='2010M')
        visit_2010 = MaternalVisitFactory(appointment=app_2010)
        maternal_post_fu = MaternalPostFuFactory(maternal_visit=visit_2010)
        visits = ['2020M', '2030M', '2060M', '2090M', '2120M','2150M', '2180M']
        for visit in visits:
            appointment = Appointment.objects.get(registered_subject=self.registered_subject1,visit_definition__code=visit)
            visit = MaternalVisitFactory(appointment=appointment)
            entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
            meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=self.registered_subject1, entry=entry)
            print 'assert that {} entry status is NEW for visit {}'.format(form, visit)
            self.assertEqual(meta_data.entry_status, 'NEW')

    def test_status_on_update_diff_bid_same_form_same_visit(self):
        print """Assert that updating meta data for one model, will not affect creating metadata for same model, same visit, different bids """
        delivery_days_ago = 20
        delivery_datetime = datetime.today() - timedelta(days=delivery_days_ago - 3)
        form = 'maternallabdel'
        m1_app_2000 = Appointment.objects.get(registered_subject=self.registered_subject1,visit_definition__code='2000M')
        m1_visit_2000 = MaternalVisitFactory(appointment=m1_app_2000)
        m1_maternal_lab_del = MaternalLabDelFactory(maternal_visit=m1_visit_2000,
                                                         live_infants=1,
                                                         live_infants_to_register=1,
                                                         delivery_datetime=delivery_datetime,
                                                         has_ga='Yes',
                                                         ga=37,
                                                         )

        m2_app_2000 = Appointment.objects.get(registered_subject=self.registered_subject2,visit_definition__code='2000M')
        m2_visit_2000 = MaternalVisitFactory(appointment=m2_app_2000)
        print 'assert that maternallabdel entry stataus is NEW for second mother'
        entry = Entry.objects.get(model_name=form, visit_definition_id=m2_app_2000.visit_definition_id)
        meta_data = ScheduledEntryMetaData.objects.get(appointment=m2_app_2000, registered_subject=self.registered_subject2, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')
