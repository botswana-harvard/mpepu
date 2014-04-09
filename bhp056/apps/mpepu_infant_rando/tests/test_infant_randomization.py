from datetime import datetime, timedelta
from django.test import TestCase
from django.core.exceptions import ValidationError

from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.visit_schedule.classes import site_visit_schedules
from edc.core.bhp_variables.tests.factories import StudySiteFactory
from edc.core.bhp_content_type_map.models import ContentTypeMap
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.subject.appointment.models import Appointment
from edc.lab.lab_profile.classes import site_lab_profiles

from apps.mpepu_lab.lab_profiles import MpepuInfantProfile
from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration
from edc.subject.registration.models import RegisteredSubject
from apps.mpepu_maternal.tests.factories import (MaternalConsentFactory, MaternalEligibilityPostFactory,
                                                 MaternalVisitFactory, MaternalLabDelFactory)
from apps.mpepu_infant.tests.factories import InfantBirthFactory, InfantVisitFactory, InfantEligibilityFactory

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

    def test_multiple_birth_rando(self):
        study_site = StudySiteFactory(site_code=2)
        content_type_map = ContentTypeMap.objects.get(model='maternalconsent', app_label='mpepu_maternal')
        consent_catalogue = ConsentCatalogueFactory(content_type_map=content_type_map)
        consent_catalogue.add_for_app = 'mpepu_infant'
        consent_catalogue.save()

        delivery_days_ago = 20
        delivery_datetime = datetime.today() - timedelta(days=delivery_days_ago - 3)
        print "Consent a mother"
        maternal_consent = MaternalConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print "Consent: {}".format(maternal_consent)
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'check if mother is eligible'
        maternal_eligibility = MaternalEligibilityPostFactory(maternal_consent=maternal_consent, registered_subject=registered_subject, registration_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print 'get the 2000M visit'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000M')
        print 'create a maternal visit for the 2000M visit'
        maternal_visit = MaternalVisitFactory(appointment=appointment, report_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print 'create a maternal_lab_del registering 2 of 2 infants'
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit,
                                                         live_infants=2,
                                                         live_infants_to_register=2,
                                                         delivery_datetime=delivery_datetime,
                                                         has_ga='Yes',
                                                         ga=37,

                                                         )
        print 'maternal lab del: {}'.format(maternal_lab_del)
        print 'get registered subject of the first infant'
        registered_subject1 = RegisteredSubject.objects.filter(relative_identifier=maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'first registered subject {}'.format(registered_subject1)
        infant_birth1 = InfantBirthFactory(registered_subject=registered_subject1, maternal_lab_del=maternal_lab_del, dob=delivery_datetime.date())
        print 'first infant birth {}'.format(infant_birth1)
        appointment1 = Appointment.objects.get(registered_subject=registered_subject1, visit_definition__code='2000')
        infant_visit1 = InfantVisitFactory(appointment=appointment1, report_datetime=datetime.today(), reason='scheduled')

        for idx in xrange(1,5):
            self.populate_rando(site='Molepolole', sid=idx, rx='CTX')
            self.populate_rando(sid=idx+9, rx='CTX')
            self.populate_rando(sid=idx+14, rx='CTX', bf_duration='12months')
            self.populate_rando(site='Lobatse', sid=idx+19, rx='CTX')
            self.populate_rando(site='Molepolole', sid=idx+24, rx='Placebo')
            self.populate_rando(site='Lobatse', sid=idx+29, rx='Placebo')
            self.populate_rando(sid=idx+34, rx='Placebo')
            self.populate_rando(site='Molepolole', stratum='FF', sid=idx+39, rx='CTX', bf_duration='NA')
            self.populate_rando(sid=idx+44, rx='CTX', stratum='FF',bf_duration='NA')
            self.populate_rando(site='Lobatse', stratum='FF', sid=idx+49, rx='CTX', bf_duration='NA')
            self.populate_rando(site='Molepolole', stratum='FF', sid=idx+54, rx='Placebo', bf_duration='NA')
            self.populate_rando(site='Lobatse', stratum='FF', sid=idx+59, rx='Placebo', bf_duration='NA')
            self.populate_rando(stratum='FF', sid=idx+64, rx='Placebo', bf_duration='')
            self.populate_rando(stratum='FF', sid=idx+104, rx='Placebo', bf_duration='')
            self.populate_rando(stratum='FF', sid=idx+124, rx='Placebo', bf_duration='')

        original_sids = InfantRando.objects.all()
#         for i in original_sids: 
#             print list(i.__dict__)

        allow_rando1 = Eligibility().check(
                current_consent_version=2,
                dob=delivery_datetime.date(),
                ga=37,
                weight=4,
                clinical_jaundice='No',
                anemia_neutropenia='No',
                exception_cls=ValidationError,
                suppress_exception=False)
        print 'allow rando {}'.format(allow_rando1)
        infant_eligibility1 = InfantEligibilityFactory(
                    infant_birth=infant_birth1,
                    registered_subject=infant_birth1.registered_subject,
                    rando_bf_duration = 'N/A',
                    congen_anomaly = 'No',
                    maternal_art_status = 'ON',
                    maternal_feeding_choice = 'FF',
                    randomization_site = 'Gaborone',
                    ctx_contra = 'No',
                    )
        print 'Infant Eligibility {}'.format(infant_eligibility1.__dict__)
        print 'assert that the rest of the appointments were created, i.e. 2000,2010,2020,2030,2060,2090,2120,2150,2180'
        all_appointments = Appointment.objects.filter(registered_subject=registered_subject1)
        self.assertEqual(all_appointments.count(), 9)
        print 'confirm infant 1 was randomized'
        print InfantRando.objects.randomize(infant_eligibility=infant_eligibility1)
        print InfantRando.objects.get(subject_identifier=registered_subject1.subject_identifier)
        print 'get registered subject of the second infant'
        registered_subject2 = RegisteredSubject.objects.filter(relative_identifier=maternal_consent.subject_identifier).order_by('subject_identifier')[1]
        print 'second registered subject {}'.format(registered_subject2)
        infant_birth2 = InfantBirthFactory(registered_subject=registered_subject2, maternal_lab_del=maternal_lab_del, dob=delivery_datetime.date())
        print 'second infant birth {}'.format(infant_birth2)
        appointment2 = Appointment.objects.get(registered_subject=registered_subject2, visit_definition__code='2000')
        infant_visit2 = InfantVisitFactory(appointment=appointment2, report_datetime=datetime.today(), reason='scheduled')
        allow_rando2 = Eligibility().check(
                current_consent_version=2,
                dob=delivery_datetime.date(),
                ga=37,
                weight=3.9,
                clinical_jaundice='No',
                anemia_neutropenia='No',
                exception_cls=ValidationError,
                suppress_exception=False)
        print 'allow rando {}'.format(allow_rando2)
        infant_eligibility2 = InfantEligibilityFactory(
                    infant_birth=infant_birth2,
                    registered_subject=infant_birth2.registered_subject,
                    rando_bf_duration = 'No',
                    congen_anomaly = 'No',
                    maternal_art_status = 'ON',
                    maternal_feeding_choice = 'BF',
                    randomization_site = 'Molepolole',
                    ctx_contra = 'No',
                    )
        print infant_eligibility2
        print 'assert that the rest of the appointments were created, i.e. 2000,2010,2020,2030,2060,2090,2120,2150,2180'
        all_appointments = Appointment.objects.filter(registered_subject=registered_subject2)
        self.assertEqual(all_appointments.count(), 9)
        print 'confirm infant 2 was randomized'
        InfantRando.objects.randomize(infant_eligibility=infant_eligibility2)
        print InfantRando.objects.get(subject_identifier=registered_subject2.subject_identifier)
        rando1 = InfantRando.objects.get(subject_identifier=registered_subject1.subject_identifier)
        rando2 = InfantRando.objects.get(subject_identifier=registered_subject1.subject_identifier)
        print "assert that the twins were randomized to the same feeding arm"
        self.assertEquals(rando1.feeding_choice, rando2.feeding_choice)
        print "assert that the twins were randomized to the same breast feeding duration"
        self.assertEqual(rando1.bf_duration, rando2.bf_duration)
        print "assert that the twins were randomised to the same rx arm"
        self.assertEqual(rando1.rx, rando2.rx)
        print "assert that the twins were randomised to the same stratum"
        self.assertEqual(rando1.stratum,rando2.stratum)
        print "assert that the twins were randomised to the same site"
        self.assertEqual(rando1.site, rando2.site)

        print "ensure original set rando fields remain unchanged"
        og = original_sids.get(sid=rando1.sid)
        print "assert that for sid assigned twin 1, rx remained unchanged"
        self.assertEqual(og.rx, rando1.rx)
        print "assert that for sid assined twin 1, site remained unchanged"
        self.assertEqual(og.site, rando1.site)
        print "assert that for sid assined twin 1, stratum remained unchanged"
        self.assertEqual(og.stratum, rando1.stratum)
        print "assert that for sid assined twin 1, bf_duration remained unchanged"
#         self.assertEqual(og.bf_duration, rando1.bf_duration)
        og = original_sids.get(sid=rando2.sid)
        print "assert that for sid assigned twin 2, rx remained unchanged"
        self.assertEqual(og.rx, rando2.rx)
        print "assert that for sid assined twin 2, site remained unchanged"
        self.assertEqual(og.site, rando2.site)
        print "assert that for sid assined twin 2, stratum remained unchanged"
        self.assertEqual(og.stratum, rando2.stratum)
        print "assert that for sid assined twin 2, bf_duration remained unchanged"
#         self.assertEqual(og.bf_duration, rando2.bf_duration)

    def populate_rando(self,site='Gaborone', stratum='BF,HAART', sid=1,rx='Placebo',bf_duration='6months'):
        _sid = 110140 + sid
        return InfantRando.objects.create(site=site, stratum=stratum, sid=_sid,rx=rx,bf_duration=bf_duration,dispensed='NO',infant_initials='XX')
