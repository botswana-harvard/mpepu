from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from edc.subject.registration.models import RegisteredSubject
from mpepu_dashboard.classes import InfantDashboard
from mpepu_infant.models import Visit, InfantBirth
from mpepu_infant_rando.models import InfantRando
from ..models import MaternalConsent

@login_required
def infant_dashboard(request, **kwargs):

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
    dashboard = InfantDashboard()

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

