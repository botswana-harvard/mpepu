import re
import pprint
from datetime import datetime, date, timedelta
from django.test import TestCase
from django.db.models import get_app, get_models
from django.core.exceptions import ValidationError
from edc.core.identifier.exceptions import IdentifierError
from edc.subject.lab_tracker.classes import lab_tracker
from bhp_entry_rules.classes import rule_groups
from edc.core.bhp_variables.models import StudySpecific, StudySite
from edc.core.bhp_variables.tests.factories import StudySpecificFactory, StudySiteFactory
from edc.subject.registration.models import RegisteredSubject
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from bhp_entry.tests.factories import EntryFactory
from bhp_entry.models import ScheduledEntryBucket
from edc.subject.appointment.models import Appointment
from edc.subject.appointment.tests.factories import ConfigurationFactory
from edc.subject.visit_schedule.tests.factories import MembershipFormFactory, ScheduleGroupFactory, VisitDefinitionFactory
from bhp_content_type_map.classes import ContentTypeMapHelper
from bhp_content_type_map.models import ContentTypeMap
from ..models import MaternalVisit, MaternalConsent, MaternalOffStudy, MaternalEligibilityAnte, MaternalEligibilityPost, MaternalPostReg
from ..tests.factories import MaternalConsentFactory, MaternalOffStudyFactory, MaternalVisitFactory, MaternalEligibilityAnteFactory, MaternalLabDelFactory
from edc.core.identifier.models import SubjectIdentifier, Sequence
from edc.subject.off_study.exceptions import SubjectOffStudyError, SubjectOffStudyDateError
from mpepu_infant.models import InfantBirth, InfantPreEligibility, InfantFu, InfantFeeding
from factories import InfantVisitFactory, InfantBirthFactory, InfantBirthDataFactory, InfantEligibilityFactory, InfantPreEligibilityFactory, InfantOffStudyFactory, InfantArvProphFactory, InfantArvProphModFactory
from edc.subject.consent.classes import ConsentHelper
from mpepu_infant_rando.classes import Eligibility


