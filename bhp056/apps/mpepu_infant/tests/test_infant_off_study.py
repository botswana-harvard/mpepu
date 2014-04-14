import re
import pprint
from datetime import datetime, date, timedelta
from django.test import TestCase
from django.db.models import get_app, get_models

from edc.core.bhp_content_type_map.models import ContentTypeMap
from edc.core.bhp_variables.tests.factories import StudySiteFactory
from edc.core.identifier.exceptions import IdentifierError
from edc.core.identifier.models import SubjectIdentifier
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.subject.appointment.models import Appointment
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.off_study.exceptions import SubjectOffStudyError, SubjectOffStudyDateError
from edc.subject.registration.models import RegisteredSubject
from edc.subject.visit_schedule.classes import site_visit_schedules

from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration
from apps.mpepu_infant.models import InfantBirth, InfantVisit
from apps.mpepu_lab.lab_profiles import MpepuInfantProfile
from apps.mpepu_maternal.models import MaternalVisit, MaternalConsent, MaternalOffStudy, MaternalEligibilityAnte, MaternalEligibilityPost, MaternalPostReg
from apps.mpepu_maternal.tests.factories import MaternalConsentFactory, MaternalOffStudyFactory, MaternalVisitFactory, MaternalEligibilityAnteFactory, MaternalLabDelFactory

from .factories import InfantVisitFactory, InfantBirthFactory, InfantBirthDataFactory, InfantEligibilityFactory, InfantOffStudyFactory, InfantArvProphFactory, InfantArvProphModFactory


