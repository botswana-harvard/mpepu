import re
import pprint
from datetime import datetime, date, timedelta
from django.test import TestCase
from django.db.models import get_app, get_models
from bhp_identifier.exceptions import IdentifierError
from bhp_lab_tracker.classes import lab_tracker
from bhp_variables.models import StudySpecific, StudySite
from bhp_variables.tests.factories import StudySpecificFactory, StudySiteFactory
from bhp_registration.models import RegisteredSubject
from bhp_consent.tests.factories import ConsentCatalogueFactory
from edc.subject.appointment.models import Appointment
from bhp_appointment.tests.factories import ConfigurationFactory
from bhp_visit.tests.factories import MembershipFormFactory, ScheduleGroupFactory, VisitDefinitionFactory
from bhp_content_type_map.classes import ContentTypeMapHelper
from bhp_content_type_map.models import ContentTypeMap
from mpepu_maternal.models import MaternalVisit, MaternalConsent, MaternalOffStudy, MaternalEligibilityAnte, MaternalEligibilityPost, MaternalPostReg
from mpepu_maternal.tests.factories import MaternalConsentFactory, MaternalOffStudyFactory, MaternalVisitFactory, MaternalEligibilityAnteFactory, MaternalLabDelFactory
from bhp_identifier.models import SubjectIdentifier, Sequence
from bhp_off_study.exceptions import SubjectOffStudyError, SubjectOffStudyDateError


class MaternalOffStudyTests(TestCase):
    app_label = 'mpepu_maternal'
    subject_consent = MaternalConsent
    consent_catalogue_name = 'mpepu V1'
    visit_model = MaternalVisit

    def test_has_off_study_mixin(self):
        print 'check each model has off study methods'
        app = get_app('mpepu_maternal')
        for model in get_models(app):
            if 'Audit' not in model._meta.object_name and 'OffStudy' not in model._meta.object_name:
                print model._meta.object_name
                self.assertTrue('get_off_study_cls' in dir(model), 'Method \'get_off_study_cls\' not found on model {0}'.format(model._meta.object_name))
                self.assertTrue('is_off_study' in dir(model), 'Method \'is_off_study\' not found on model {0}'.format(model._meta.object_name))
                self.assertTrue('get_report_datetime' in dir(model), 'Method \'get_report_datetime\' not found on model {0}'.format(model._meta.object_name))
                self.assertTrue('get_subject_identifier' in dir(model), 'Method \'get_subject_identifier\' not found on model {0}'.format(model._meta.object_name))

    def test_p1(self):
        lab_tracker.autodiscover()
        StudySpecificFactory()
        study_site = StudySiteFactory()
        ConfigurationFactory()
        content_type_map_helper = ContentTypeMapHelper()
        content_type_map_helper.populate()
        content_type_map_helper.sync()
        print 'setup the consent catalogue for app {0}'.format(self.app_label)
        content_type_map = ContentTypeMap.objects.get(content_type__model=self.subject_consent._meta.object_name.lower())
        consent_catalogue = ConsentCatalogueFactory(name=self.consent_catalogue_name, content_type_map=content_type_map)
        consent_catalogue.add_for_app = self.app_label
        consent_catalogue.save()

        print 'setup bhp_visit'
        content_type_map = ContentTypeMap.objects.get(content_type__model=MaternalEligibilityAnte._meta.object_name.lower())
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Maternal Ante Natal Reg', grouping_key='ELIGIBILITY')
        visit_definition = VisitDefinitionFactory(code='1000M', title='Maternal Ante Natal Registration', grouping='maternal')
        visit_definition.schedule_group.add(schedule_group)

        content_type_map = ContentTypeMap.objects.get(content_type__model=MaternalEligibilityPost._meta.object_name.lower())
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Maternal Post Partum Reg', grouping_key='ELIGIBILITY')
        visit_definition = VisitDefinitionFactory(code='2000M', title='Maternal Post Natal Registration', grouping='maternal')
        visit_definition.schedule_group.add(schedule_group)

        content_type_map = ContentTypeMap.objects.get(content_type__model=MaternalPostReg._meta.object_name.lower())
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Post Partum Follow-up')
        visit_definition = VisitDefinitionFactory(code='2010M', title='Infant Randomization', grouping='maternal')
        visit_definition.schedule_group.add(schedule_group)

        print 'consent a mother (2 days ago)'
        maternal_consent = MaternalConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=2))
        print maternal_consent.subject_identifier
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'take mother off study (1 day ago)'
        maternal_off_study = MaternalOffStudyFactory(registered_subject=registered_subject, offstudy_date=date.today() - timedelta(days=1))
        print 'Off study: {0}'.format(maternal_off_study)
        print 'confirm cannot add a registration form today'
        self.assertRaises(SubjectOffStudyError, MaternalEligibilityAnteFactory, maternal_consent=maternal_consent, registered_subject=registered_subject, registration_datetime=datetime.today() - timedelta(days=0))

        print 'consent a mother (3 days ago)'
        maternal_consent = MaternalConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=3))
        print maternal_consent.subject_identifier
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'add a registration form 2 days ago'
        maternal_eligibility = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject, registration_datetime=datetime.today() - timedelta(days=2))
        print 'confirm appointments'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        print 'Appointment {0} {1}'.format(appointment, appointment.appt_datetime)
        print 'take mother off study (1 day ago)'
        maternal_off_study = MaternalOffStudyFactory(registered_subject=registered_subject, offstudy_date=appointment.appt_datetime - timedelta(days=1))
        print 'Off study: {0} offstudy_datetime={1}'.format(maternal_off_study, date.today() - timedelta(days=1))
        print 'confirm appointments deleted'
        self.assertEquals(Appointment.objects.filter(registered_subject=registered_subject, visit_definition__code='1000M').count(), 0)

        print 'consent a mother (4 days ago)'
        maternal_consent = MaternalConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=4))
        print maternal_consent.subject_identifier
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'add a registration form 3 days ago'
        maternal_eligibility = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject, registration_datetime=datetime.today() - timedelta(days=3))
        print 'confirm appointments'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        print 'add a visit form 2 days ago'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        maternal_visit = MaternalVisitFactory(appointment=appointment, report_datetime=datetime.today() - timedelta(days=2))
        print 'confirm cannot take mother off study (3 day ago)'
        self.assertRaises(SubjectOffStudyDateError, MaternalOffStudyFactory, registered_subject=registered_subject, offstudy_date=date.today() - timedelta(days=3))
        print 'confirm can take mother off study (2 day ago)'
        maternal_off_study = MaternalOffStudyFactory(registered_subject=registered_subject, offstudy_date=date.today() - timedelta(days=2))
        print 'Off study: {0}'.format(maternal_off_study)
        print 'confirm appointments not deleted'
        self.assertEquals(Appointment.objects.filter(registered_subject=registered_subject, visit_definition__code='1000M').count(), 1)

