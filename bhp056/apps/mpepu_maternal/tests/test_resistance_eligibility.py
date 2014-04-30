from django.contrib import admin
from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import ResistanceEligibility, ResistanceConsent, MaternalConsent
from .factories import ResistanceEligibilityFactory

from edc.core.bhp_content_type_map.classes import ContentTypeMapHelper
from edc.core.bhp_content_type_map.models import ContentTypeMap
from edc.core.bhp_variables.tests.factories import StudySpecificFactory, StudySiteFactory
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.subject.lab_tracker.classes import site_lab_tracker

from apps.mpepu_maternal.tests.factories import ResistanceConsentFactory, MaternalConsentFactory


class ResistanceEligibilityTests(TestCase):

    app_label = 'mpepu_maternal'

    def test_maternal_eligibility(self):

        site_lab_tracker.autodiscover()
        study_specific = StudySpecificFactory()
        StudySiteFactory()

        content_type_map_helper = ContentTypeMapHelper()
        content_type_map_helper.populate()
        content_type_map_helper.sync()
        content_type_map = ContentTypeMap.objects.get(model__iexact=ResistanceConsent._meta.object_name)
        ConsentCatalogueFactory(
            name=self.app_label,
            content_type_map=content_type_map,
            consent_type='sub-study',
            version=1,
            start_datetime=study_specific.study_start_datetime,
            end_datetime=datetime(datetime.today().year + 5, 1, 1),
            add_for_app=self.app_label)

        maternal_consent = MaternalConsentFactory(first_name='MELISSA', gender='F', dob='1994-03-25', identity='111121111')
        self.assertEqual(MaternalConsent.objects.all().count(), 1)
        print maternal_consent.subject_identifier
        resistance_consent = ResistanceConsentFactory(first_name='MELISSA', gender='F', dob='1994-03-25', identity='111121111')
        self.assertEqual(ResistanceConsent.objects.all().count(), 1)
        print resistance_consent.subject_identifier
        print 'resistance consent does exists'

        print 'assert there is no eligibility'
        self.assertEqual(ResistanceEligibility.objects.all().count(), 0)

        print 'create eligibility for mother'
        eligibility = ResistanceEligibilityFactory(co_enrolled='Yes', status_evidence='Yes', lates_cd4=250, who_illness='No')
        self.assertEqual(ResistanceEligibility.objects.all().count(), 1)
        print eligibility
