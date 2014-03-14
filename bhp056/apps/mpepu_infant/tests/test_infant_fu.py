import factory
from datetime import datetime
from django.test import TestCase
from django.db import IntegrityError, transaction

from edc.core.bhp_content_type_map.classes import ContentTypeMapHelper
from edc.core.bhp_content_type_map.models import ContentTypeMap
from edc.core.bhp_content_type_map.tests.factories import ContentTypeMapFactory
from django.contrib.contenttypes.models import ContentType
from edc.subject.appointment.tests.factories import ConfigurationFactory
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.core.bhp_variables.tests.factories import StudySpecificFactory, StudySiteFactory
from edc.subject.entry.tests.factories import EntryFactory
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.visit_schedule.tests.factories import MembershipFormFactory, ScheduleGroupFactory, VisitDefinitionFactory
from edc.subject.rule_groups.classes import site_rule_groups

#from django.utils import unittest

from apps.mpepu_infant.models import InfantFu, InfantVisit
from apps.mpepu_maternal.models import  MaternalConsent
from .factories import InfantFuFactory, InfantVisitFactory


class InfantFuTests(TestCase):
    subject_consent = MaternalConsent
    consent_catalogue_name = 'mpepu V1'
    
    def setUp(self):
        site_lab_tracker.autodiscover()
        study_specific = StudySpecificFactory()
        StudySiteFactory()
        ConfigurationFactory()
        content_type_map_helper=ContentTypeMapHelper()
        content_type_map_helper.populate()
        content_type_map_helper.sync()
        maternal_consent_ct = ContentType.objects.get(app_label='mpepu_maternal', model='maternalconsent')
        content_type_map = ContentTypeMapFactory(content_type=maternal_consent_ct)#ContentTypeMap.objects.get(content_type__model='MaternalConsent'.lower())
        #TODO: Turn signal off
        consent_cat = ConsentCatalogueFactory(
             name=self.app_label,
             consent_type='study',
             content_type_map=content_type_map,
             version=2,
             start_datetime=study_specific.study_start_datetime,
             end_datetime=datetime(datetime.today().year + 5, 1, 1),
             add_for_app=self.app_label)
        #TODO: Turn signal onn
        #TODO: Creae atached model for maternal consent and link it with consent catalogue
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Infant Rando and F/Up')
        visit_tracking_content_type_map = ContentTypeMap.objects.get(content_type__model='infantvisit')
        visit_definition = VisitDefinitionFactory(grouping='infant', visit_tracking_content_type_map=visit_tracking_content_type_map)
        visit_definition.schedule_group.add(schedule_group)
        
        
    def test_save_get_infant_fu(self):   
        #self.assertTrue(InfantFuFactory(infant_visit = InfantVisit.objects.all()[0]))
        infant_fu = InfantFuFactory() 
        self.assertTrue(infant_fu)                  
           
#     def test_saving_infant_fu(self):
#         
#         fu = InfantFu()
#          
#         fu.physical_assessment = 'Yes'
#         fu.has_dx = 'Yes'
#         fu.diarrhea_illness = 'Yes'
#         
#         self.assertIsNone(fu.id, "Fu id should be None")
#         
#         fu.save()
#         
#         self.assertIsNotNone(fu.id, "Fu id should not be None")
#          
#         # now check we can find it in the database again
#         all_fu = InfantFu.objects.all()
#         self.assertEquals(len(all_fu), 1)
#         only_fu = all_fu[0]
#         self.assertEquals(only_fu, fu)
#  
#         # and check that it's saved its three attributes
#         self.assertEquals(only_fu.physical_assessment)
#         self.assertEquals(only_fu.has_dx)
#         self.assertEquals(only_fu.has_dx)