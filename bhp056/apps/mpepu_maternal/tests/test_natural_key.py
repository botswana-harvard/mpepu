import re
import pprint
from datetime import datetime
from django.core import serializers
from edc.core.crypto_fields.classes import FieldCryptor
from django.db.models import get_app, get_models
from edc.testing.classes import BaseNaturalKeyTests
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.device.sync.classes import SerializeToTransaction, DeserializeFromTransaction
from edc.core.bhp_variables.models import StudySpecific, StudySite
from edc.core.bhp_variables.tests.factories import StudySpecificFactory, StudySiteFactory
from edc.subject.registration.models import RegisteredSubject
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.subject.appointment.models import Appointment
from edc.subject.visit_schedule.tests.factories import MembershipFormFactory, ScheduleGroupFactory, VisitDefinitionFactory
from edc.core.bhp_content_type_map.classes import ContentTypeMapHelper
from edc.core.bhp_content_type_map.models import ContentTypeMap
from ..models import MaternalVisit, MaternalConsent, MaternalEligibilityAnte, MaternalEligibilityPost, MaternalPostReg
from ..tests.factories import MaternalConsentFactory, MaternalVisitFactory, MaternalEligibilityAnteFactory


class NaturalKeyTests(BaseNaturalKeyTests):

    app_label = 'mpepu_maternal'
    subject_consent = MaternalConsent
    consent_catalogue_name = 'mpepu V1'
    visit_model = MaternalVisit

    def test_p3(self):
        site_lab_tracker.autodiscover()
        StudySpecificFactory()
        study_site = StudySiteFactory()
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
        visit_definition = VisitDefinitionFactory(code='1000M', title='Maternal Ante Natal Registration', grouping='maternal')
        visit_definition.schedule_group.add(schedule_group)

        content_type_map = ContentTypeMap.objects.get(content_type__model=MaternalEligibilityPost._meta.object_name.lower())
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Maternal Post Partum Reg', grouping_key='ELIGIBILITY')
        visit_definition = VisitDefinitionFactory(code='2000M', title='Maternal Post Natal Registration', grouping='maternal')
        visit_definition.schedule_group.add(schedule_group)

        content_type_map = ContentTypeMap.objects.get(content_type__model=MaternalPostReg._meta.object_name.lower())
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Post Partum Follow-up')
        visit_definition = VisitDefinitionFactory(code='2010M', title='Infant Randomization', grouping='maternal')
        visit_definition.schedule_group.add(schedule_group)

        print 'consent a mother'
        maternal_consent = MaternalConsentFactory(study_site=study_site)
        print maternal_consent.subject_identifier
        print 'get subject registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        print 'enroll mother ante natal'
        maternal_eligibility_ante = MaternalEligibilityAnteFactory(maternal_consent=maternal_consent, registered_subject=registered_subject)

        instances = [maternal_eligibility_ante]

        print 'test natural key / get_by_natural_key on subject_visit'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000M')
        subject_visit = MaternalVisitFactory(appointment=appointment)
        instances.append(subject_visit)
        print 'NOTE, not all models tested'
        print 'test serialization.'
        self.serialize_deserialize(instances)
