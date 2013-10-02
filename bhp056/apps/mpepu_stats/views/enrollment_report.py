from itertools import groupby
from django.db import connection
from django.db.models import Q
from datetime import datetime, date, time, timedelta
from django.shortcuts import render_to_response
from django.db.models import Count, Avg, Max, Min, StdDev, Variance
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from bhp_common.utils import os_variables
from edc.subject.registration.models import RegisteredSubject
from bhp_variables.models import StudySite
from mpepu_infant.models import InfantBirth
from django.db import models
from mpepu_maternal.models import MaternalConsent, MaternalEnroll
from mpepu_stats.forms import DateRangeForm

@login_required
def enrollment_report(request, **kwargs):
    section_name = kwargs.get('section_name')
    report_title  = 'Enrollment Stats'
    template = 'enrollment_report.html' 
    months = []
    years = []
    sites = []
    model_reports = {}
    model_reports_ordered_keys = []
             
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            # get all models with a registered_subject fk
            model_list = [{'name': model._meta.module_name, 'model':model} 
                        for model in models.get_models() 
                        if (model._meta.app_label=='mpepu_maternal' 
                        or model._meta.app_label=='mpepu_infant') 
                        and 'registered_subject' in 
                        [field.name for field in model._meta.fields] 
                        and '_audit_id' not in 
                        [field.name for field in model._meta.fields]
                       ]
            for dct in model_list:
                model_reports[dct['name']] = {
                        'name': dct['model']._meta.module_name,        
                        'verbose_name': dct['model']._meta.verbose_name, 
                        'model': dct['model'], 
                        'data': None, 
                        'month_totals': [], 
                        'year_totals': [],
                        'total':0,                 
                        'date_grouping_field':'created', 
                        }
            # get date_grouping_field if other than created
            for key,model_report in model_reports.items():
                model_reports_ordered_keys.append(key)
                # get an instance of the model
                m = model_report['model']()
                # get date_grouping_field if method is defined
                try: 
                    model_reports[model_report['name']]['date_grouping_field'] = m.get_date_grouping_field()
                except:
                    pass
            model_reports_ordered_keys.sort()

            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']       

            # prepare ordered lists of years, months and sites
            years = range(start_date.year,end_date.year)                    
            if not years:
                years = [start_date.year,]
            months = range(start_date.month,end_date.month+1)
            sites = [study_site.site_name for study_site in StudySite.objects.all()]
            sites = list(set(sites))
            sites.sort()            
                    
            # get data for each model  
            for key,model_report in model_reports.items():
                if key == 'infantbirth': 
                    model_report['date_grouping_field'] = 'dob'
                data = model_report['model'].objects.filter(
                    Q((model_report['date_grouping_field']+'__gte', start_date)),
                    Q((model_report['date_grouping_field']+'__lte', 
                        end_date))).extra(
                                          select={
                                                  'year': 'extract(year from '+model_report['model']._meta.app_label+'_'+
                                                  model_report['model']._meta.module_name+'.'+
                                                  model_report['date_grouping_field']+')', 
                                                  'month': 'extract(month from '+model_report['model']._meta.app_label+'_'+
                                                  model_report['model']._meta.module_name+'.'+
                                                  model_report['date_grouping_field']+')'
                                                  }
                                        ).values('year', 'month', 
                                                 'registered_subject__gender', 
                                                 'registered_subject__study_site__site_name'
                                        ).annotate(frequency=Count(model_report['date_grouping_field'])
                                    )

                model_reports[model_report['name']]['data'] = data
                total = 0
                for year in years:
                    year_total = 0
                    for month in months:
                        month_total = 0
                        for x in [rpt['frequency'] for rpt in model_reports[model_report['name']]['data'] if rpt['year']==year and rpt['month']==month]:
                            month_total += x
                        model_reports[model_report['name']]['month_totals'].append({'year':year, 'month':month, 'total':month_total})
                        year_total += month_total
                    model_reports[model_report['name']]['year_totals'].append({'year':year, 'total':year_total})
                    total += year_total  
                model_reports[model_report['name']]['total'] = total

    else:
        form = DateRangeForm(request.POST)            
    

    return render_to_response(template, { 
        'form': form,
        'years': years,
        'months': months,
        'sites': sites,                
        'cumulative_frequency':0,
        'model_reports': model_reports,
        'model_reports_ordered_keys':model_reports_ordered_keys,
        'section_name': section_name, 
        'report_title': report_title,                          
        'report': ''  ,
        'report_name': kwargs.get('report_name'),         
        }, context_instance=RequestContext(request))



# 294-0 rando'ed at 2 days
# 201-5-10 rando at time to be off-study (hiv+)
