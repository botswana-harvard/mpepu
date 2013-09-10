from bhp_calendar.classes import BaseCalendar
from bhp_calendar.forms import CalendarForm
from mpepu.classes import get_my_calendar_queryset

class MyCalendar (BaseCalendar):

    def __init__(self, **kwargs):
        BaseCalendar.__init__(self,  **kwargs)

        
    def get_labeled_queryset(self, queryset_label, **kwargs):
        get_my_calendar_queryset(self, queryset_label, **kwargs) 

    def form(self, post=None):
        return CalendarForm(post)  