class InfantOffStudyTests(TestCase):
    app_label = 'mpepu_maternal'
    subject_consent = MaternalConsent
    consent_catalogue_name = 'mpepu V1'
    visit_model = MaternalVisit

    def setUp(self):
        try:
            site_lab_profiles.register(MpepuInfantProfile())
        except AlreadyRegistered:
            pass
        MpepuAppConfiguration()
        site_lab_tracker.autodiscover()
        site_visit_schedules.autodiscover()
        site_visit_schedules.build_all()

    def test_off_study_mixin(self):
        print 'check each model has off study methods from mixin'
        app = get_app('mpepu_infant')
        for model in get_models(app):
            if 'Audit' not in model._meta.object_name and 'OffStudy' not in model._meta.object_name:
                print model._meta.object_name
                self.assertTrue('get_off_study_cls' in dir(model), 'Method \'get_off_study_cls\' not found on model {0}'.format(model._meta.object_name))
                self.assertTrue('is_off_study' in dir(model), 'Method \'is_off_study\' not found on model {0}'.format(model._meta.object_name))
                self.assertTrue('get_report_datetime' in dir(model), 'Method \'get_report_datetime\' not found on model {0}'.format(model._meta.object_name))
                self.assertTrue('get_subject_identifier' in dir(model), 'Method \'get_subject_identifier\' not found on model {0}'.format(model._meta.object_name))

    def test_p1(self):
        study_site = StudySiteFactory(site_code=2)
        content_type_map = ContentTypeMap.objects.get(model='maternalconsent', app_label='mpepu_maternal')
        consent_catalogue = ConsentCatalogueFactory(content_type_map=content_type_map)
        consent_catalogue.add_for_app = 'mpepu_infant'
        consent_catalogue.save()

        print 'consent a mother (30 days ago)'
        maternal_consent = MaternalConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=30))
        print maternal_consent.subject_identifier
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'add a registration form 30 days ago'
        maternal_eligibility = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject, registration_datetime=datetime.today() - timedelta(days=30))
        print 'add a visit form 28 days ago'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        maternal_visit = MaternalVisitFactory(appointment=appointment, report_datetime=datetime.today() - timedelta(days=28))
        print 'create a maternal lab-del: registering 2 of 1 infant'
        delivery_datetime = datetime.today() - timedelta(days=28)
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit, live_infants=2, live_infants_to_register=1, delivery_datetime=delivery_datetime)
        print maternal_lab_del
        print 'confirm infant subject identifier in bhp_identifier.models.SubjectIdentifier and follows derived format {0}'.format('{0}-25'.format(maternal_consent.subject_identifier))
        self.assertIsNotNone(SubjectIdentifier.objects.get(identifier='{0}-25'.format(maternal_consent.subject_identifier)))
        print 'confirm infant registered subject exists'
        registered_subject = RegisteredSubject.objects.get(relative_identifier=maternal_consent.subject_identifier)
        print registered_subject
        print 'complete infant birth'
        infant_birth = InfantBirthFactory(registered_subject=registered_subject, maternal_lab_del=maternal_lab_del, dob=date(delivery_datetime.year, delivery_datetime.month, delivery_datetime.day))
        print infant_birth
        print 'add a visit'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000')
        infant_visit = InfantVisitFactory(appointment=appointment, report_datetime=datetime.today(), reason='scheduled')
        print 'complete infant eligibility'
        infant_eligibility = InfantEligibilityFactory(infant_birth=infant_birth, registered_subject=registered_subject)
        print 'complete infant birth data'
        infant_birth_data = InfantBirthDataFactory(infant_visit=infant_visit, infant_birth=infant_birth)
        print 'complete off study model'
        infant_off_study = InfantOffStudyFactory(registered_subject=registered_subject, offstudy_date=date.today() - timedelta(days=0), infant_visit=infant_visit)
        print 'confirm can still save scheduled model'
        infant_birth_data.save()

        print 'consent a mother (30 days ago)'
        maternal_consent = MaternalConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=30))
        print maternal_consent.subject_identifier
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'add a registration form 30 days ago'
        maternal_eligibility = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject, registration_datetime=datetime.today() - timedelta(days=30))
        print 'add a visit form 28 days ago'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        maternal_visit = MaternalVisitFactory(appointment=appointment, report_datetime=datetime.today() - timedelta(days=28))
        print 'create a maternal lab-del: registering 2 of 1 infant'
        delivery_datetime = datetime.today() - timedelta(days=28)
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit, live_infants=2, live_infants_to_register=1, delivery_datetime=delivery_datetime)
        print maternal_lab_del
        print 'confirm infant subject identifier in bhp_identifier.models.SubjectIdentifier and follows derived format {0}'.format('{0}-25'.format(maternal_consent.subject_identifier))
        self.assertIsNotNone(SubjectIdentifier.objects.get(identifier='{0}-25'.format(maternal_consent.subject_identifier)))
        print 'confirm infant registered subject exists'
        registered_subject = RegisteredSubject.objects.get(relative_identifier=maternal_consent.subject_identifier)
        print registered_subject
        print 'complete infant birth'
        infant_birth = InfantBirthFactory(registered_subject=registered_subject, maternal_lab_del=maternal_lab_del, dob=date(delivery_datetime.year, delivery_datetime.month, delivery_datetime.day))
        print infant_birth
        print 'add a visit 1 day ago'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000')
        infant_visit = InfantVisitFactory(appointment=appointment, report_datetime=datetime.today() - timedelta(days=1), reason='scheduled')
        print 'complete off study model'
        infant_off_study = InfantOffStudyFactory(registered_subject=registered_subject, offstudy_date=date.today() - timedelta(days=1), infant_visit=infant_visit)
        print 'confirm cannot add a visit'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000')
        self.assertRaises(SubjectOffStudyError, InfantVisitFactory, appointment=appointment, report_datetime=datetime.today(), reason='scheduled')
        print 'remove off study'
        infant_off_study.delete()
        infant_off_study = InfantOffStudyFactory(registered_subject=registered_subject, offstudy_date=date.today() - timedelta(days=1),infant_visit=infant_visit)
        print 'assert cannot complete infant eligibility for today'
        self.assertRaises(SubjectOffStudyError, InfantEligibilityFactory,infant_birth=infant_birth, registered_subject=registered_subject)
        print 'remove off study'
        infant_off_study.delete()
        print 'complete infant birth data'
        infant_birth_data = InfantBirthDataFactory(infant_visit=infant_visit, infant_birth=infant_birth)
        print 'complete off study model'
        infant_off_study = InfantOffStudyFactory(registered_subject=registered_subject, offstudy_date=date.today() - timedelta(days=1),infant_visit=infant_visit)
        print 'confirm cannot add an off study with younger data already entered (3 days ago)'
        self.assertRaises(SubjectOffStudyDateError, InfantOffStudyFactory, registered_subject=registered_subject, offstudy_date=date.today() - timedelta(days=3))
