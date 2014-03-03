from datetime import datetime, timedelta
from django.shortcuts import render_to_response
from django.db.models import Count, Avg, Max, Min, StdDev, Variance
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from apps.mpepu_infant.models import InfantBirth
from apps.mpepu_stats.query_objects.infant_data_decorator import InfantDataDecorator


@login_required
def potential_randos_report(request, **kwargs):

    section_name = kwargs.get('section_name')
    report_title = 'Potential vs Missed Randomizations'
    template = 'potential_randos_report.html'

    # get all births / infants
    infantbirth_aggregates = InfantBirth.objects.all().aggregate(Count('dob'), Avg('dob'), Max('dob'), Min('dob'), StdDev('dob'), Variance('dob'))
    cutoff_dob = datetime.today() - timedelta(34)

    mrandos = InfantBirth.objects.filter(dob__lt=cutoff_dob, registered_subject__sid__isnull=True).order_by('dob')
    missed_randos = [InfantDataDecorator(ib) for ib in mrandos]

    prandos = InfantBirth.objects.filter(dob__gte=cutoff_dob, registered_subject__sid__isnull=True).order_by('dob')
    potential_randos = [InfantDataDecorator(ib) for ib in prandos]

    return render_to_response(template, {
        'infantbirth_aggregates': infantbirth_aggregates,
        'missed_randos': missed_randos,
        'potential_randos': potential_randos,
        'cutoff_dob': cutoff_dob,
        'section_name': section_name,
        'report_title': report_title,
        'report': '',
        'report_name': kwargs.get('report_name'),
        }, context_instance=RequestContext(request))
