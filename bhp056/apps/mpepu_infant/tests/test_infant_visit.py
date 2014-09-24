from django.test import TestCase
from datetime import datetime, date, timedelta
from django.core.exceptions import ValidationError

from edc.core.bhp_content_type_map.models import ContentTypeMap
from edc.core.bhp_variables.tests.factories import StudySiteFactory
from edc.core.identifier.models import SubjectIdentifier
from edc.entry_meta_data.models import ScheduledEntryMetaData
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.subject.appointment.models import Appointment
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.subject.entry.tests.factories import EntryFactory
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.registration.models import RegisteredSubject
from edc.subject.visit_schedule.classes import site_visit_schedules
from edc.subject.entry.models import Entry

from apps.mpepu_lab.lab_profiles import MpepuInfantProfile
from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration

from apps.mpepu_maternal.tests.factories import (MaternalConsentFactory, MaternalEligibilityPostFactory,
                                                 MaternalVisitFactory, MaternalLabDelFactory)
from apps.mpepu_infant.tests.factories import (InfantBirthFactory, InfantVisitFactory, InfantEligibilityFactory)
from apps.mpepu_infant_rando.tests import InfantRandomizationTests, RandoTestHelper
from apps.mpepu_infant_rando.models import InfantRando
from apps.mpepu_infant.models import InfantVisit


