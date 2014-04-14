from datetime import datetime, timedelta, date
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
from apps.mpepu_infant.tests.factories import (InfantBirthFactory, InfantVisitFactory, InfantEligibilityFactory,
                                               InfantFuFactory, InfantFuPhysicalFactory, InfantFuDxFactory)

from ..forms import InfantFuPhysicalForm, InfantFuDxItemsForm, InfantFuDForm


class InfantFuTests(TestCase):
    def setUp(self):
        try:
            site_lab_profiles.register(MpepuInfantProfile())
        except AlreadyRegistered:
            pass
        MpepuAppConfiguration()
        site_lab_tracker.autodiscover()
        site_visit_schedules.autodiscover()
        site_visit_schedules.build_all()
        study_site = StudySiteFactory(site_code=2)
        content_type_map = ContentTypeMap.objects.get(model='maternalconsent', app_label='mpepu_maternal')
        consent_catalogue = ConsentCatalogueFactory(content_type_map=content_type_map)
        consent_catalogue.add_for_app = 'mpepu_infant'
        consent_catalogue.save()

        delivery_days_ago = 20
        delivery_datetime = datetime.today() - timedelta(days=delivery_days_ago - 3)
        print "Consent a mother"
        self.maternal_consent = MaternalConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print "Consent: {}".format(self.maternal_consent)
        self.registered_subject = RegisteredSubject.objects.get(subject_identifier=self.maternal_consent.subject_identifier)
        print 'check if mother is eligible'
        self.maternal_eligibility = MaternalEligibilityPostFactory(maternal_consent=self.maternal_consent, registered_subject=self.registered_subject, registration_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print 'get the 2000M visit'
        self.m_appointment = Appointment.objects.get(registered_subject=self.registered_subject, visit_definition__code='2000M')
        print 'create a maternal visit for the 2000M visit'
        self.maternal_visit = MaternalVisitFactory(appointment=self.m_appointment, report_datetime=datetime.today() - timedelta(days=delivery_days_ago))
        print 'create a maternal_lab_del registering 2 of 2 infants'
        self.maternal_lab_del = MaternalLabDelFactory(maternal_visit=self.maternal_visit,
                                                         live_infants=1,
                                                         live_infants_to_register=1,
                                                         delivery_datetime=delivery_datetime,
                                                         has_ga='Yes',
                                                         ga=37,
                                                         )
        print 'maternal lab del: {}'.format(self.maternal_lab_del)
        print 'get registered subject of the infant'
        self.registered_subject = RegisteredSubject.objects.filter(relative_identifier=self.maternal_consent.subject_identifier).order_by('subject_identifier')[0]
        print 'infant registered subject {}'.format(self.registered_subject)
        self.infant_birth = InfantBirthFactory(registered_subject=self.registered_subject, maternal_lab_del=self.maternal_lab_del, dob=delivery_datetime.date())
        print 'infant birth {}'.format(self.infant_birth)
        self.appointment = Appointment.objects.get(registered_subject=self.registered_subject, visit_definition__code='2000')
        self.infant_visit = InfantVisitFactory(appointment=self.appointment, report_datetime=datetime.today(), reason='scheduled')
        self.infant_eligibility = InfantEligibilityFactory(infant_birth=self.infant_birth, registered_subject=self.registered_subject)
        print 'infant eligibility {}'.format(self.infant_eligibility)
        app_2010 = Appointment.objects.get(registered_subject=self.registered_subject, visit_definition__code='2010')
        visit_2010 = InfantVisitFactory(appointment=app_2010, report_datetime=datetime.today(), reason='scheduled')
        self.fu = InfantFuFactory(infant_visit=visit_2010)
        self.fu_physical = InfantFuPhysicalFactory(infant_fu=self.fu, infant_visit=visit_2010)
        self.fu_dx = InfantFuDxFactory(infant_fu=self.fu, infant_visit=visit_2010)

    def test_infant_fu_dx_items_validations(self):
        form = InfantFuDxItemsForm()

        print "assert that if onset date is greater than the visit date" 
        form.cleaned_data = {'infant_fu_dx': self.fu_dx,
                             'fu_dx':'Rash',
                            'fu_dx_specify': 'Severe rash all over body',
                            'grade': 3,
                            'health_facility': 'Yes',
                            'was_hospitalized': 'Yes',
                            'onset_date': date.today()+timedelta(5),
                            'is_eae_required': 'No',
                          }
        self.assertRaisesMessage(ValidationError,
            "Onset date cannot be greater than the visit date. Please correct",
            form.clean
            )

        print "assert that if was_hospitalised='Yes' in InfantFuPhysical then was_hospital should be 'Yes'" 
        form.cleaned_data = {'infant_fu_dx': self.fu_dx,
                             'fu_dx':'Rash',
                            'fu_dx_specify': 'Severe rash all over body',
                            'grade': 3,
                            'health_facility': 'Yes',
                            'was_hospitalized': 'No',
                            'onset_date': date.today()-timedelta(5),
                            'is_eae_required': 'No',
                          }
        self.assertRaisesMessage(ValidationError,
            "Your response about hospitalization in InfantFuPhysical, and whether or not patient was hospitalized in this DX form are not the same. Please correct.",
            form.clean
            )

        print "assert that if diagnosis is not 'Rash' nor 'Hepatitis:Drug related' and is a grade 2 then it should not be reportable" 
        form.cleaned_data = {'infant_fu_dx': self.fu_dx,
                             'fu_dx': 'Otitis media',
                            'fu_dx_specify': 'ear discharge',
                            'grade': 2,
                            'health_facility': 'Yes',
                            'was_hospitalized': 'No',
                            'onset_date': date.today() - timedelta(5),
                            'is_eae_required': 'No',
                          }
        self.assertRaisesMessage(ValidationError,
            "{dx} is not reportable at grade 2."
            .format(dx=form.cleaned_data.get('fu_dx')),
            form.clean
            )

        try:
            print "assert that if diagnosis is 'Rash' or 'Hepatitis:Drug related' and is a grade 2 then it should be reportable" 
            form.cleaned_data = {'infant_fu_dx': self.fu_dx,
                                 'fu_dx': 'Rash',
                                'fu_dx_specify': 'Rash on body',
                                'grade': 2,
                                'health_facility': 'Yes',
                                'was_hospitalized': 'Yes',
                                'onset_date': date.today() - timedelta(5),
                                'is_eae_required': 'No',
                              }
        except:
            print "Failed. Raised validation error that grade 2 rash is not reportable."

