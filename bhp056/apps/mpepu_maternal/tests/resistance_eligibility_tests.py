from django.contrib import admin
from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import ResistanceEligibility
from .factories import ResistanceEligibilityFactory

from edc.lab.lab_profile.classes import site_lab_profiles
from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration
from apps.mpepu_maternal.visit_schedule import MpepuResistanceStudyVisitSchedule


class ResistanceEligibilityTests(TestCase):

    def test_maternal_eligibility(self):

        admin.autodiscover()
        site_lab_profiles.autodiscover()
        MpepuAppConfiguration()
        MpepuResistanceStudyVisitSchedule().build()

        """when mother is eligible"""
        self.assertEquals(0, ResistanceEligibility.objects.count(), "There should be no saved Resistance Eligibility objects")
        ResistanceEligibilityFactory(co_enrolled='Yes', status_evidence='Yes', lates_cd4=250, who_illness='No')
        self.assertEquals(1, ResistanceEligibility.objects.count(), "There should be one Eligibility saved.")
