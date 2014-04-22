from datetime import datetime, timedelta,date
from django.test import TestCase
from django.core.exceptions import ValidationError

from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.visit_schedule.classes import site_visit_schedules
from edc.core.bhp_variables.tests.factories import StudySiteFactory
from edc.core.bhp_content_type_map.models import ContentTypeMap
from edc.subject.consent.tests.factories import ConsentCatalogueFactory
from edc.subject.appointment.models import Appointment
from edc.lab.lab_profile.classes import site_lab_profiles

from apps.mpepu_lab.lab_profiles import MpepuInfantProfile
from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration
from edc.subject.registration.models import RegisteredSubject
from apps.mpepu_maternal.tests.factories import (MaternalConsentFactory, MaternalEligibilityPostFactory,
                                                 MaternalVisitFactory, MaternalLabDelFactory)
from apps.mpepu_infant.tests.factories import InfantBirthFactory, InfantVisitFactory, InfantEligibilityFactory

from ..forms import InfantEligibilityForm


class InfantEligibilityTests(TestCase):

    def setUp(self):
        try:
            site_lab_profiles.register(MpepuInfantProfile())
        except AlreadyRegistered:
            pass
        MpepuAppConfiguration()
        site_lab_tracker.autodiscover()
        site_visit_schedules.autodiscover()
        site_visit_schedules.build_all()
        study_site = StudySiteFactory()
        content_type_map = ContentTypeMap.objects.get(model='maternalconsent', app_label='mpepu_maternal')
        consent_catalogue = ConsentCatalogueFactory(content_type_map=content_type_map)
        consent_catalogue.add_for_app = 'mpepu_infant'
        consent_catalogue.save()

        print "register a mother "
        delivery_days_ago = 20
        delivery_datetime = datetime.today() - timedelta(days=delivery_days_ago - 3)
        maternal_consent = MaternalConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print "Consent: {}".format(maternal_consent)
        m_registered_subject = RegisteredSubject.objects.get(subject_identifier=maternal_consent.subject_identifier)
        maternal_eligibility = MaternalEligibilityPostFactory(maternal_consent=maternal_consent, registered_subject=m_registered_subject, registration_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        appointment = Appointment.objects.get(registered_subject=m_registered_subject, visit_definition__code='2000M')
        maternal_visit = MaternalVisitFactory(appointment=appointment, report_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print 'create a maternal_lab_del registering 2 of 2 infants'
        maternal_lab_del = MaternalLabDelFactory(maternal_visit=maternal_visit,
                                                         live_infants=2,
                                                         live_infants_to_register=2,
                                                         delivery_datetime=delivery_datetime,
                                                         has_ga='Yes',
                                                         ga=37,

                                                         )
        print 'maternal lab del: {}'.format(maternal_lab_del)
        print 'register infant 1 of 2'
        self.registered_subject1 = RegisteredSubject.objects.filter(relative_identifier=maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'first registered subject {}'.format(self.registered_subject1)
        self.infant_birth1 = InfantBirthFactory(registered_subject=self.registered_subject1, maternal_lab_del=maternal_lab_del, dob=delivery_datetime.date())
        print 'first infant birth {}'.format(self.infant_birth1)
        self.infant_eligibility1 = InfantEligibilityFactory(
                    infant_birth=self.infant_birth1,
                    registered_subject=self.infant_birth1.registered_subject,
                    clinical_jaundice = 'No',
                    anemia_neutropenia = 'No',
                    hiv_result_reference = 'PENDING',
                    maternal_feeding_choice = 'BF',
                    maternal_art_status = 'ON',
                    rando_bf_duration = 'Yes',
                    ctx_contra = 'No',
                    congen_anomaly = 'No',
                    randomization_site = 'Gaborone',
                    )
        print 'First infant Eligibility {}'.format(self.infant_eligibility1)

        print "register infant 2 of 2"
        self.registered_subject2 = RegisteredSubject.objects.filter(relative_identifier=maternal_consent.subject_identifier).order_by('subject_identifier')[1]
        print 'second registered subject {}'.format(self.registered_subject2)
        infant_birth2 = InfantBirthFactory(registered_subject=self.registered_subject2, maternal_lab_del=maternal_lab_del, dob=delivery_datetime.date())
        print 'second infant birth {}'.format(infant_birth2)
        self.registered_subject2.dob = infant_birth2.dob
        self.registered_subject2.gender = infant_birth2.gender
        self.registered_subject2.initials = infant_birth2.initials
        self.registered_subject2.relative_identifier = m_registered_subject.subject_identifier
        self.registered_subject2.save()

    def test_multiple_birth_validations(self):
        print "create Infant Elibility Form to test validations"
        form = InfantEligibilityForm()

        print "assert that maternal art status should be identical for multiple birth infants"
        form.cleaned_data = {'registered_subject': self.registered_subject2,
                             'rando_bf_duration': 'Yes',
                             'congen_anomaly': 'No',
                             'maternal_art_status': 'OFF',
                             'maternal_feeding_choice': 'BF',
                             'randomization_site': 'Gaborone',
                             'ctx_contra': 'No',
                             'weight': 3.7,
                             'clinical_jaundice': 'No',
                             'anemia_neutropenia': 'No',
                             }
        self.assertRaisesMessage(ValidationError,
            "The maternal ART status is not identical for multiple birth infants. On '{0}' you indicated '{1}'. Please correct."
            .format(self.registered_subject1.subject_identifier, self.infant_eligibility1.maternal_art_status),
             form.clean)

        print "assert that maternal feeeding choice should be identical for multiple birth infants"
        form.cleaned_data = {'registered_subject': self.registered_subject2,
                             'rando_bf_duration': 'N/A',
                             'congen_anomaly': 'No',
                             'maternal_art_status': 'ON',
                             'maternal_feeding_choice': 'FF',
                             'randomization_site': 'Gaborone',
                             'ctx_contra': 'No',
                             'weight': 3.7,
                             'clinical_jaundice': 'No',
                             'anemia_neutropenia': 'No',
                             }
        self.assertRaisesMessage(ValidationError,
            "The maternal feeding choice is not identical for multiple birth infants. On '{0}' you indicated '{1}'. Please correct."
            .format(self.registered_subject1.subject_identifier,self.infant_eligibility1.maternal_feeding_choice),
            form.clean)

        print "assert that the breastfeeding rando choice is identical for multiple birth infants"
        form.cleaned_data = {'registered_subject': self.registered_subject2,
                             'rando_bf_duration': 'No',
                             'congen_anomaly': 'No',
                             'maternal_art_status': 'ON',
                             'maternal_feeding_choice': 'BF',
                             'randomization_site': 'Gaborone',
                             'ctx_contra': 'No',
                             'weight': 3.7,
                             'clinical_jaundice': 'No',
                             'anemia_neutropenia': 'No',
                             }
        self.assertRaisesMessage(ValidationError,
            "The breast feeding randomization choice is not identical for mutliple birth infants. On '{0}' you indicated '{1}'. Please correct."
            .format(self.registered_subject1.subject_identifier, self.infant_eligibility1.rando_bf_duration),
            form.clean)

        print "assert that the rando site is identical for multiple birth infants"
        form.cleaned_data = {'registered_subject': self.registered_subject2,
                             'rando_bf_duration': 'Yes',
                             'congen_anomaly': 'No',
                             'maternal_art_status': 'ON',
                             'maternal_feeding_choice': 'BF',
                             'randomization_site': 'Molepolole',
                             'ctx_contra': 'No',
                             'weight': 3.7,
                             'clinical_jaundice': 'No',
                             'anemia_neutropenia': 'No',
                             }
        self.assertRaisesMessage(ValidationError,
            "The rando site is not identical for multiple birth infants. On '{0}' you indicated '{1}'.Please correct."
            .format(self.registered_subject1.subject_identifier, self.infant_eligibility1.randomization_site),
            form.clean)
