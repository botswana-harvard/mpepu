from datetime import date, timedelta, datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from edc.subject.registration.models import RegisteredSubject
from mpepu_dashboard.classes import MaternalDashboard
from mpepu_maternal.models import MaternalConsent, MaternalVisit
from mpepu_infant.models import InfantBirth


@login_required
def maternal_dashboard(request, **kwargs):

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
        registered_subject = RegisteredSubject.objects.get(
            subject_identifier=subject_identifier)

    # create dashboard object
    dashboard = MaternalDashboard(**kwargs)

    # create a basic dashboard context
    dashboard.create(
        registered_subject=registered_subject,
        visit_code=kwargs.get('visit_code'),
        visit_instance=kwargs.get("visit_instance"),
    )

    return render_to_response(
        dashboard.template,
        dashboard.get_context(),
        context_instance=RequestContext(request))

