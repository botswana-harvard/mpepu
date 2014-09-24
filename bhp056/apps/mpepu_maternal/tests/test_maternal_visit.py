from datetime import datetime, date, timedelta
from django.test import TestCase
from django.core.exceptions import ValidationError

from edc.core.bhp_variables.tests.factories import StudySiteFactory
from edc.core.identifier.models import Sequence
from edc.core.identifier.models import SubjectIdentifier
from edc.entry_meta_data.models import ScheduledEntryMetaData
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.subject.appointment.models import Appointment
from edc.subject.entry.models import Entry
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.registration.models import RegisteredSubject
from edc.subject.visit_schedule.classes import site_visit_schedules

from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration
from apps.mpepu_infant.tests.factories import InfantBirthFactory
from apps.mpepu_lab.lab_profiles import MpepuMaternalProfile
from apps.mpepu_maternal.forms import MaternalEligibilityPostForm, MaternalEligibilityAnteForm, MaternalConsentForm
from apps.mpepu_maternal.models import MaternalConsent, MaternalVisit, MaternalEligibilityPost
from apps.mpepu_maternal.visit_schedule import MpepuMaternalPostNatalVisitSchedule, MpepuMaternalAnteNatalVisitSchedule, MpepuMaternalPostPartumVisitSchedule

from .factories import( MaternalConsentFactory, MaternalEligibilityPostFactory, MaternalEligibilityAnteFactory, MaternalPostRegFactory,
                        MaternalVisitFactory, MaternalLabDelFactory)


class MaternalVisitTests(TestCase):

    def setUp(self):
        try:
            site_lab_profiles.register(MpepuMaternalProfile())
        except AlreadyRegistered:
            pass
        MpepuAppConfiguration().prepare()
        site_lab_tracker.autodiscover()
        site_visit_schedules.autodiscover()
        site_visit_schedules.build_all()
        study_site = StudySiteFactory()
        print "Consenting a mother"
        MaternalConsent.objects.all().delete()
        self.maternal_consent = MaternalConsentFactory(study_site=study_site)
        print "Maternal Consent: {}".format(self.maternal_consent)
        print 'get maternal registered subject'
        self.registered_subject = RegisteredSubject.objects.get(subject_identifier=self.maternal_consent.subject_identifier)
        print "check if mother is eligible"
        self.post_elibility = MaternalEligibilityPostFactory(maternal_consent=self.maternal_consent, registered_subject=self.maternal_consent.registered_subject)

    def test_meta_data_visit_reason_death(self):
        print """Test that for all visits if visit reason is """
        form = 'maternaldeath'
        visits = ['2000M','2010M','2020M','2030M','2060M','2090M','2120M','2150M','2180M']
        for visit in visits:
            print 'assert that maternaldeath status is \'New\' for visit {} where reason is death.'.format(visit)
            appointment = Appointment.objects.get(registered_subject=self.maternal_consent.registered_subject, visit_definition__code=visit)
            MaternalVisitFactory(appointment=appointment, reason='death')
            entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
            meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=self.registered_subject, entry=entry)
            self.assertEqual(meta_data.entry_status, 'NEW')

    def test_meta_data_avail_forms_2000M(self):
        print """Test that for all visits if visit reason is """
        forms = ['feedingchoice', 'feedingchoicesectionone', 'feedingchoicesectiontwo', 'feedingchoicesectionthree']
        visits = ['2000M','2010M','2020M','2030M','2060M','2090M','2120M','2150M','2180M']
        for visit in visits:
            appointment = Appointment.objects.get(registered_subject=self.maternal_consent.registered_subject, visit_definition__code=visit)
            MaternalVisitFactory(appointment=appointment)
            for form in forms:
                if visit == '2000M':
                    entry = Entry.objects.get(model_name=form, visit_definition_id=appointment.visit_definition_id)
                    meta_data = ScheduledEntryMetaData.objects.get(appointment=appointment, registered_subject=self.registered_subject, entry=entry)
                    print 'assert that {} status is {} for visit {} where consent is greater than two.'.format(form, meta_data.entry_status, visit)
                    self.assertEqual(meta_data.entry_status, 'NEW')
                else:
                    print 'assert that {} meta data for visit {} where consent is greater than two is not created.'.format(form, visit)
                    entry = Entry.objects.filter(model_name=form, visit_definition_id=appointment.visit_definition_id)
                    self.assertEqual(entry.count(), 0)
