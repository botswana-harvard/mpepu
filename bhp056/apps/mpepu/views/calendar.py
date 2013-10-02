from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.safestring import mark_safe
from bhp_calendar.classes import DataCalendar
from mpepu.classes import MyCalendar


def calendar(request, **kwargs):
  
    """prepare a month calendar for display based on queryset_label, month amd year criteria """
  
    #if kwargs.get('year'):
    #    year = int(kwargs.get('year'))  
    #else:
    #    year=''         
    #if kwargs.get('month') :
    #    month = int(kwargs.get('month'))
    #else:
    #    month=''    
    #if kwargs.get('netbook') :
    #    netbook = kwargs.get('netbook')
    #else:
    #    netbook=''  
        
    search_name = kwargs.get('search_name')

    queryset_label = '%s_month' % (search_name)
        
    section_name = kwargs.get('section_name')  

    # call MyCalendar which will either initiate an empty form or
    # handle a posted form passing the posted values to the labelled queryset    
    cal = MyCalendar(**kwargs)
    
    cal.get_response(request, queryset_label=queryset_label, **kwargs)
    
    if cal['search_results']:
        html_calendar = DataCalendar(appointment_label='Scheduled visits', appointments=cal['search_results']).formatmonth(cal['year'], cal['month'])
        cal['calendar'] = mark_safe(html_calendar)
    else:        
        cal['calendar'] = ''

    return render_to_response('calendar.html',
        cal.context(), 
        context_instance=RequestContext(request))

