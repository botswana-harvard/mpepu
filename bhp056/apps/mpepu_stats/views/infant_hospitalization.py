from datetime import datetime, date, time, timedelta
from django.shortcuts import render_to_response
from django.db.models import Count, Avg, Max, Min, StdDev, Variance, F, Q
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from edc.dashboard.search.forms.date_range_search_form import DateRangeSearchForm
from apps.mpepu_infant.models import InfantDeath, InfantFuPhysical
from ..query_objects.infant_data_decorator import InfantDataDecorator


@login_required
def infant_hospitalization(request, **kwargs):

    section_name = kwargs.get('section_name')
    report_title = 'Infant Hospitalizations'
    template = 'infant_hospitalization.html'
    total_infant_death = None
    total_hospitalized = None
    total_follow_up = 0
    total_death = None
    period_total_hospitalized = 0
    infant_hospitalized_randomized = None
    infant_hospitalized_not_randomized = None
    infant_death_hospitalized_randomized = None
    infant_death_hospitalized_not_randomized = None

    if request.method == 'POST':

        form = DateRangeSearchForm(request.POST)
        if form.is_valid():

            start_date = form.cleaned_data['date_start']
            end_date = form.cleaned_data['date_end']
            total_infant_death = InfantDeath.objects.all().count()
            # get total hospitalized by adding those reported
            # at follow up with those reported at death
            total_hospitalized = InfantFuPhysical.objects.filter(was_hospitalized__iexact='yes').count() + InfantDeath.objects.filter(participant_hospitalized__iexact = 'Yes').count()

            # reported at followup before rando
            not_randomized = InfantFuPhysical.objects.filter(
                                        was_hospitalized__iexact = 'Yes',
                                        infant_visit__report_datetime__gt=start_date,
                                        infant_visit__report_datetime__lte=end_date,
                                        infant_visit__appointment__visit_definition__code='2010'
                                        ).order_by('infant_visit__report_datetime')
            infant_hospitalized_not_randomized = (InfantDataDecorator(hospitalized.infant_visit.appointment, report_datetime=hospitalized.infant_visit.report_datetime) for hospitalized in not_randomized)

            # reported at followup after rando
            randomized = InfantFuPhysical.objects.filter(
                                        was_hospitalized__iexact = 'Yes',
                                        infant_visit__report_datetime__gt=start_date,
                                        infant_visit__report_datetime__lte=end_date,
                                        ).exclude(infant_visit__appointment__visit_definition__code='2010'
                                        ).order_by('infant_visit__report_datetime')
            infant_hospitalized_randomized = (InfantDataDecorator(hospitalized.infant_visit.appointment, report_datetime=hospitalized.infant_visit.report_datetime) for hospitalized in randomized )
            total_follow_up = not_randomized.count() + randomized.count()

            period_total_hospitalized = total_follow_up


            period_total_infant_death_hospitalized = InfantDeath.objects.filter(
                                        participant_hospitalized__iexact = 'Yes',
                                        death_date__gt=start_date,
                                        death_date__lte=end_date,).count()

            # reported at death before rando
            death_not_randomized = InfantDeath.objects.filter(
                participant_hospitalized__iexact='Yes',
                death_date__gt=start_date,
                death_date__lte=end_date,
                registered_subject__sid__isnull=True,
            )
            infant_death_hospitalized_not_randomized = (InfantDataDecorator(id) for id in death_not_randomized)

            # reported at death after rando
            death_randomized = InfantDeath.objects.filter(
                participant_hospitalized__iexact='Yes',
                death_date__gt=start_date,
                death_date__lte=end_date,
                registered_subject__sid__isnull=False,
            )
            infant_death_hospitalized_randomized = (InfantDataDecorator(id) for id in death_randomized)

            total_death = death_not_randomized.count() + death_randomized.count()
            period_total_hospitalized += total_death





    else:

        form = DateRangeSearchForm()
        form.date_start = date.today()
        form.date_end = date.today()

    return render_to_response(template, {
        'form': form,
        'total_infant_death': total_infant_death,
        'total_hospitalized': total_hospitalized,
        'total_follow_up': total_follow_up,
        'total_death': total_death,
        'period_total_hospitalized': period_total_hospitalized,
        'infant_hospitalized_randomized' : infant_hospitalized_randomized,
        'infant_hospitalized_not_randomized' : infant_hospitalized_not_randomized,
        'infant_death_hospitalized_randomized' : infant_death_hospitalized_randomized,
        'infant_death_hospitalized_not_randomized' : infant_death_hospitalized_not_randomized,
        'section_name': section_name,
        'report_title': report_title,
        'report': ''  ,
        'report_name': kwargs.get('report_name'),
        }, context_instance=RequestContext(request))


