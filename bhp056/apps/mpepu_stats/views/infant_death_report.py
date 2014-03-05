from datetime import datetime, date, time, timedelta
from django.shortcuts import render_to_response
from django.db.models import Count, Avg, Max, Min, StdDev, Variance
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from edc.dashboard.search.forms.date_range_search_form import DateRangeSearchForm
from apps.mpepu_infant.models import InfantDeath
from apps.mpepu_stats.query_objects.infant_data_decorator import InfantDataDecorator


@login_required
def infant_death_report(request, **kwargs):

    section_name = kwargs.get('section_name')
    report_title  = 'Infant Deaths'
    template = 'infant_death_report.html'
    total_infant_death = None
    infant_death_randomized = None
    infant_death_not_randomized = None
    infant_death_dob_aggregates = None

    if request.method == 'POST':
        form = DateRangeSearchForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['date_start']
            end_date = form.cleaned_data['date_end']
            total_infant_death = InfantDeath.objects.all().count()
            infant_death_dob_aggregates = InfantDeath.objects.filter(
                                            death_date__gt=start_date,
                                            death_date__lte=end_date
                                            ).aggregate(Count('registered_subject__dob'), Avg('registered_subject__dob'), Max('registered_subject__dob'), Min('registered_subject__dob'), StdDev('registered_subject__dob'), Variance('registered_subject__dob'))

            randomized = InfantDeath.objects.filter(
                                            death_date__gt=start_date,
                                            death_date__lte=end_date,
                                            registered_subject__sid__isnull=False
                                            ).order_by('registered_subject__dob')
            infant_death_randomized = (InfantDataDecorator(id) for id in randomized)

            not_randomized = InfantDeath.objects.filter(
                                            death_date__gt=start_date,
                                            death_date__lte=end_date,
                                            registered_subject__sid__isnull=True
                                            ).order_by('registered_subject__dob')
            infant_death_not_randomized = (InfantDataDecorator(id) for id in not_randomized)
    else:
        form = DateRangeSearchForm()
        form.date_start = date.today()
        form.date_end = date.today()

    return render_to_response(template, {
        'form': form,
        'total_infant_death': total_infant_death,
        'infant_death_randomized' : infant_death_randomized,
        'infant_death_not_randomized' : infant_death_not_randomized,
        'infant_death_dob_aggregates' : infant_death_dob_aggregates,
        'section_name': section_name,
        'report_title': report_title,
        'report': ''  ,
        'report_name': kwargs.get('report_name'),
        }, context_instance=RequestContext(request))


