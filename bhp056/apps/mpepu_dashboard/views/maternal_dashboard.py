from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.mpepu_maternal.models import MaternalConsent

from ..classes import MaternalDashboard


@login_required
def maternal_dashboard(request, **kwargs):
    dashboard = MaternalDashboard(
        dashboard_type=kwargs.get('dashboard_type'),
        dashboard_id=kwargs.get('dashboard_id'),
        dashboard_model=kwargs.get('dashboard_model'),
        dashboard_category=kwargs.get('dashboard_category'),
        registered_subject=kwargs.get('registered_subject'),
        show=kwargs.get('show'),
        dashboard_type_list=['maternal'],
        dashboard_models={'maternal_consent': MaternalConsent},
        )
    return render_to_response(
        'maternal_dashboard.html',
        dashboard.get_context().get(),
        context_instance=RequestContext(request))
