import re
import pprint
from datetime import datetime
from django.test import TestCase
from edc.core.identifier.exceptions import IdentifierError
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.core.bhp_variables.models import StudySpecific, StudySite
from edc.core.bhp_variables.tests.factories import StudySpecificFactory, StudySiteFactory
from edc.subject.registration.models import RegisteredSubject
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.subject.appointment.models import Appointment
from edc.subject.appointment.tests.factories import ConfigurationFactory
from edc.subject.visit_schedule.tests.factories import MembershipFormFactory, ScheduleGroupFactory, VisitDefinitionFactory
from edc.core.bhp_content_type_map.classes import ContentTypeMapHelper
from edc.core.bhp_content_type_map.models import ContentTypeMap
from ..models import MaternalVisit, MaternalConsent, MaternalEligibilityAnte, MaternalEligibilityPost, MaternalPostReg
from ..tests.factories import MaternalConsentFactory, MaternalVisitFactory, MaternalEligibilityAnteFactory, MaternalLabDelFactory
from edc.core.identifier.models import SubjectIdentifier, Sequence


class MaternalRegistrationTests(TestCase):

    app_label = 'mpepu_maternal'
    subject_consent = MaternalConsent
    consent_catalogue_name = 'mpepu V1'
    visit_model = MaternalVisit

    def test_p1(self):
        site_lab_tracker.autodiscover()
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
        visit_definition = VisitDefinitionFactory(code='1000M', title='Maternal Ante Natal Registration', grouping='maternal', visit_tracking_content_type_map=MaternalVisit)
        visit_definition.schedule_group.add(schedule_group)

        content_type_map = ContentTypeMap.objects.get(content_type__model=MaternalEligibilityPost._meta.object_name.lower())
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Maternal Post Partum Reg', grouping_key='ELIGIBILITY', visit_tracking_content_type_map=MaternalVisit)
        visit_definition = VisitDefinitionFactory(code='2000M', title='Maternal Post Natal Registration', grouping='maternal')
        visit_definition.schedule_group.add(schedule_group)

        content_type_map = ContentTypeMap.objects.get(content_type__model=MaternalPostReg._meta.object_name.lower())
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Post Partum Follow-up')
        visit_definition = VisitDefinitionFactory(code='2010M', title='Infant Randomization', grouping='maternal', visit_tracking_content_type_map=MaternalVisit)
        visit_definition.schedule_group.add(schedule_group)

        print 'consent a mother'
        maternal_consent = MaternalConsentFactory(study_site=study_site)
        print maternal_consent.subject_identifier
        print 'confirm maternal subject identifier in bhp_identifier.models.SubjectIdentifier'
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier=maternal_consent.subject_identifier))
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'enroll mother ante natal'
        maternal_eligibility_ante = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject)
        print 'setup a maternal visit for this mother'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        maternal_visit = MaternalVisitFactory(appointment=appointment)
        #print 'confirm number of infants to register cannot exceed number of live infants'
        #self.assertRaises(IdentifierError, MaternalLabDelFactory, maternal_visit=maternal_visit, live_infants=1, live_infants_to_register=5)
        print 'create a maternal lab-del: registering 1 of 1 infant'
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit, live_infants=1, live_infants_to_register=1)
        print maternal_lab_del
        print 'confirm infant subject identifier in bhp_identifier.models.SubjectIdentifier and follows derived format {0}'.format('{0}-10'.format(maternal_consent.subject_identifier))
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier='{0}-10'.format(maternal_consent.subject_identifier)))

        print 'setup up another mother'
        print 'consent a mother'
        maternal_consent = MaternalConsentFactory(study_site=study_site)
        print maternal_consent.subject_identifier
        print 'confirm maternal subject identifier in bhp_identifier.models.SubjectIdentifier'
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier=maternal_consent.subject_identifier))
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'enroll mother ante natal'
        maternal_eligibility_ante = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject)
        print 'setup a maternal visit for this mother'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        maternal_visit = MaternalVisitFactory(appointment=appointment)
        print 'create a maternal lab-del: registering 2 of 1 infant'
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit, live_infants=2, live_infants_to_register=1)
        print maternal_lab_del
        print 'confirm infant subject identifier in bhp_identifier.models.SubjectIdentifier and follows derived format {0}'.format('{0}-10'.format(maternal_consent.subject_identifier))
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier='{0}-10'.format(maternal_consent.subject_identifier)))

        print 'setup up another mother'
        print 'consent a mother'
        maternal_consent = MaternalConsentFactory(study_site=study_site)
        print maternal_consent.subject_identifier
        print 'confirm maternal subject identifier in bhp_identifier.models.SubjectIdentifier'
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier=maternal_consent.subject_identifier))
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'enroll mother ante natal'
        maternal_eligibility_ante = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject)
        print 'setup a maternal visit for this mother'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        maternal_visit = MaternalVisitFactory(appointment=appointment)
        print 'create a maternal lab-del: registering 2 of 2 infant'
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit, live_infants=2, live_infants_to_register=2)
        print maternal_lab_del
        print 'confirm infant subject identifier in bhp_identifier.models.SubjectIdentifier and follows derived format {0} and {1}'.format('{0}-25'.format(maternal_consent.subject_identifier), '{0}-35'.format(maternal_consent.subject_identifier))
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier='{0}-25'.format(maternal_consent.subject_identifier)))
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier='{0}-35'.format(maternal_consent.subject_identifier)))

        print 'setup up another mother'
        print 'consent a mother'
        maternal_consent = MaternalConsentFactory(study_site=study_site)
        print maternal_consent.subject_identifier
        print 'confirm maternal subject identifier in bhp_identifier.models.SubjectIdentifier'
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier=maternal_consent.subject_identifier))
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'enroll mother ante natal'
        maternal_eligibility_ante = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject)
        print 'setup a maternal visit for this mother'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        maternal_visit = MaternalVisitFactory(appointment=appointment)
        print 'create a maternal lab-del: registering 2 of 3 infant'
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit, live_infants=3, live_infants_to_register=2)
        print maternal_lab_del
        print 'confirm infant subject identifier in bhp_identifier.models.SubjectIdentifier and follows derived format \n{0} and \n{1}.'.format(
            '{0}-36'.format(maternal_consent.subject_identifier),
            '{0}-46'.format(maternal_consent.subject_identifier))
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier='{0}-36'.format(maternal_consent.subject_identifier)))
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier='{0}-46'.format(maternal_consent.subject_identifier)))

        print 'setup up another mother'
        print 'consent a mother'
        maternal_consent = MaternalConsentFactory(study_site=study_site)
        print maternal_consent.subject_identifier
        print 'confirm maternal subject identifier in bhp_identifier.models.SubjectIdentifier'
        self.assertIsNotNone(SubjectIdentifier.objects.filter(identifier=maternal_consent.subject_identifier))
        print 'get maternal registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'enroll mother ante natal'
        maternal_eligibility_ante = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject)
        print 'setup a maternal visit for this mother'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        maternal_visit = MaternalVisitFactory(appointment=appointment)
        print 'create a maternal lab-del: registering 4 of 4 infant'
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit, live_infants=4, live_infants_to_register=4)
        print maternal_lab_del
        print 'confirm infant subject identifier in bhp_identifier.models.SubjectIdentifier and follows derived format \n{0}\n{1}\n{2}\n{3}.'.format(
            '{0}-47'.format(maternal_consent.subject_identifier),
            '{0}-57'.format(maternal_consent.subject_identifier),
            '{0}-67'.format(maternal_consent.subject_identifier),
            '{0}-77'.format(maternal_consent.subject_identifier),)
        self.assertIsNotNone(SubjectIdentifier.objects.get(identifier='{0}-47'.format(maternal_consent.subject_identifier)))
        self.assertIsNotNone(SubjectIdentifier.objects.get(identifier='{0}-57'.format(maternal_consent.subject_identifier)))
        self.assertIsNotNone(SubjectIdentifier.objects.get(identifier='{0}-67'.format(maternal_consent.subject_identifier)))
        self.assertIsNotNone(SubjectIdentifier.objects.get(identifier='{0}-77'.format(maternal_consent.subject_identifier)))

        print "confirm sequence table is sequential"
        x = 1
        for obj in Sequence.objects.all().order_by('id'):
            self.assertEqual(obj.id, x)
            x += 1
        print 'confirm sequence was only used for maternal identifiers'
        self.assertEqual(MaternalConsent.objects.all().count(), Sequence.objects.all().count())

        print 'confirm sequence is 0 for infant identifiers based on RegisteredSubject and bhp_identifier.models.SubjectIdentifier'
        self.assertEqual(RegisteredSubject.objects.filter(relative_identifier__isnull=False).count(), SubjectIdentifier.objects.filter(sequence_number=0).count())
        print 'confirm subject_type for infants and mothers'
        self.assertEqual(RegisteredSubject.objects.filter(relative_identifier__isnull=False, subject_type__icontains='infant').count(), SubjectIdentifier.objects.filter(sequence_number=0).count())
        self.assertEqual(RegisteredSubject.objects.filter(relative_identifier__isnull=True, subject_type__icontains='maternal').count(), SubjectIdentifier.objects.exclude(sequence_number=0).count())
        print 'maternal consents'
        for rs in MaternalConsent.objects.all():
            print rs.subject_identifier, rs.subject_type
        print 'subject identifier model'
        for subject_identifier in SubjectIdentifier.objects.all():
            print subject_identifier.identifier, subject_identifier.sequence_number, subject_identifier.device_id
        print 'registered_subject'
        for rs in RegisteredSubject.objects.all():
            print rs.subject_identifier, rs.subject_type
