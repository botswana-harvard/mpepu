from django.test import TestCase
from datetime import datetime, date, timedelta
from django.core.exceptions import ValidationError

from edc.core.bhp_content_type_map.models import ContentTypeMap
from edc.core.bhp_variables.tests.factories import StudySiteFactory
from edc.core.identifier.models import SubjectIdentifier
from edc.entry_meta_data.models import ScheduledEntryMetaData, RequisitionMetaData
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.subject.appointment.models import Appointment
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.subject.entry.tests.factories import EntryFactory
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.registration.models import RegisteredSubject
from edc.subject.visit_schedule.classes import site_visit_schedules
from edc.subject.entry.models import Entry, LabEntry

from apps.mpepu_lab.lab_profiles import MpepuInfantProfile
from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration

from apps.mpepu_maternal.tests.factories import (MaternalConsentFactory, MaternalEligibilityPostFactory,
                                                 MaternalVisitFactory, MaternalLabDelFactory)
from apps.mpepu_infant.tests.factories import (InfantBirthFactory, InfantVisitFactory, InfantEligibilityFactory, 
                                               InfantBirthDataFactory, InfantArvProphFactory, InfantFuFactory,
                                               InfantStudyDrugFactory, InfantStoolCollectionFactory)
from apps.mpepu_infant_rando.tests import InfantRandomizationTests, RandoTestHelper
from apps.mpepu_infant_rando.models import InfantRando
from apps.mpepu_infant.models import InfantVisit

from apps.mpepu_infant.rule_groups import (InfantArvProphRuleGroup, InfantFuRuleGroup, InfantBirthDataRuleGroup,
                                           InfantStudyDrugRuleGroup)


class InfantRuleGroupsTests(TestCase):

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
        delivery_datetime = datetime.today() - timedelta(days=delivery_days_ago - 3)
#         print "Consent a mother"
        self.maternal_consent = MaternalConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=delivery_days_ago))
#         print "Consent: {}".format(self.maternal_consent)
        self.registered_subject = RegisteredSubject.objects.get(subject_identifier=self.maternal_consent.subject_identifier)
#         print 'check if mother is eligible'
        self.maternal_eligibility = MaternalEligibilityPostFactory(maternal_consent=self.maternal_consent, registered_subject=self.registered_subject, registration_datetime=datetime.today() - timedelta(days=delivery_days_ago))
#         print 'get the 2000M visit'
        self.m_appointment = Appointment.objects.get(registered_subject=self.registered_subject, visit_definition__code='2000M')
#         print 'create a maternal visit for the 2000M visit'
        self.maternal_visit = MaternalVisitFactory(appointment=self.m_appointment, report_datetime=datetime.today() - timedelta(days=delivery_days_ago))
#         print 'create a maternal_lab_del registering 2 of 2 infants'
        self.maternal_lab_del = MaternalLabDelFactory(maternal_visit=self.maternal_visit,
                                                         live_infants=1,
                                                         live_infants_to_register=1,
                                                         delivery_datetime=delivery_datetime,
                                                         has_ga='Yes',
                                                         ga=37,
                                                         )
#         print 'maternal lab del: {}'.format(self.maternal_lab_del)
#         print 'get registered subject of the infant'
        self.registered_subject = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'infant registered subject {}'.format(self.registered_subject)
        self.infant_birth = InfantBirthFactory(registered_subject=self.registered_subject, maternal_lab_del=self.maternal_lab_del, dob=delivery_datetime.date())
