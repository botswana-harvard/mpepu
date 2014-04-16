from django.test import TestCase
from datetime import datetime, date, timedelta
from django.core.exceptions import ValidationError

from edc.core.bhp_content_type_map.models import ContentTypeMap
from edc.core.bhp_variables.tests.factories import StudySiteFactory
from edc.core.identifier.models import SubjectIdentifier
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.subject.appointment.models import Appointment
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.subject.entry.tests.factories import EntryFactory
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.registration.models import RegisteredSubject
from edc.subject.visit_schedule.classes import site_visit_schedules

from apps.mpepu_lab.lab_profiles import MpepuInfantProfile
from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration

from apps.mpepu_maternal.tests.factories import (MaternalConsentFactory, MaternalEligibilityPostFactory,
                                                 MaternalVisitFactory, MaternalLabDelFactory)
from apps.mpepu_infant.tests.factories import (InfantBirthFactory, InfantVisitFactory)


class InfantVisitTests(TestCase):

    def setUp(self):
        try:
            site_lab_profiles.register(MpepuInfantProfile())
        except AlreadyRegistered:
            pass
        MpepuAppConfiguration()
        site_lab_tracker.autodiscover()
        site_visit_schedules.autodiscover()
        site_visit_schedules.build_all()
        study_site = StudySiteFactory(site_code=2)
        content_type_map = ContentTypeMap.objects.get(model='maternalconsent', app_label='mpepu_maternal')
        consent_catalogue = ConsentCatalogueFactory(content_type_map=content_type_map)
        consent_catalogue.add_for_app = 'mpepu_infant'
        consent_catalogue.save()
        delivery_days_ago = 20
        self.delivery_datetime = datetime.today() - timedelta(days=delivery_days_ago - 3)
        print "Consent a mother"
        self.maternal_consent = MaternalConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print "Consent: {}".format(self.maternal_consent)
        self.registered_subject = RegisteredSubject.objects.get(subject_identifier=self.maternal_consent.subject_identifier)
        print 'check if mother is eligible'
        self.maternal_eligibility = MaternalEligibilityPostFactory(maternal_consent=self.maternal_consent, registered_subject=self.registered_subject, registration_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print 'get the 2000M visit'
        self.m_appointment = Appointment.objects.get(registered_subject=self.registered_subject, visit_definition__code='2000M')
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
        self.registered_subject = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'infant registered subject {}'.format(self.registered_subject)
        self.infant_birth = InfantBirthFactory(registered_subject=self.registered_subject, maternal_lab_del=self.maternal_lab_del, dob=self.delivery_datetime.date())
        print 'infant birth {}'.format(self.infant_birth)
        print 'get 2000 appointment'
        appointment_2000 = Appointment.objects.get(registered_subject=self.registered_subject, visit_definition__code='2000')
        print '2000 appointment {}'.format(appointment_2000)
        infant_visit_2000 = InfantVisitFactory(appointment=appointment_2000, report_datetime=datetime.today(), reason='scheduled')
        print '2000 infant visit {}'.format(infant_visit_2000)
        print 'get 2010 appointment'
        appointment_2010 = Appointment.objects.get(registered_subject=self.registered_subject, visit_definition__code='2010')
        print "assert that saving 2010 infant visit before saving infant eligibility fails"
        self.assertRaisesMessage(ValidationError,
            'Please complete the Infant Eligibility or Infant Pre-eligibility before conducting scheduled visits beyond visit 2000.',
            InfantVisitFactory, appointment=appointment_2010, report_datetime=datetime.today(), reason='scheduled')
        