class InfantVisitTests(TestCase):

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
        self.delivery_datetime = datetime.today() - timedelta(days=delivery_days_ago - 3)
        print "Consent a mother"
        self.maternal_consent = MaternalConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print "Consent: {}".format(self.maternal_consent)
        m_registered_subject = RegisteredSubject.objects.get(subject_identifier=self.maternal_consent.subject_identifier)
        print 'check if mother is eligible'
        self.maternal_eligibility = MaternalEligibilityPostFactory(maternal_consent=self.maternal_consent, registered_subject=m_registered_subject, registration_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print 'get the 2000M visit'
        self.m_appointment = Appointment.objects.get(registered_subject=m_registered_subject, visit_definition__code='2000M')
        print 'create a maternal visit for the 2000M visit'
        self.maternal_visit = MaternalVisitFactory(appointment=self.m_appointment, report_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print 'create a maternal_lab_del registering 2 of 2 infants'
        self.maternal_lab_del = MaternalLabDelFactory(maternal_visit=self.maternal_visit,
                                                         live_infants=1,
                                                         live_infants_to_register=1,
                                                         delivery_datetime=self.delivery_datetime,
                                                         has_ga='Yes',
                                                         ga=37,
                                                         )
        print 'maternal lab del: {}'.format(self.maternal_lab_del)

    def test_eligibility_required_after2000(self):
        print 'get registered subject of the infant'
        registered_subject = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'infant registered subject {}'.format(registered_subject)
        self.infant_birth = InfantBirthFactory(registered_subject=registered_subject, maternal_lab_del=self.maternal_lab_del, dob=self.delivery_datetime.date())
        print 'infant birth {}'.format(self.infant_birth)
        print 'get 2000 appointment'
        appointment_2000 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000')
        print '2000 appointment {}'.format(appointment_2000)
        infant_visit_2000 = InfantVisitFactory(appointment=appointment_2000, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy notrando')
        print '2000 infant visit {}'.format(infant_visit_2000)
        print 'get 2010 appointment'
        appointment_2010 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2010')
        print "assert that saving 2010 infant visit before saving infant eligibility fails"
        self.assertRaisesMessage(ValidationError,
            'Please complete the Infant Eligibility or Infant Pre-eligibility before conducting scheduled visits beyond visit 2000.',
            InfantVisitFactory, appointment=appointment_2010, report_datetime=datetime.today(), reason='scheduled')
 
    def test_previous_visit_required(self):
        print 'get registered subject of the infant'
        registered_subject = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'infant registered subject {}'.format(registered_subject)
        infant_birth = InfantBirthFactory(registered_subject=registered_subject, maternal_lab_del=self.maternal_lab_del, dob=self.delivery_datetime.date())
        print 'infant birth {}'.format(infant_birth)
        print 'get 2000 appointment'
        appointment_2000 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000')
        print '2000 appointment {}'.format(appointment_2000)
        infant_visit_2000 = InfantVisitFactory(appointment=appointment_2000, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy notrando')
        print '2000 infant visit {}'.format(infant_visit_2000)
        print 'get 2010 appointment'
        appointment_2010 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2010')
        print 'Infant Eligibility'
        infant_eligibility = InfantEligibilityFactory(infant_birth=infant_birth, registered_subject=registered_subject)
        print 'infant eligibility {}'.format(infant_eligibility)
        print 'assert that the rest of the visits were created'
        appointment_all = Appointment.objects.filter(registered_subject=registered_subject)
        self.assertEqual(appointment_all.count(), 9)
        print 'assert that trying to save a visit before the previous one has been filled in will fail'
        appointment_2030 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2030')
        self.assertRaises(ValidationError, InfantVisitFactory, appointment=appointment_2030)
        print 'assert that saving previous visit then re-saving the visit will save.'
        infant_visit_2010 = InfantVisitFactory(appointment=appointment_2010, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy ondrug')
        appointment_2020 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2020')
        infant_visit_2020 = InfantVisitFactory(appointment=appointment_2020, report_datetime=datetime.today(), reason='scheduled')
        infant_visit_2030 = InfantVisitFactory(appointment=appointment_2030, report_datetime=datetime.today(), reason='scheduled')
        print 'infant 2030 visit {}'.format(infant_visit_2030)
 
    def test_meta_data_status_initial_state(self):
        print 'get registered subject of the infant'
        registered_subject = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'infant registered subject {}'.format(registered_subject)
        infant_birth = InfantBirthFactory(registered_subject=registered_subject, maternal_lab_del=self.maternal_lab_del, dob=self.delivery_datetime.date())
        print 'infant birth {}'.format(infant_birth)
        print 'Infant Eligibility'
        infant_eligibility = InfantEligibilityFactory(infant_birth=infant_birth, registered_subject=registered_subject)
        print 'infant eligibility {}'.format(infant_eligibility)
 
        print 'check initial state of additional forms for visits greater than 2020'
        visits = ['2000','2010']
        forms = ['infantdeath', 'infantverbalautopsy', 'infantsurvival', 'infantoffstudy']
        for visit in visits:
            appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code=visit)
            InfantVisitFactory(appointment=appointment, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy notrando')
            for form in forms:
                print 'assert that {0} initial state is NOT_REQUIRED for a {1} visit where reason is not DEAD or LOST'.format(form, visit)
                entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
                meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=registered_subject, entry=entry)
                self.assertEqual(meta_data.entry_status, 'NOT_REQUIRED')
 
        print 'check initial state of additional forms for visits greater than 2020'
        visits = ['2020', '2030', '2060', '2090', '2120', '2150', '2180']
        forms = ['infantdeath', 'infantoffdrug', 'infantverbalautopsy', 'infantsurvival', 'infantoffstudy']
        for visit in visits:
            appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code=visit)
            iv = InfantVisitFactory(appointment=appointment, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy ondrug')
            for form in forms:
                print 'assert that {0} initial status is NOT_REQUIRED for a {1} visit where reason is not DEAD or LOST'.format(form, visit)
                entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
                meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=registered_subject, entry=entry)
                #Infantoffdrug because new at 2180 if it was not filled in at 2150
                if iv.appointment.visit_definition.code != '2180' and form !='infantoffdrug':
                    self.assertEqual(meta_data.entry_status, 'NOT_REQUIRED')
 
    def test_meta_data_status_reason_death_sid_none(self):
        print 'get registered subject of the infant'
        registered_subject = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'infant registered subject {}'.format(registered_subject)
        infant_birth = InfantBirthFactory(registered_subject=registered_subject, maternal_lab_del=self.maternal_lab_del, dob=self.delivery_datetime.date())
        print 'infant birth {}'.format(infant_birth)
 
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000')
        infant_visit = InfantVisitFactory(appointment=appointment, report_datetime=datetime.today(), reason='death', study_status = 'onstudy notrando')
        forms = ['infantdeath', 'infantprerandoloss', 'infantsurvival', 'infantverbalautopsy', 'infantoffstudy']
        for form in forms:
            print 'assert that {0} status is \'NEW\' for a 2000 visit where reason DEAD and sid is none'.format(form)
            entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
            meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=registered_subject, entry=entry)
            self.assertEqual(meta_data.entry_status, 'NEW')
 
    def test_meta_data_status_reason_death_sid_not_none(self):
        print 'get registered subject of the infant'
        registered_subject = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'infant registered subject {}'.format(registered_subject)
        infant_birth = InfantBirthFactory(registered_subject=registered_subject, maternal_lab_del=self.maternal_lab_del, dob=self.delivery_datetime.date())
        print 'infant birth {}'.format(infant_birth)
        print 'Infant Eligibility'
        infant_eligibility = InfantEligibilityFactory(
                    infant_birth=infant_birth,
                    registered_subject=infant_birth.registered_subject,
                    rando_bf_duration = 'N/A',
                    congen_anomaly = 'No',
                    maternal_art_status = 'ON',
                    maternal_feeding_choice = 'FF',
                    randomization_site = 'Gaborone',
                    ctx_contra = 'No',
                    )
        print 'infant eligibility {}'.format(infant_eligibility)
        print 'randomize infant'
        RandoTestHelper().populate_rando()
        infant_rando = InfantRando.objects.randomize(infant_eligibility=infant_eligibility)
        print 'Infant Rando {}'.format(infant_rando)

        appointment_2000 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000')
        InfantVisitFactory(appointment=appointment_2000, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy notrando')
        appointment_2010 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2010')
        InfantVisitFactory(appointment=appointment_2010, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy rando today')
        appointment_2020 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2020')
        InfantVisitFactory(appointment=appointment_2020, report_datetime=datetime.today(), reason='death', study_status = 'offstudy')

        forms = ['infantdeath', 'infantsurvival', 'infantverbalautopsy', 'infantoffstudy']
        for form in forms:
            print 'assert that {0} status is \'NEW\' for a visit where visit is dead and sid is not none'.format(form)
            entry = Entry.objects.get(model_name=form, visit_definition_id=appointment_2020.visit_definition_id)
            meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment_2020, registered_subject=registered_subject, entry=entry)
            self.assertEqual(meta_data.entry_status, 'NEW')

    def test_meta_data_status_reason_lost_sid_none(self):
        print 'get registered subject of the infant'
        registered_subject = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'infant registered subject {}'.format(registered_subject)
        infant_birth = InfantBirthFactory(registered_subject=registered_subject, maternal_lab_del=self.maternal_lab_del, dob=self.delivery_datetime.date())
        print 'infant birth {}'.format(infant_birth)

        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000')
        infant_visit = InfantVisitFactory(appointment=appointment, report_datetime=datetime.today(), reason='lost', study_status = 'onstudy notrando')
        forms = ['infantprerandoloss', 'infantoffstudy']
        for form in forms:
            print 'assert that {0} status is \'NEW\' for a 2000 visit where reason LOST and sid is none'.format(form)
            entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
            meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=registered_subject, entry=entry)
            self.assertEqual(meta_data.entry_status, 'NEW')

    def test_meta_data_status_reason_lost_sid_not_none(self):
        print 'get registered subject of the infant'
        registered_subject = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'infant registered subject {}'.format(registered_subject)
        infant_birth = InfantBirthFactory(registered_subject=registered_subject, maternal_lab_del=self.maternal_lab_del, dob=self.delivery_datetime.date())
        print 'infant birth {}'.format(infant_birth)
        print 'Infant Eligibility'
        infant_eligibility = InfantEligibilityFactory(
                    infant_birth=infant_birth,
                    registered_subject=infant_birth.registered_subject,
                    rando_bf_duration = 'N/A',
                    congen_anomaly = 'No',
                    maternal_art_status = 'ON',
                    maternal_feeding_choice = 'FF',
                    randomization_site = 'Gaborone',
                    ctx_contra = 'No',
                    )
        print 'infant eligibility {}'.format(infant_eligibility)
        print 'randomize infant'
        RandoTestHelper().populate_rando()
        infant_rando = InfantRando.objects.randomize(infant_eligibility=infant_eligibility)
        print 'Infant Rando {}'.format(infant_rando)

        appointment_2000 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000')
        InfantVisitFactory(appointment=appointment_2000, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy notrando')
        appointment_2010 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2010')
        InfantVisitFactory(appointment=appointment_2010, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy rando today')
        appointment_2020 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2020')
        InfantVisitFactory(appointment=appointment_2020, report_datetime=datetime.today(), reason='lost', study_status = 'offstudy')

        forms = ['infantoffdrug', 'infantoffstudy']
        for form in forms:
            print 'assert that {0} status is \'NEW\' for a visit where visit is \'lost\' and sid is not none'.format(form)
            entry = Entry.objects.get(model_name=form, visit_definition_id=appointment_2020.visit_definition_id)
            meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment_2020, registered_subject=registered_subject, entry=entry)
            self.assertEqual(meta_data.entry_status, 'NEW')

    def test_meta_data_status_study_status_onstudy_rando_offdrug(self):
        print 'get registered subject of the infant'
        registered_subject = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'infant registered subject {}'.format(registered_subject)
        infant_birth = InfantBirthFactory(registered_subject=registered_subject, maternal_lab_del=self.maternal_lab_del, dob=self.delivery_datetime.date())
        print 'infant birth {}'.format(infant_birth)
        print 'Infant Eligibility'
        infant_eligibility = InfantEligibilityFactory(
                    infant_birth=infant_birth,
                    registered_subject=infant_birth.registered_subject,
                    rando_bf_duration = 'N/A',
                    congen_anomaly = 'No',
                    maternal_art_status = 'ON',
                    maternal_feeding_choice = 'FF',
                    randomization_site = 'Gaborone',
                    ctx_contra = 'No',
                    )
        print 'infant eligibility {}'.format(infant_eligibility)
        print 'randomize infant'
        RandoTestHelper().populate_rando()
        infant_rando = InfantRando.objects.randomize(infant_eligibility=infant_eligibility)
        print 'Infant Rando {}'.format(infant_rando)

        appointment_2000 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000')
        InfantVisitFactory(appointment=appointment_2000, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy notrando')
        appointment_2010 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2010')
        InfantVisitFactory(appointment=appointment_2010, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy rando today')
        appointment_2020 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2020')
        infant_visit = InfantVisitFactory(appointment=appointment_2020, report_datetime=datetime.today())
        infant_visit.study_status='onstudy rando offdrug'
        infant_visit.change_meta_data_status_if_study_status_is_onstudy_rando_offdrug()

        form = 'infantoffdrug'
        print 'assert that {0} status is \'NEW\' for a visit where visit study_status is \'onstudy rando offdrug\' and sid is not none'.format(form)
        entry = Entry.objects.get(model_name=form, visit_definition_id=appointment_2020.visit_definition_id)
        meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment_2020, registered_subject=registered_subject, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')

    def test_meta_data_status_reason_offstudy(self):
        print 'get registered subject of the infant'
        registered_subject = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'infant registered subject {}'.format(registered_subject)
        infant_birth = InfantBirthFactory(registered_subject=registered_subject, maternal_lab_del=self.maternal_lab_del, dob=self.delivery_datetime.date())
        print 'infant birth {}'.format(infant_birth)
        print 'Infant Eligibility'
        infant_eligibility = InfantEligibilityFactory(
                    infant_birth=infant_birth,
                    registered_subject=infant_birth.registered_subject,
                    rando_bf_duration = 'N/A',
                    congen_anomaly = 'No',
                    maternal_art_status = 'ON',
                    maternal_feeding_choice = 'FF',
                    randomization_site = 'Gaborone',
                    ctx_contra = 'No',
                    )
        print 'infant eligibility {}'.format(infant_eligibility)
        print 'randomize infant'
        RandoTestHelper().populate_rando()
        infant_rando = InfantRando.objects.randomize(infant_eligibility=infant_eligibility)
        print 'Infant Rando {}'.format(infant_rando)

        appointment_2000 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000')
        InfantVisitFactory(appointment=appointment_2000, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy notrando')
        appointment_2010 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2010')
        InfantVisitFactory(appointment=appointment_2010, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy rando today')
        appointment_2020 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2020')
        infant_visit = InfantVisitFactory(appointment=appointment_2020, report_datetime=datetime.today())
        infant_visit.reason='off study'
        infant_visit.change_meta_data_status_if_visit_reason_is_off_study()
 
        form = 'infantoffstudy'
        print 'assert that {0} status is \'NEW\' for a visit where visit reason is \'off study\'.'.format(form)
        entry = Entry.objects.get(model_name=form, visit_definition_id=appointment_2020.visit_definition_id)
        meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment_2020, registered_subject=registered_subject, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')
 
    def test_meta_data_status_info_source_telephone(self):
        print 'get registered subject of the infant'
        registered_subject = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'infant registered subject {}'.format(registered_subject)
        infant_birth = InfantBirthFactory(registered_subject=registered_subject, maternal_lab_del=self.maternal_lab_del, dob=self.delivery_datetime.date())
        print 'infant birth {}'.format(infant_birth)
        print 'Infant Eligibility'
        infant_eligibility = InfantEligibilityFactory(
                    infant_birth=infant_birth,
                    registered_subject=infant_birth.registered_subject,
                    rando_bf_duration = 'N/A',
                    congen_anomaly = 'No',
                    maternal_art_status = 'ON',
                    maternal_feeding_choice = 'FF',
                    randomization_site = 'Gaborone',
                    ctx_contra = 'No',
                    )
        print 'infant eligibility {}'.format(infant_eligibility)
        print 'randomize infant'
        RandoTestHelper().populate_rando()
        infant_rando = InfantRando.objects.randomize(infant_eligibility=infant_eligibility)
        print 'Infant Rando {}'.format(infant_rando)

        appointment_2000 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000')
        InfantVisitFactory(appointment=appointment_2000, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy notrando')
        appointment_2010 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2010')
        InfantVisitFactory(appointment=appointment_2010, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy rando today')
        appointment_2020 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2020')
        infant_visit = InfantVisitFactory(appointment=appointment_2020, report_datetime=datetime.today())

        infant_visit.info_source='telephone'
        infant_visit.change_meta_data_status_if_info_source_is_telephone()

        forms = ['infantfu', 'infantfuphysical', 'infantfud', 'infantfudx', 'infantfudx2proph', 'infantfunewmed', 'infantfumed']
        for form in forms:
            print 'assert that {0} status is \'NOT_REQUIRED\' for a visit where info_source is \'Telephone\''.format(form)
            entry = Entry.objects.get(model_name=form, visit_definition_id=appointment_2020.visit_definition_id)
            meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment_2020, registered_subject=infant_birth.registered_subject, entry=entry)
            self.assertEqual(meta_data.entry_status, 'NOT_REQUIRED')