class InfantBirthTests(TestCase):
    subject_consent = MaternalConsent
    consent_catalogue_name = 'mpepu V1'

    def test_p1(self):
        lab_tracker.autodiscover()
        rule_groups.autodiscover()
        StudySpecificFactory()
        study_site = StudySiteFactory()
        ConfigurationFactory()
        content_type_map_helper = ContentTypeMapHelper()
        content_type_map_helper.populate()
        content_type_map_helper.sync()
        print 'setup the consent catalogue'
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
        GA = 0
        DAYS = 1
        DAYS_UPPER = 2
        for delivery_days_ago in range(30, 42):
            for criteria in [(33, 27, 34), (34, 27, 34), (35, 27, 34), (36, 13, 27), (37, 13, 27), (38, 13, 27), (39, 13, 27)]:
                delivery_datetime = datetime.today() - timedelta(days=delivery_days_ago - 3)
                maternal_consent = MaternalConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=delivery_days_ago))
                registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
                maternal_eligibility = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject, registration_datetime=datetime.today() - timedelta(days=delivery_days_ago))
                appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
                maternal_visit = MaternalVisitFactory(appointment=appointment, report_datetime=datetime.today() - timedelta(days=delivery_days_ago))
                print 'create a maternal lab-del: registering 2 of 1 infant'
                print '    GA={0}, DAYS={1}, UPPER={2}, DELIVERY_DAYS_AGO={3}'.format(criteria[GA], criteria[DAYS], criteria[DAYS_UPPER], delivery_days_ago)
                maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit,
                                                         live_infants=2,
                                                         live_infants_to_register=1,
                                                         delivery_datetime=delivery_datetime,
                                                         has_ga='Yes',
                                                         ga=criteria[GA],
                                                         )
                print '    {0}'.format(maternal_lab_del)
                self.assertIsNotNone(SubjectIdentifier.objects.get(identifier='{0}-25'.format(maternal_consent.subject_identifier)))
                registered_subject = RegisteredSubject.objects.get(relative_identifier=maternal_consent.subject_identifier)
                print '    confirm not appointments exist for infant'
                self.assertEquals([appointment.visit_definition.code for appointment in Appointment.objects.filter(registered_subject=registered_subject).order_by('visit_definition__code')], [])

                print '    add infant birth'
                infant_birth = InfantBirthFactory(registered_subject=registered_subject, maternal_lab_del=maternal_lab_del)
                print '    {0}'.format(infant_birth)
                print '    confirm infant appointments exist, 2000, 2010 were created'
                self.assertEquals([appointment.visit_definition.code for appointment in Appointment.objects.filter(registered_subject=registered_subject).order_by('visit_definition__code')], ['2000', '2010'])
                #print 'Infant 2000 at {0}'.format(Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000').appt_datetime)
                #print 'Infant 2010 at {0}'.format(Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2010').appt_datetime)
                #print '    add an infant visit'
                appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000')
                infant_visit = InfantVisitFactory(appointment=appointment, report_datetime=datetime.today(), reason='scheduled')
                #print '    {0}'.format(infant_visit)
                appt_2000 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2000').appt_datetime
                appt_2010 = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2010').appt_datetime
                print '    confirm {1}-{2} days between appointments for GA={0}'.format(*criteria)
                self.assertTrue((date(appt_2010.year, appt_2010.month, appt_2010.day) - date(appt_2000.year, appt_2000.month, appt_2000.day)).days in range(criteria[DAYS], criteria[DAYS_UPPER]),
                                '{0} is not in {1}. using {2}, {3}'.format((date(appt_2010.year, appt_2010.month, appt_2010.day) - date(appt_2000.year, appt_2000.month, appt_2000.day)).days, range(criteria[DAYS], criteria[DAYS_UPPER]), appt_2000, appt_2010))
                appt_date = date(appt_2010.year, appt_2010.month, appt_2010.day)
                delivery_date = date(delivery_datetime.year, delivery_datetime.month, delivery_datetime.day)
                diffdays = (appt_date - delivery_date).days
                print '    GOT {0} days for a {1}'.format(diffdays, appt_date.strftime("%A"))
                print '    confirm days calculated from delivery date'
                print '    raw calc puts appt on {0} {1}'.format((delivery_date + timedelta(days=criteria[DAYS])).strftime("%A"), delivery_date + timedelta(days=criteria[DAYS]))
                while True:
                    if (delivery_date + timedelta(days=criteria[DAYS])).strftime("%A") == 'Saturday':
                        print '        appt date would have fallen on {0}, advance +2 days'.format(delivery_date.strftime("%A"))
                        delivery_date = delivery_date + timedelta(days=2)
                    elif (delivery_date + timedelta(days=criteria[DAYS])).strftime("%A") == 'Sunday':
                        print '        appt date would have fallen on {0}, advance +1 days'.format(delivery_date.strftime("%A"))
                        delivery_date = delivery_date + timedelta(days=1)
                    else:
                        break
                self.assertEqual(delivery_date + timedelta(days=criteria[DAYS]), appt_date)

    def test_p2(self):
        lab_tracker.autodiscover()
        StudySpecificFactory()
        study_site = StudySiteFactory()
        ConfigurationFactory()
        content_type_map_helper = ContentTypeMapHelper()
        content_type_map_helper.populate()
        content_type_map_helper.sync()
        print 'setup the consent catalogue'
        content_type_map = ContentTypeMap.objects.get(content_type__model=self.subject_consent._meta.object_name.lower())
        consent_catalogue = ConsentCatalogueFactory(name=self.consent_catalogue_name, content_type_map=content_type_map)
        consent_catalogue.add_for_app = 'mpepu_maternal'
        consent_catalogue.save()
        consent_catalogue.add_for_app = 'mpepu_infant'
        consent_catalogue.save()

        maternal_visit_tracking_content_type_map = ContentTypeMap.objects.get(content_type__model='maternalvisit')
        infant_visit_tracking_content_type_map = ContentTypeMap.objects.get(content_type__model='infantvisit')

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

        content_type_map = ContentTypeMap.objects.get(content_type__model=InfantBirth._meta.object_name.lower())
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Infant Birth')
        visit_definition = VisitDefinitionFactory(code='2000', title='Infant Birth', grouping='infant', time_point=0, base_interval=0, base_interval_unit='D', visit_tracking_content_type_map=infant_visit_tracking_content_type_map)
        visit_definition.schedule_group.add(schedule_group)
        visit_definition = VisitDefinitionFactory(code='2010', title='Randomization', grouping='infant', time_point=10, base_interval=27, base_interval_unit='D', visit_tracking_content_type_map=infant_visit_tracking_content_type_map)
        visit_definition.schedule_group.add(schedule_group)

        # add entries to 2010
        content_type_map = ContentTypeMap.objects.get(content_type__model=InfantFu._meta.object_name.lower())
        entry = EntryFactory(visit_definition=visit_definition, content_type_map=content_type_map)
        content_type_map = ContentTypeMap.objects.get(content_type__model=InfantFeeding._meta.object_name.lower())
        entry = EntryFactory(visit_definition=visit_definition, content_type_map=content_type_map)

        # add entries to 2015
        content_type_map = ContentTypeMap.objects.get(content_type__model=InfantPreEligibility._meta.object_name.lower())
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Infant Deferred Eligibility')
        visit_definition = VisitDefinitionFactory(code='2015', title='Randomization II', grouping='infant', time_point=15, base_interval=27, base_interval_unit='D', visit_tracking_content_type_map=infant_visit_tracking_content_type_map)
        visit_definition.schedule_group.add(schedule_group)
        content_type_map = ContentTypeMap.objects.get(content_type__model=InfantFu._meta.object_name.lower())
        entry = EntryFactory(visit_definition=visit_definition, content_type_map=content_type_map)
        content_type_map = ContentTypeMap.objects.get(content_type__model=InfantFeeding._meta.object_name.lower())
        entry = EntryFactory(visit_definition=visit_definition, content_type_map=content_type_map)

        AGE = 0
        DAYS = 2
        DAYS_UPPER = 3
        GA = 1
        WGHT = 4
        CJ = 5
        AN = 6
        STAT = 7
        for eligibility_criteria in [
                                     #(35, 33, 27, 34, 2.25, 'No', 'No', 'fail'),
                                     #(26, 33, 27, 34, 2.25, 'No', 'No', 'fail'),
                                     #(13, 37, 27, 34, 2.25, 'No', 'No', 'fail'),
                                     (13, 37, 13, 27, 2.25, 'No', 'No', 'fail'),
                                     #(27, 37, 27, 34, 2.25, 'No', 'No', 'pass'),
                                     #(27, 36, 13, 27, 2.5, 'No', 'No', 'pass'),
                                     #(28, 36, 13, 27, 2.5, 'No', 'No', 'pass'),
                                     #(13, 36, 13, 27, 2.5, 'No', 'No', 'pass'),
                                     #(13, 36, 13, 27, 2.5, 'Yes', 'No', 'fail'),
                                     #(13, 36, 13, 27, 2.5, 'Yes', 'No', 'fail'),
                                     #(13, 36, 13, 27, 2.0, 'No', 'No', 'fail'),
                                     #(12, 36, 13, 27, 2.5, 'No', 'No', 'fail')
                                     ]:
            print 'criteria {0}'.format(eligibility_criteria)
            delivery_datetime, infant_birth, registered_subject = self.prepare_maternal(study_site, (eligibility_criteria[GA], eligibility_criteria[DAYS], eligibility_criteria[DAYS_UPPER]), eligibility_criteria[AGE])
            delivery_date = date(delivery_datetime.year, delivery_datetime.month, delivery_datetime.day)
            self.assertTrue(Appointment.objects.filter(registered_subject=registered_subject).count() == 2)
            appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2010', visit_instance='0')
            print '    {0} days >= {1}'.format(abs((delivery_datetime - appointment.appt_datetime).days), eligibility_criteria[2])
            self.assertGreaterEqual(abs((delivery_datetime - appointment.appt_datetime).days), eligibility_criteria[2])
            print '    {0} days < {1}'.format(abs((delivery_datetime - appointment.appt_datetime).days), eligibility_criteria[3])
            self.assertLess(abs((delivery_datetime - appointment.appt_datetime).days), eligibility_criteria[3])
            print '    {0}'.format(', '.join([appt.appt_datetime.strftime('%Y-%m-%d') for appt in Appointment.objects.filter(registered_subject=registered_subject).order_by('appt_datetime')]))
            print '    attempt to complete infant eligibility for infant aged {0} days'.format(abs((delivery_date - date.today()).days))
            allow_rando = Eligibility().check(
                current_consent_version=2,
                dob=delivery_date,
                ga=eligibility_criteria[GA],
                weight=eligibility_criteria[WGHT],
                clinical_jaundice=eligibility_criteria[CJ],
                anemia_neutropenia=eligibility_criteria[AN],
                exception_cls=ValidationError,
                suppress_exception=True)
            if allow_rando:
                infant_eligibility = InfantEligibilityFactory(
                    infant_birth=infant_birth,
                    registered_subject=registered_subject,
                    weight=eligibility_criteria[WGHT],
                    clinical_jaundice=eligibility_criteria[CJ],
                    anemia_neutropenia=eligibility_criteria[AN])
                print '    completed infant eligibility'.format(infant_eligibility)
                print '    confirm 2015 does not exist'
                self.assertEqual(eligibility_criteria[STAT], 'pass')
                self.assertEquals([appointment.visit_definition.code for appointment in Appointment.objects.filter(registered_subject=registered_subject).order_by('visit_definition__code')],
                                  ['2000', '2010'])
            elif not allow_rando and eligibility_criteria[AGE] >= 13 and eligibility_criteria[AGE] <= 33:
                print '    allow_rando={0}'.format(allow_rando)
                self.assertRaises(ValidationError, InfantEligibilityFactory,
                    infant_birth=infant_birth,
                    registered_subject=registered_subject,
                    weight=eligibility_criteria[WGHT],
                    clinical_jaundice=eligibility_criteria[CJ],
                    anemia_neutropenia=eligibility_criteria[AN])
                self.assertEqual(eligibility_criteria[STAT], 'fail')
                print '    add InfantVisit 2000'
                appointment = Appointment.objects.get(visit_definition__code='2000', registered_subject=registered_subject)
                infant_visit = InfantVisitFactory(appointment=appointment, reason='scheduled')
                print '    attempt add InfantVisit 2010 to trigger ValidationError'
                appointment = Appointment.objects.get(visit_definition__code='2010', registered_subject=registered_subject)
                self.assertRaises(ValidationError, InfantVisitFactory, appointment=appointment, reason='scheduled')
                print '    complete pre-eligibility form'
                infant_pre_eligibility = InfantPreEligibilityFactory(
                    infant_birth=infant_birth,
                    registered_subject=registered_subject,
                    weight=eligibility_criteria[WGHT],
                    clinical_jaundice=eligibility_criteria[CJ],
                    anemia_neutropenia=eligibility_criteria[AN])
                print '    confirm 2015 created'
                self.assertEqual(Appointment.objects.filter(registered_subject=registered_subject).count(), 3)
                self.assertEquals([appointment.visit_definition.code for appointment in Appointment.objects.filter(registered_subject=registered_subject).order_by('visit_definition__code')],
                          ['2000', '2010', '2015'])
                print '    confirm appointment date set for 2015'
                appointment = Appointment.objects.get(visit_definition__code='2015', registered_subject=registered_subject)
                print '    2015={0}'.format(appointment.appt_datetime)
                print '    {0} days >= {1}'.format(abs((delivery_datetime - appointment.appt_datetime).days), 27)
                self.assertGreaterEqual(abs((delivery_datetime - appointment.appt_datetime).days), 27)
                #infant_visit = InfantVisitFactory(appointment=appointment, report_datetime=datetime.today(), reason='scheduled')
            elif not allow_rando and eligibility_criteria[AGE] > 33:
                print '    allow_rando={0} but age={1}'.format(allow_rando, eligibility_criteria[AGE])
                self.assertRaises(ValidationError, InfantEligibilityFactory,
                    infant_birth=infant_birth,
                    registered_subject=registered_subject,
                    weight=eligibility_criteria[WGHT],
                    clinical_jaundice=eligibility_criteria[CJ],
                    anemia_neutropenia=eligibility_criteria[AN])
                self.assertEqual(eligibility_criteria[STAT], 'fail')
                print '    add InfantVisit 2000'
                appointment = Appointment.objects.get(visit_definition__code='2000', registered_subject=registered_subject)
                infant_visit = InfantVisitFactory(appointment=appointment, reason='scheduled')
                print '    attempt add InfantVisit 2010 to trigger ValidationError'
                appointment = Appointment.objects.get(visit_definition__code='2010', registered_subject=registered_subject)
                self.assertRaises(ValidationError, InfantVisitFactory, appointment=appointment, reason='scheduled')
                print '    attempt to complete pre-eligibility form'
                print '    complete pre-eligibility form'
                InfantPreEligibilityFactory(
                    infant_birth=infant_birth,
                    registered_subject=registered_subject,
                    weight=eligibility_criteria[WGHT],
                    clinical_jaundice=eligibility_criteria[CJ],
                    anemia_neutropenia=eligibility_criteria[AN])
                print '    confirm 2015 NOT created'
                self.assertEqual(Appointment.objects.filter(registered_subject=registered_subject).count(), 2)
                self.assertEquals([appointment.visit_definition.code for appointment in Appointment.objects.filter(registered_subject=registered_subject).order_by('visit_definition__code')],
                          ['2000', '2010'])
            elif eligibility_criteria[AGE] < 13:
                print '    allow_rando={0} but age={1}'.format(allow_rando, eligibility_criteria[AGE])
                self.assertRaises(ValidationError, InfantEligibilityFactory,
                    infant_birth=infant_birth,
                    registered_subject=registered_subject,
                    weight=eligibility_criteria[WGHT],
                    clinical_jaundice=eligibility_criteria[CJ],
                    anemia_neutropenia=eligibility_criteria[AN])
                self.assertEqual(eligibility_criteria[STAT], 'fail')
                print '    add InfantVisit 2000'
                appointment = Appointment.objects.get(visit_definition__code='2000', registered_subject=registered_subject)
                infant_visit = InfantVisitFactory(appointment=appointment, reason='scheduled')
                print '    attempt add InfantVisit 2010 to trigger ValidationError'
                appointment = Appointment.objects.get(visit_definition__code='2010', registered_subject=registered_subject)
                self.assertRaises(ValidationError, InfantVisitFactory, appointment=appointment, reason='scheduled')
                print '    attempt to complete pre-eligibility form'
                print '    complete pre-eligibility form'
                self.assertRaises(ValidationError, InfantPreEligibilityFactory,
                    infant_birth=infant_birth,
                    registered_subject=registered_subject,
                    weight=eligibility_criteria[WGHT],
                    clinical_jaundice=eligibility_criteria[CJ],
                    anemia_neutropenia=eligibility_criteria[AN])
                print '    confirm 2015 NOT created'
                self.assertEqual(Appointment.objects.filter(registered_subject=registered_subject).count(), 2)
                self.assertEquals([appointment.visit_definition.code for appointment in Appointment.objects.filter(registered_subject=registered_subject).order_by('visit_definition__code')],
                          ['2000', '2010'])
            else:
                raise TypeError('Impossible test case? unhandled?')

    def prepare_maternal(self, study_site, criteria, delivery_days_ago):
        GA = 0
        DAYS = 1
        DAYS_UPPER = 2
        delivery_datetime = datetime.today() - timedelta(days=delivery_days_ago)
        maternal_consent = MaternalConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        maternal_eligibility = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject, registration_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        maternal_visit = MaternalVisitFactory(appointment=appointment, report_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print 'create a maternal lab-del: registering 2 of 1 infant'
        print '    GA={0}, DAYS={1}, UPPER={2}, DELIVERY_DAYS_AGO={3}'.format(criteria[GA], criteria[DAYS], criteria[DAYS_UPPER], delivery_days_ago)
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit,
                                                 live_infants=2,
                                                 live_infants_to_register=1,
                                                 delivery_datetime=delivery_datetime,
                                                 has_ga='Yes',
                                                 ga=criteria[GA],
                                                 )
        print '    {0}'.format(maternal_lab_del)
        self.assertIsNotNone(SubjectIdentifier.objects.get(identifier='{0}-25'.format(maternal_consent.subject_identifier)))
        registered_subject = RegisteredSubject.objects.get(relative_identifier=maternal_consent.subject_identifier)
        print '    confirm not appointments exist for infant'
        self.assertEquals([appointment.visit_definition.code for appointment in Appointment.objects.filter(registered_subject=registered_subject).order_by('visit_definition__code')], [])
        print '    add infant birth'
        infant_birth = InfantBirthFactory(registered_subject=registered_subject, maternal_lab_del=maternal_lab_del, dob=date(delivery_datetime.year, delivery_datetime.month, delivery_datetime.day))
        print '    {0}'.format(infant_birth)
        print '    confirm infant appointments exist, 2000, 2010 were created'
        self.assertEquals([appointment.visit_definition.code for appointment in Appointment.objects.filter(registered_subject=registered_subject).order_by('visit_definition__code')],
                          ['2000', '2010'])
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2010')
        print '    {0}, {1}'.format(delivery_datetime, appointment.appt_datetime)
        return delivery_datetime, infant_birth, registered_subject
    
    
#         print 'complete infant birth data'
#             print 'confirm appt date was changed to __. (Criteria are : ga >=36, weight >=2.5, clinical_jaundice=No, anemia_neutropenia=No)'
#             infant_birth_data = InfantBirthDataFactory(infant_visit=infant_visit, infant_birth=infant_birth, infant_birth_weight=3.5, )
#             print 'Infant 2010 at {0}'.format(Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='2010').appt_datetime)

       
        