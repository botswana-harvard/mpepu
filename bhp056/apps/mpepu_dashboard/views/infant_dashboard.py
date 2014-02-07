from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from ..classes import InfantDashboard


@login_required
def infant_dashboard(request, **kwargs):
    dashboard = InfantDashboard(
        dashboard_type=kwargs.get('dashboard_type'),
        dashboard_id=kwargs.get('dashboard_id'),
        dashboard_model=kwargs.get('dashboard_model'),
        dashboard_category=kwargs.get('dashboard_category'),
        registered_subject=kwargs.get('registered_subject'),
        dashboard_type_list=['infant'],
        show=kwargs.get('show'),
        )
    dashboard.set_context()
    return render_to_response(
        'infant_dashboard.html',
        dashboard.context.get(),
        context_instance=RequestContext(request))