#         print 'infant birth {}'.format(self.infant_birth)
        self.appointment = Appointment.objects.get(registered_subject=self.registered_subject, visit_definition__code='2000')
        self.infant_visit = InfantVisitFactory(appointment=self.appointment, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy notrando')
        self.infant_eligibility = InfantEligibilityFactory(infant_birth=self.infant_birth, registered_subject=self.registered_subject)
#         print 'infant eligibility {}'.format(self.infant_eligibility)
        app_2010 = Appointment.objects.get(registered_subject=self.registered_subject, visit_definition__code='2010')
        self.visit_2010 = InfantVisitFactory(appointment=app_2010, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy rando today')
        app_2020 = Appointment.objects.get(registered_subject=self.registered_subject, visit_definition__code='2020')
        self.visit_2020 = InfantVisitFactory(appointment=app_2020, report_datetime=datetime.today(), reason='scheduled', study_status = 'onstudy rando ondrug')
#         self.fu = InfantFuFactory(infant_visit=visit_2010)
#         self.fu_physical = InfantFuPhysicalFactory(infant_fu=self.fu, infant_visit=visit_2010)
#         self.fu_dx = InfantFuDxFactory(infant_fu=self.fu, infant_visit=visit_2010)

    def test_infant_birth_data_rule_group(self):
        """If indicated 'Yes' for congenital anomalies in InfantBirthData then CongenitalAnomalies form is required"""
        print "Assert that upon creation of a 2000 visit Congenital anomalies is NEW"
        entry = Entry.objects.get(visit_definition__code='2000', model_name='infantcongenitalanomalies')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.infant_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NOT_REQUIRED')
 
        print "Assert that if has congenital anomalies is indicated as Yes then Congenital Anomalies form is New"
        birth_data = InfantBirthDataFactory(infant_birth=self.infant_birth, infant_visit=self.infant_visit, congenital_anomalities = 'Yes')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.infant_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NEW')
 
        print "Assert that if has congenital anomalies as indicated as No then Congenital Anomalies form is NOT_REQUIRED"
        birth_data.congenital_anomalities = 'No'
        birth_data.save()
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.infant_visit.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NOT_REQUIRED')

    def test_infant_arv_proph_rule_group(self):
        """If Infant was supposed to be taking NVP propylaxis, then 
        NVP Adherence should be required, otherwise it should be not required"""
        print "Assert that upon creation of a visit after 2000 InfantnNvpAdeherance is NEW"
        entry = Entry.objects.get(visit_definition__code='2010', model_name='infantnvpadherence')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2010.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status,'NEW')

        print "Assert that if prophylactic_nvp is No then InfantNvpAdherance is NOT_REQUIRED"
        infant_arv_proph = InfantArvProphFactory(infant_visit=self.visit_2010, prophylatic_nvp='No')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2010.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NOT_REQUIRED')

        print "Assert that if prophylactic_nvp is Yes then InfantNvpAdherance is NEW"
        infant_arv_proph.prophylatic_nvp = 'Yes'
        infant_arv_proph.save()
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2010.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')

    def test_infant_fu_rule_group_diarrhea(self):
        """Check InfantFu rule groups on diarrhea"""
        print "Assert that upon creation of a visit after 2000 InfantFuD is NEW"
        entry = Entry.objects.get(visit_definition__code='2010', model_name='infantfud')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2010.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')

        print "Assert that if diarrhea_illness is No then InfantFuD is NOT_REQUIRED"
        infant_fu = InfantFuFactory(infant_visit=self.visit_2010, diarrhea_illness = 'No')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2010.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NOT_REQUIRED')

        print "Assert that if diarrhea_illness is YES then InfantFuD is NEW"
        infant_fu.diarrhea_illness = 'Yes'
        infant_fu.save()
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2010.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')

    def test_infant_fu_rule_group_dx(self):
        """Check InfantFu rule groups on diagnosis"""
        print "Assert that upon creation of a visit after 2000 InfantFuDx is NEW"
        entry = Entry.objects.get(visit_definition__code='2010', model_name='infantfudx')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2010.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')

        print "Assert that if has_dx is No then InfantFuDx is NOT_REQUIRED"
        infant_fu = InfantFuFactory(infant_visit=self.visit_2010, has_dx = 'No')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2010.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NOT_REQUIRED')

        print "Assert that if has_dx is YES then InfantFuDx is NEW"
        infant_fu.has_dx = 'Yes'
        infant_fu.save()
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2010.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')

    def test_infant_study_drug_rule_group(self):
        """Check rule group on CTX """
        print "Assert that upon creation of a visit after 2000 InfantCtxPlaceboAdh is NEW"
        entry = Entry.objects.get(visit_definition__code='2020', model_name='infantctxplaceboadh')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2020.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')

        print "Assert that if on_placebo_status is No then InfantCtxPlaceboAdh is NOT_REQUIRED"
        study_drug = InfantStudyDrugFactory(infant_visit=self.visit_2020, on_placebo_status = 'No')
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2020.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NOT_REQUIRED')

        print "Assert that if on_placebo_status is YES then InfantCtxPlaceboAdh is NEW"
        study_drug.on_placebo_status = 'Yes'
        study_drug.save()
        meta_data = ScheduledEntryMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2020.appointment, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')

    def test_stool_sampling_rule_group(self):
        """Check rule group on stool sampling"""
        print "Assert that upon creation of a 2010 visit, stool sample is required."
        lab_entry = LabEntry.objects.get(model_name='infantrequisition', requisition_panel__name='Stool storage', visit_definition__code='2010')
#         requisition = RequisitionMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2010.appointment, lab_entry=lab_entry)
#         self.assertEqual(requisition.entry_status, 'NEW')

        print "Assert that if sample_obtained is indicated as Yes then InfantStoolCollection is New"
        stool = InfantStoolCollectionFactory(infant_visit=self.visit_2010, sample_obtained='Yes')
        requisition = RequisitionMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2010.appointment, lab_entry=lab_entry)
        self.assertEqual(requisition.entry_status, 'NEW')

        print "Assert that if sample_obtained is indicated as No then InfantStoolCollection is New"
        stool.sample_obtained = 'No'
        stool.save()
        requisition = RequisitionMetaData.objects.get(registered_subject=self.registered_subject, appointment=self.visit_2010.appointment, lab_entry=lab_entry)
        self.assertEqual(requisition.entry_status, 'NOT_REQUIRED')
