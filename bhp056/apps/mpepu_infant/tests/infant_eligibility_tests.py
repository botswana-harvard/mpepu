from django.test import TestCase
from django.core.exceptions import ValidationError
from edc.subject.rule_groups.classes import rule_groups
from edc.core.bhp_variables.tests.factories import StudySpecificFactory, StudySiteFactory
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.registration.models import RegisteredSubject
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.subject.entry.tests.factories import EntryFactory
from edc.subject.appointment.models import Appointment
from edc.subject.appointment.tests.factories import ConfigurationFactory
from edc.subject.visit_schedule.tests.factories import MembershipFormFactory, ScheduleGroupFactory, VisitDefinitionFactory
from edc.core.bhp_content_type_map.classes import ContentTypeMapHelper
from edc.core.bhp_content_type_map.models import ContentTypeMap
from ..models import InfantBirth, InfantEligibility, InfantPreEligibility
from factories import InfantVisitFactory, InfantBirthFactory, InfantEligibilityFactory, InfantPreEligibilityFactory


class InfantEligibilityTests(TestCase):

    def create_only_2010_visit_when_eligibility_saved(self):
        infant_birth_factory = InfantBirthFactory()
        infant_eligibility_factory = InfantEligibilityFactory()
        infant_visit_factory = InfantVisitFactory()
