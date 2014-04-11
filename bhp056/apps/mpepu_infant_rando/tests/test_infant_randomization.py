from datetime import datetime, timedelta, date
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.visit_schedule.classes import site_visit_schedules
from edc.core.bhp_variables.tests.factories import StudySiteFactory
from edc.core.bhp_content_type_map.models import ContentTypeMap
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.subject.appointment.models import Appointment
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.subject.registration.models import RegisteredSubject

from apps.mpepu_lab.lab_profiles import MpepuInfantProfile
from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration
from apps.mpepu_maternal.tests.factories import (MaternalConsentFactory, MaternalEligibilityPostFactory,
                                                 MaternalVisitFactory, MaternalLabDelFactory)
from apps.mpepu_infant.tests.factories import InfantBirthFactory, InfantVisitFactory, InfantEligibilityFactory
from apps.mpepu_infant.forms import InfantEligibilityForm
from apps.mpepu_maternal.models import MaternalConsent, MaternalLabDel, MaternalEligibilityPost, MaternalVisit
from apps.mpepu_infant.models import InfantBirth, InfantVisit

from ..models import InfantRando
from ..classes import Eligibility


class InfantRandomizationTests(TestCase):
    def setUp(self):
        try:
            site_lab_profiles.register(MpepuInfantProfile())
        except AlreadyRegistered:
            pass
        MpepuAppConfiguration()
        site_lab_tracker.autodiscover()
        site_visit_schedules.autodiscover()
        site_visit_schedules.build_all()
        admin.autodiscover()
        study_site = StudySiteFactory(site_code=2)
        content_type_map = ContentTypeMap.objects.get(model='maternalconsent', app_label='mpepu_maternal')
        consent_catalogue = ConsentCatalogueFactory(content_type_map=content_type_map)
        consent_catalogue.add_for_app = 'mpepu_infant'
        consent_catalogue.save()

        self.delivery_days_ago = 20
        self.delivery_datetime = datetime.today() - timedelta(days=self.delivery_days_ago - 3)
        print "Consent a mother"
        self.maternal_consent = MaternalConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=self.delivery_days_ago))
        print "Consent: {}".format(self.maternal_consent)
        registered_subject = RegisteredSubject.objects.get(subject_identifier=self.maternal_consent.subject_identifier)
        print 'check if mother is eligible'
        maternal_eligibility = MaternalEligibilityPostFactory(maternal_consent=self.maternal_consent, registered_subject=registered_subject, registration_datetime=datetime.today() - timedelta(days=self.delivery_days_ago))
        print 'get the 2000M visit'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000M')
        print 'create a maternal visit for the 2000M visit'
        maternal_visit = MaternalVisitFactory(appointment=appointment, report_datetime=datetime.today() - timedelta(days=self.delivery_days_ago))
        print 'create a maternal_lab_del registering 2 of 2 infants'
        self.maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit,
                                                         live_infants=2,
                                                         live_infants_to_register=2,
                                                         delivery_datetime=self.delivery_datetime,
                                                         has_ga='Yes',
                                                         ga=37,

                                                         )
        print 'maternal lab del: {}'.format(self.maternal_lab_del)
        print 'get registered subject of the first infant'
        self.registered_subject1 = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'first registered subject {}'.format(self.registered_subject1)
        self.infant_birth1 = InfantBirthFactory(registered_subject=self.registered_subject1, maternal_lab_del=self.maternal_lab_del, dob=self.delivery_datetime.date())
        print 'first infant birth {}'.format(self.infant_birth1)
        appointment1 = Appointment.objects.get(registered_subject=self.registered_subject1, visit_definition__code='2000')
        infant_visit1 = InfantVisitFactory(appointment=appointment1, report_datetime=datetime.today(), reason='scheduled')
        print 'get registered subject of the second infant'
        self.registered_subject2 = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[1]
        print 'second registered subject {}'.format(self.registered_subject2)
        self.infant_birth2 = InfantBirthFactory(registered_subject=self.registered_subject2, maternal_lab_del=self.maternal_lab_del, dob=self.delivery_datetime.date())
        print 'second infant birth {}'.format(self.infant_birth2)
        appointment2 = Appointment.objects.get(registered_subject=self.registered_subject2, visit_definition__code='2000')
        infant_visit2 = InfantVisitFactory(appointment=appointment2, report_datetime=datetime.today(), reason='scheduled')

    def teardown(self):
        RegisteredSubject.objects.all().delete()
        MaternalConsent.objects.all().delete()
        InfantBirth.objects.all().delete()
        InfantVisit.objects.all().delete()
        Appointment.objects.all().delete()
        MaternalLabDel.objects.all().delete()
        MaternalEligibilityPost.objects.all().delete()
        MaternalVisit.objects.all().delete()

    def test_multiple_birth_rando(self):

        original_sids = self.populate_rando()

        print "assert that infant 1 is eligible to be randomised"
        allow_rando1 = Eligibility().check(
                current_consent_version=2,
                dob=self.delivery_datetime.date(),
                ga=37,
                weight=4,
                clinical_jaundice='No',
                anemia_neutropenia='No',
                exception_cls=ValidationError,
                suppress_exception=False)
        self.assertTrue(allow_rando1, "Infant Cannot be randomized")
        infant_eligibility1 = InfantEligibilityFactory(
                    infant_birth=self.infant_birth1,
                    registered_subject=self.infant_birth1.registered_subject,
                    rando_bf_duration = 'N/A',
                    congen_anomaly = 'No',
                    maternal_art_status = 'ON',
                    maternal_feeding_choice = 'FF',
                    randomization_site = 'Gaborone',
                    ctx_contra = 'No',
                    )
        print 'Infant Eligibility {}'.format(infant_eligibility1)
        print 'assert that the rest of the appointments were created, i.e. 2000,2010,2020,2030,2060,2090,2120,2150,2180'
        all_appointments = Appointment.objects.filter(registered_subject=self.registered_subject1)
        self.assertEqual(all_appointments.count(), 9)
        print 'confirm infant 1 was randomized'
        print InfantRando.objects.randomize(infant_eligibility=infant_eligibility1)
        print "Infant 1 Rando {}".format(InfantRando.objects.get(subject_identifier=self.registered_subject1.subject_identifier))
        print "assert that infant 2 is eligible to be randomised"
        allow_rando2 = Eligibility().check(
                current_consent_version=2,
                dob=self.delivery_datetime.date(),
                ga=37,
                weight=3.9,
                clinical_jaundice='No',
                anemia_neutropenia='No',
                exception_cls=ValidationError,
                suppress_exception=False)
        self.assertTrue(allow_rando2, "Infant Cannot be randomized")
        infant_eligibility2 = InfantEligibilityFactory(
                    infant_birth=self.infant_birth2,
                    registered_subject=self.infant_birth2.registered_subject,
                    rando_bf_duration = 'No',
                    congen_anomaly = 'No',
                    maternal_art_status = 'ON',
                    maternal_feeding_choice = 'BF',
                    randomization_site = 'Molepolole',
                    ctx_contra = 'No',
                    )
        print infant_eligibility2
        print 'assert that the rest of the appointments were created, i.e. 2000,2010,2020,2030,2060,2090,2120,2150,2180'
        all_appointments = Appointment.objects.filter(registered_subject=self.registered_subject2)
        self.assertEqual(all_appointments.count(), 9)
        print 'confirm infant 2 was randomized'
        InfantRando.objects.randomize(infant_eligibility=infant_eligibility2)
        print "Inafnt 2 Rando {}".format(InfantRando.objects.get(subject_identifier=self.registered_subject2.subject_identifier))
        rando1 = InfantRando.objects.get(subject_identifier=self.registered_subject1.subject_identifier)
        rando2 = InfantRando.objects.get(subject_identifier=self.registered_subject1.subject_identifier)
        print "assert that the twins were randomized to the same feeding arm"
        self.assertEquals(rando1.feeding_choice, rando2.feeding_choice)
        print "assert that the twins were randomized to the same breast feeding duration"
        self.assertEqual(rando1.bf_duration, rando2.bf_duration)
        print "assert that the twins were randomized to the same rx arm"
        self.assertEqual(rando1.rx, rando2.rx)
        print "assert that the twins were randomized to the same stratum"
        self.assertEqual(rando1.stratum,rando2.stratum)
        print "assert that the twins were randomized to the same site"
        self.assertEqual(rando1.site, rando2.site)

        print "ensure original set rando fields remain unchanged"
        og = original_sids.get(sid=rando1.sid)
        print "assert that for sid assigned twin 1, rx remained unchanged"
        self.assertEqual(og.rx, rando1.rx)
        print "assert that for sid assigned twin 1, site remained unchanged"
        self.assertEqual(og.site, rando1.site)
        print "assert that for sid assigned twin 1, stratum remained unchanged"
        self.assertEqual(og.stratum, rando1.stratum)
        print "assert that for sid assigned twin 1, bf_duration remained unchanged"
        if infant_eligibility1.maternal_feeding_choice =='BF':
            self.assertEqual(og.bf_duration, rando1.bf_duration)
        og = original_sids.get(sid=rando2.sid)
        print "assert that for sid assigned twin 2, rx remained unchanged"
        self.assertEqual(og.rx, rando2.rx)
        print "assert that for sid assigned twin 2, site remained unchanged"
        self.assertEqual(og.site, rando2.site)
        print "assert that for sid assigned twin 2, stratum remained unchanged"
        self.assertEqual(og.stratum, rando2.stratum)
        print "assert that for sid assigned twin 2, bf_duration remained unchanged"
        if infant_eligibility2.maternal_feeding_choice =='BF':
            self.assertEqual(og.bf_duration, rando2.bf_duration)

    def test_check(self):

        print "assert that if weight is less than 2.5 randomization check will return false"
        allow_rando = Eligibility().check(
                current_consent_version=2,
                dob=self.delivery_datetime.date(),
                ga=37,
                weight=2.1,
                clinical_jaundice='No',
                anemia_neutropenia='No',
                exception_cls=ValidationError,
                suppress_exception=True
                )
        self.assertFalse(allow_rando, "method check failed to recognise infant is underweight")

        print "assert that if infant days alive is less than 14 then check will return false"
        allow_rando = Eligibility().check(
                current_consent_version=2,
                dob=date.today(),
                ga=37,
                weight=3.9,
                clinical_jaundice='No',
                anemia_neutropenia='No',
                exception_cls=ValidationError,
                suppress_exception=True
                )
        self.assertFalse(allow_rando, "method check failed to recognise infant days of alive < 14")

        print "assert that if infant days alive is greater than 14 then check will return false"
        allow_rando = Eligibility().check(
                current_consent_version=2,
                dob=date.today()+timedelta(365),
                ga=37,
                weight=3.9,
                clinical_jaundice='No',
                anemia_neutropenia='No',
                exception_cls=ValidationError,
                suppress_exception=True
                )
        self.assertFalse(allow_rando, "method check failed to recognise infant days of alive > 14")

        print "assert that if infant is jaundiced then check will return false"
        allow_rando = Eligibility().check(
                current_consent_version=2,
                dob=self.delivery_datetime.date(),
                ga=37,
                weight=3.9,
                clinical_jaundice='Yes',
                anemia_neutropenia='No',
                exception_cls=ValidationError,
                suppress_exception=True
                )
        self.assertFalse(allow_rando, "method check failed to recognise infant is jaundiced")

        print "assert that if infant has aneimaia then check will return false"
        allow_rando = Eligibility().check(
                current_consent_version=2,
                dob=self.delivery_datetime.date(),
                ga=37,
                weight=3.9,
                clinical_jaundice='No',
                anemia_neutropenia='Yes',
                exception_cls=ValidationError,
                suppress_exception=True
                )
        self.assertFalse(allow_rando, "method check failed to recognise infant has anemia")

        print "assert that if mother has ga less than 36 then check will return false"
        allow_rando = Eligibility().check(
                current_consent_version=2,
                dob=self.delivery_datetime.date(),
                ga=30,
                weight=3.9,
                clinical_jaundice='No',
                anemia_neutropenia='No',
                exception_cls=ValidationError,
                suppress_exception=True
                )
        self.assertFalse(allow_rando, "method check failed to recognise mother's ga is less than 36")

    def populate_rando(self):

        InfantRando.objects.create(site='Gaborone', stratum='BF,HAART', sid=110140,rx='CTX',bf_duration='6months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,HAART', sid=110142,rx='CTX',bf_duration='6months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,HAART', sid=110143,rx='CTX',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,HAART', sid=110144,rx='CTX',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,HAART', sid=110172,rx='CTX',bf_duration='6months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,HAART', sid=110173,rx='CTX',bf_duration='6months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,HAART', sid=110174,rx='CTX',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,HAART', sid=110175,rx='CTX',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,notHAART', sid=110176,rx='CTX',bf_duration='6months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,notHAART', sid=110177,rx='CTX',bf_duration='6months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,notHAART', sid=110178,rx='CTX',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,notHAART', sid=110179,rx='CTX',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,notHAART', sid=110180,rx='CTX',bf_duration='6months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,notHAART', sid=110100,rx='CTX',bf_duration='6months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,notHAART', sid=110101,rx='CTX',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,notHAART', sid=110102,rx='CTX',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='FF', sid=110145,rx='CTX',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='FF', sid=110146,rx='CTX',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='FF', sid=110147,rx='CTX',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,HAART', sid=110148,rx='Placebo',bf_duration='6months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,HAART', sid=110149,rx='Placebo',bf_duration='6months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,HAART', sid=110150,rx='Placebo',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,notHAART', sid=110151,rx='Placebo',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='BF,notHAART', sid=110152,rx='Placebo',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='FF', sid=110153,rx='Placebo',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='FF', sid=110154,rx='Placebo',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='FF', sid=110155,rx='Placebo',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Gaborone', stratum='FF', sid=110156,rx='Placebo',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Molepolole', stratum='FF', sid=110157,rx='CTX',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Molepolole', stratum='FF', sid=110158,rx='CTX',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Molepolole', stratum='FF', sid=110159,rx='CTX',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Molepolole', stratum='BF,HAART', sid=110160,rx='CTX',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Molepolole', stratum='BF,HAART', sid=110161,rx='CTX',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Molepolole', stratum='FF', sid=110162,rx='Placebo',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Molepolole', stratum='FF', sid=110163,rx='Placebo',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Molepolole', stratum='FF', sid=110164,rx='Placebo',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Molepolole', stratum='BF,HAART', sid=110165,rx='Placebo',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Molepolole', stratum='BF,notHAART', sid=110166,rx='Placebo',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Lobatse', stratum='FF', sid=110167,rx='CTX',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Lobatse', stratum='BF,HAART', sid=110168,rx='CTX',bf_duration='12months',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Lobatse', stratum='FF', sid=110169,rx='Placebo',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Lobatse', stratum='FF', sid=110170,rx='Placebo',bf_duration='',dispensed='NO',infant_initials='XX')
        InfantRando.objects.create(site='Lobatse', stratum='BF,notHAART', sid=110171,rx='Placebo',bf_duration='12months',dispensed='NO',infant_initials='XX')
        return InfantRando.objects.all()
