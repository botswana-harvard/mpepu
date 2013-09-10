from datetime import datetime, date, time, timedelta
from django.shortcuts import render_to_response
from django.db.models import Count, Avg, Max, Min, StdDev, Variance, F, Q
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from bhp_search.forms import DateRangeSearchForm, WeekNumberSearchForm
from bhp_common.utils import os_variables
from mpepu_infant.models import InfantFuDxItems
from mpepu_stats.forms import DateRangeGradeSearchForm


@login_required
def infant_diagnoses(request, **kwargs):

    section_name = kwargs.get('section_name')
    report_title  = 'Infant Diagnoses'
    template = 'infant_diagnoses.html'
    infant_dx_randomized = None
    infant_dx_not_randomized = None
    infant_dx_randomized_group = None
    infant_dx_not_randomized_group = None    
    total_dx = None
    period_total_dx = 0    


    if request.method == 'POST':

        form = DateRangeGradeSearchForm(request.POST)
        if form.is_valid():

            total_dx = InfantFuDxItems.objects.all().count()

            start_date = form.cleaned_data['date_start']
            end_date = form.cleaned_data['date_end']
            grade = form.cleaned_data['grade']            
            hospitalized = form.cleaned_data['hospitalized']            
            
            # reported at dx before rando
            qset = Q()
            if grade == '3' or grade == '4':
                qset.add(Q(grade__exact = grade),Q.AND)                
            if hospitalized == 'yes' or hospitalized == 'no':
                qset.add(Q(was_hospitalized__exact = hospitalized),Q.AND)                
            qset.add(Q(was_hospitalized__iexact = 'Yes'),Q.AND)
            qset.add(Q(infant_fu_dx__infant_visit__report_datetime__gt=start_date),Q.AND)
            qset.add(Q(infant_fu_dx__infant_visit__report_datetime__lte=end_date),Q.AND) 
            qset.add(Q(infant_fu_dx__infant_visit__appointment__visit_definition__code='2010'),Q.AND)

            infant_dx_not_randomized = InfantFuDxItems.objects.filter(qset).order_by('infant_fu_dx__infant_visit__appointment__registered_subject__subject_identifier','infant_fu_dx__infant_visit__report_datetime')
            infant_dx_not_randomized_group = InfantFuDxItems.objects.filter(qset).values('fu_dx').annotate(Count('fu_dx'))
            
            # reported at dx after rando
            qset = Q()
            if grade == '3' or grade == '4':
                qset.add(Q(grade__exact = grade),Q.AND)                
            if hospitalized == 'yes' or hospitalized == 'no':
                qset.add(Q(was_hospitalized__exact = hospitalized),Q.AND)                

            qset.add(Q(infant_fu_dx__infant_visit__report_datetime__gt=start_date),Q.AND)
            qset.add(Q(infant_fu_dx__infant_visit__report_datetime__lte=end_date),Q.AND) 
            
            infant_dx_randomized = InfantFuDxItems.objects.filter(qset).exclude(infant_fu_dx__infant_visit__appointment__visit_definition__code='2010'
                                        ).order_by('infant_fu_dx__infant_visit__appointment__registered_subject__subject_identifier','infant_fu_dx__infant_visit__report_datetime')
            
            infant_dx_randomized_group = InfantFuDxItems.objects.filter(qset).exclude(infant_fu_dx__infant_visit__appointment__visit_definition__code='2010'
                                        ).values('fu_dx').annotate(Count('fu_dx'))

            
            
            period_total_dx = infant_dx_not_randomized.count() + infant_dx_randomized.count()
            
            
            
                                        
    else:

        form = DateRangeGradeSearchForm()
        form.date_start = date.today()
        form.date_end = date.today()        
        
    return render_to_response(template, { 
        'form': form,
        'total_dx': total_dx,
        'period_total_dx': period_total_dx,        
        'infant_dx_randomized' : infant_dx_randomized,
        'infant_dx_not_randomized' : infant_dx_not_randomized,   
        'infant_dx_randomized_group':infant_dx_randomized_group,
        'infant_dx_not_randomized_group':infant_dx_not_randomized_group,                  
        'section_name': section_name, 
        'report_title': report_title,                          
        'report': ''  ,
        'report_name': kwargs.get('report_name'),         
        }, context_instance=RequestContext(request))


