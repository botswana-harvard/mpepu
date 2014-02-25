from datetime import datetime, date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_GET

from ..query_objects.infant_randomization import NonRandomizedInfants


DEFAULT_DATE_FORMAT = "%Y-%m-%d"


def date_from_str(date_str, date_format=DEFAULT_DATE_FORMAT):
    return datetime.strptime(date_str, date_format).date()


@login_required
@require_GET
def eligible_infants(request, **kwargs):
    template = 'eligible_infants.html'
    search_dt = request.GET.get('search_date')
    context = {}
    search_date = date.today()
    if search_dt:
        search_date = date_from_str(search_dt)
    site = request.GET.get('site')
    if site:
        context['site'] = site
    infants = NonRandomizedInfants(site=site, search_date=search_date)
    eligibles = infants.eligibles
    context['infants'] = eligibles
    context['infants_count'] = infants.eligible_count
    context['search_date'] = search_date
    context['today'] = date.today().strftime('%Y-%m-%d')
    return render(request, template, context)
