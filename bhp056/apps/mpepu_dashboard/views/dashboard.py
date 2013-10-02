from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from edc.subject.registration.models import RegisteredSubject
from mpepu_dashboard.classes import InfantDashboard, MaternalDashboard
from mpepu_infant.models import InfantVisit, InfantBirth
from mpepu_infant_rando.models import  InfantRando
from mpepu_maternal.models import MaternalConsent, MaternalVisit

@login_required
def dashboard(request, **kwargs):

    if kwargs.get('dashboard_type') == 'infant':

        if kwargs.get('subject_identifier'):
            subject_identifier = kwargs.get('subject_identifier')
            registered_subject = RegisteredSubject.objects.get(subject_identifier=subject_identifier)
            maternal_subject_identifier = registered_subject.relative_identifier
            maternal_consent = MaternalConsent.objects.get(subject_identifier=maternal_subject_identifier)
        elif kwargs.get('pk'):
            subject_identifier = RegisteredSubject.objects.get(pk=kwargs.get('pk')).subject_identifier
            registered_subject = RegisteredSubject.objects.get(subject_identifier=subject_identifier)
            maternal_subject_identifier = RegisteredSubject.objects.get(pk=kwargs.get('pk')).relative_identifier
            maternal_consent = MaternalConsent.objects.get(subject_identifier=maternal_subject_identifier)
        elif kwargs.get('registered_subject'):
            registered_subject = RegisteredSubject.objects.get(pk=kwargs.get('registered_subject'))
            subject_identifier = registered_subject.subject_identifier
            maternal_subject_identifier = registered_subject.relative_identifier
            maternal_consent = MaternalConsent.objects.get(subject_identifier=maternal_subject_identifier)
        else:
            registered_subject = RegisteredSubject.objects.none()
            maternal_consent = MaternalConsent.objects.none()
            subject_identifier = None

        # create dashboard object
        dashboard = InfantDashboard(**kwargs)

        # create a basic dashboard context
        dashboard.create(
            registered_subject=registered_subject,
            visit_code=kwargs.get('visit_code'),
            visit_instance=kwargs.get("visit_instance"),
        )

    elif kwargs.get('dashboard_type') == 'maternal':

        if kwargs.get('subject_identifier'):
            subject_identifier = kwargs.get('subject_identifier')
            maternal_consent = MaternalConsent.objects.get(subject_identifier=kwargs.get('subject_identifier'))
        elif kwargs.get('pk'):
            maternal_consent = MaternalConsent.objects.get(pk=unicode(kwargs.get('pk')))
            subject_identifier = maternal_consent.subject_identifier
        elif kwargs.get('registered_subject'):
            registered_subject = RegisteredSubject.objects.get(pk=kwargs.get('registered_subject'))
            subject_identifier = registered_subject.subject_identifier
            maternal_consent = MaternalConsent.objects.get(subject_identifier=subject_identifier)
        else:
            maternal_consent = MaternalConsent.objects.none()
            subject_identifier = ''

        if RegisteredSubject.objects.filter(subject_identifier=maternal_consent.subject_identifier):
            registered_subject = RegisteredSubject.objects.get(subject_identifier=subject_identifier)

        # create dashboard object
        dashboard = MaternalDashboard(**kwargs)

        # create a basic dashboard context
        dashboard.create(
            registered_subject=registered_subject,
            visit_code=kwargs.get('visit_code'),
            visit_instance=kwargs.get("visit_instance"),
        )

    else:
        raise ValueError('Unknown dashboard_type, must be \'infant\' or \'maternal\'. Got %s' % kwargs.get('dashboard_type'))

    return render_to_response(
        dashboard.template,
        dashboard.get_context(),
        context_instance=RequestContext(request))
