import factory
from django.test import TestCase
from django.db import transaction

from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.subject.lab_tracker.classes import site_lab_tracker

from apps.mpepu_lab.lab_profiles import MpepuInfantProfile
from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration
from apps.mpepu_infant.visit_schedule import MpepuInfantRandoMonthlyVisitSchedule

from .factories import InfantOffDrugFactory


class InfantOffDrugTests(TestCase):
    def setUp(self):
        try:
            site_lab_profiles.register(MpepuInfantProfile())
            MpepuAppConfiguration()
        except AlreadyRegistered:
            pass
        site_lab_tracker.autodiscover()
        try:
            with transaction.atomic():
                MpepuInfantRandoMonthlyVisitSchedule().build()
        except Exception:
            pass
        
    def test_off_drug(self):
        ios = InfantOffDrugFactory()
        print ios