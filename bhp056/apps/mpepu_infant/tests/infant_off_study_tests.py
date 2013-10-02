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
from mpepu_infant.models import InfantBirth, InfantVisit
from factories import InfantVisitFactory, InfantBirthFactory, InfantBirthDataFactory, InfantEligibilityFactory, InfantOffStudyFactory, InfantArvProphFactory, InfantArvProphModFactory


class InfantOffStudyTests(TestCase):
    app_label = 'mpepu_maternal'
    subject_consent = MaternalConsent
    consent_catalogue_name = 'mpepu V1'
    visit_model = MaternalVisit

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
        consent_catalogue.add_for_app = 'mpepu_maternal'
        consent_catalogue.save()
        consent_catalogue.add_for_app = 'mpepu_infant'
        consent_catalogue.save()

        maternal_visit_tracking_content_type_map = ContentTypeMap.objects.get(content_type__model='maternalvisit')

        print 'setup bhp_visit'
        content_type_map = ContentTypeMap.objects.get(content_type__model=MaternalEligibilityAnte._meta.object_name.lower())
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Maternal Ante Natal Reg', grouping_key='ELIGIBILITY')
        visit_definition = VisitDefinitionFactory(code='1000M', title='Maternal Ante Natal Registration', grouping='maternal', visit_tracking_content_type_map=maternal_visit_tracking_content_type_map)
        visit_definition.schedule_group.add(schedule_group)

        content_type_map = ContentTypeMap.objects.get(content_type__model=MaternalEligibilityPost._meta.object_name.lower())
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Maternal Post Partum Reg', grouping_key='ELIGIBILITY')
        visit_definition = VisitDefinitionFactory(code='2000M', title='Maternal Post Natal Registration', grouping='maternal', visit_tracking_content_type_map=maternal_visit_tracking_content_type_map)
        visit_definition.schedule_group.add(schedule_group)

        content_type_map = ContentTypeMap.objects.get(content_type__model=MaternalPostReg._meta.object_name.lower())
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Post Partum Follow-up')
        visit_definition = VisitDefinitionFactory(code='2010M', title='Infant Randomization', grouping='maternal', visit_tracking_content_type_map=maternal_visit_tracking_content_type_map)
        visit_definition.schedule_group.add(schedule_group)

        infant_visit_tracking_content_type_map = ContentTypeMap.objects.get(content_type__model='infantvisit')

        content_type_map = ContentTypeMap.objects.get(content_type__model=InfantBirth._meta.object_name.lower())
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Infant Birth')
        visit_definition = VisitDefinitionFactory(code='2000', title='Infant Birth', grouping='infant', time_point=0, base_interval=0, base_interval_unit='D', visit_tracking_content_type_map=infant_visit_tracking_content_type_map)
        visit_definition.schedule_group.add(schedule_group)
        visit_definition = VisitDefinitionFactory(code='2010', title='Randomization', grouping='infant', time_point=10, base_interval=27, base_interval_unit='D', visit_tracking_content_type_map=infant_visit_tracking_content_type_map)
        visit_definition.schedule_group.add(schedule_group)
        
        #entry = 

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
        infant_off_study = InfantOffStudyFactory(registered_subject=registered_subject, offstudy_date=date.today() - timedelta(days=0))
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
        print 'complete off study model'
        infant_off_study = InfantOffStudyFactory(registered_subject=registered_subject, offstudy_date=date.today() - timedelta(days=1))
        print 'confirm cannot add a visit'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000')
        self.assertRaises(SubjectOffStudyError, InfantVisitFactory, appointment=appointment, report_datetime=datetime.today(), reason='scheduled')
        print 'remove remove off study'
        infant_off_study.delete()
        print 'add a visit (1 day ago)'
        infant_visit = InfantVisitFactory(appointment=appointment, report_datetime=datetime.today() - timedelta(days=1), reason='scheduled')
        print 'complete off study model (1 day ago)'
        infant_off_study = InfantOffStudyFactory(registered_subject=registered_subject, offstudy_date=date.today() - timedelta(days=1))
        print 'confirm cannot complete infant eligibility for today'
        infant_eligibility = InfantEligibilityFactory(infant_birth=infant_birth, registered_subject=registered_subject)
        print 'complete infant birth data'
        infant_birth_data = InfantBirthDataFactory(infant_visit=infant_visit, infant_birth=infant_birth)
        print 'complete infant_arv_proh'
        infant_arv_proph = InfantArvProphFactory(infant_visit=infant_visit)
        infant_arv_proph_mode = InfantArvProphModFactory(infant_arv_proph=infant_arv_proph)

        print 'complete off study model'
        print 'delete off study model'
        infant_off_study.delete()
        print 'confirm cannot add an off study with younger data already entered (3 days ago)'
        self.assertRaises(SubjectOffStudyDateError, InfantOffStudyFactory, registered_subject=registered_subject, offstudy_date=date.today() - timedelta(days=3))
        print 'complete off study model for today'
        infant_off_study = InfantOffStudyFactory(registered_subject=registered_subject, offstudy_date=date.today() - timedelta(days=1))
