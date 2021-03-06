from datetime import datetime
from django.test import TestCase

from edc.core.bhp_content_type_map.classes import ContentTypeMapHelper
from edc.core.bhp_content_type_map.models import ContentTypeMap
from edc.core.bhp_variables.tests.factories import StudySpecificFactory, StudySiteFactory
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.registration.models import RegisteredSubject

from apps.mpepu_maternal.tests.factories import ResistanceConsentFactory, MaternalConsentFactory

from ..models import ResistanceConsent, MaternalConsent


class ResistanceConsentTests(TestCase):

    app_label = 'mpepu_maternal'

    def test_p1(self):
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

        print 'confirming that a maternal consent exists'
        consent = MaternalConsentFactory(first_name='MELISSA', gender='F', dob='1994-03-25', identity='111121111')
        self.assertEqual(MaternalConsent.objects.all().count(), 1)
        print consent.subject_identifier

        print 'assert one maternal consent registers one registered_subject'
        self.assertEqual(MaternalConsent.objects.all().count(), RegisteredSubject.objects.all().count())

        print 'consent first resistance mother'
        consent1 = ResistanceConsentFactory(first_name='MELISSA', gender='F', dob='1994-03-25', identity='111121111')
        self.assertEqual(ResistanceConsent.objects.all().count(), 1)
        print consent1.subject_identifier

        print 'assert that the subject identifier of both consents remains the same'
        self.assertEqual(consent.subject_identifier, consent1.subject_identifier)

        print 'assert that the subject identifier on consent1 == subject identifier in registered_subject'
        self.assertEqual(consent1.subject_identifier, RegisteredSubject.objects.get(subject_identifier=consent1.subject_identifier).subject_identifier)
