from datetime import date
from dateutil.relativedelta import relativedelta

from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import ResistanceEligibility
# from .factories import ResistanceEligibilityFactory


class ResistanceEligibilityTests(TestCase):

    def test_maternal_eligibility(self):
        """when mother is eligible"""
        self.assertEquals(0, ResistanceEligibility.objects.count(), "There should be no saved Resistance Eligibility objects")
        ResistanceEligibility.objects.create(
                                        co_enrolled='Yes',
                                        status_evidence='Yes',
                                        lates_cd4=250,
                                        who_illness='No'
                                        )
        self.assertEquals(1, ResistanceEligibility.objects.count(), "There should be one Eligibility saved.")


#     def test_maternal_ineligibility(self):
#         """when mother is ineligible"""
#         self.assertEquals(0, ResistanceEligibility.objects.count(), "There should be no saved Resistance Eligibility objects")
#         ResistanceEligibilityFactory.create(
#                                         co_enrolled = 'Yes',
#                                         status_evidence = 'Yes',
#                                         lates_cd4 = 250,
#                                         who_illness = 'No'
#                                         )
#         self.assertEquals(1, ResistanceEligibility.objects.count(), "There should be one Eligibility saved.")
