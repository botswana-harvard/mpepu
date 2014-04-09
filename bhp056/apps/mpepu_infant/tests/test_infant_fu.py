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
from apps.mpepu_infant.tests.factories import (InfantBirthFactory, InfantVisitFactory, InfantEligibilityFactory,
                                               InfantFuFactory, InfantFuPhysicalFactory)

from ..forms import InfantFuPhysicalForm


class InfantFuTests(TestCase):
    def setUp(self):
        try:
            site_lab_profiles.register(MpepuInfantProfile())
        except AlreadyRegistered:
            pass
        MpepuAppConfiguration()
        site_lab_tracker.autodiscover()
        site_visit_schedules.autodiscover()
        site_visit_schedules.build_all()

    def test_bf(self):
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
        infant_eligibility = InfantEligibilityFactory(infant_birth=infant_birth1, registered_subject=registered_subject1)
        appointment1 = Appointment.objects.get(registered_subject=registered_subject1, visit_definition__code='2010')
        infant_visit1 = InfantVisitFactory(appointment=appointment1, report_datetime=datetime.today(), reason='scheduled')
        fu = InfantFuFactory(infant_visit=infant_visit1)
        print "Infant Fu {}".format(fu)
        print "create an infant followup physical"
        fu_physical = InfantFuPhysicalFactory(infant_visit=infant_visit1, infant_fu=fu, was_hospitalized='No')
        print "Infant Fu Physical {}".format(fu_physical)
