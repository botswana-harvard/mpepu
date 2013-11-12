from django.test import TestCase
from django.utils import unittest

from apps.mpepu_infant.models import InfantFu
from .factories import InfantFuFactory


class InfantFuTests(TestCase):
    
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

        