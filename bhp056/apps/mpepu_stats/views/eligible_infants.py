from datetime import datetime, date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_GET

from ..query_objects.infant_randomization import NonRandomizedInfants


@login_required
@require_GET
def eligible_infants(request, **kwargs):
    template = 'eligible_infants.html'
    site = _site(request)
    search_date = _search_date(request)
    infants = NonRandomizedInfants(site=site, search_date=search_date).query()
    context = {'infants': infants,
               'search_date': search_date,
               'today': date.today().strftime('%Y-%m-%d'),
               'site': site
               }
    return render(request, template, context)


def _site(request):
    return request.GET.get('site')


def _search_date(request):
    search_date_param = request.GET.get('search_date')
    search_date = _date_from_text(search_date_param) if search_date_param else date.today()
    return search_date


def _date_from_text(date_str, date_format="%Y-%m-%d"):
    return datetime.strptime(date_str, date_format).date()
