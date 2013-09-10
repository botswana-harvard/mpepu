from datetime import date, datetime, timedelta
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django import forms


class DateRangeGradeSearchForm(forms.Form):
    
    date_start = forms.DateField(
        #max_length=10,
        label="Start Date",
        help_text="Format is YYYY-MM-DD",
        error_messages={'required': 'Please enter a valid date.'},
        initial=date.today()
        )
    date_end = forms.DateField(
        #max_length=10,
        label="End Date",
        help_text="Format is YYYY-MM-DD",
        error_messages={'required': 'Please enter a valid date.'},
        initial=date.today()
        )
    grade = forms.ChoiceField(        
        label="Grade",
        choices = (('0', ' -- '), ('3','3'),('4','4'), ),        
        #error_messages={'required': 'Please enter valid grade (3/4).'},
        required = False,
        )        
    hospitalized = forms.ChoiceField(        
        label="Hospitalized",
        choices = (('any', ' -- '), ('yes','Yes'),('no','No'), ),
        required = False,
        initial = 'any',
        )        

    def help_text(self):
        return "Enter the grade, the start date and the end date for the period to be listed. Format is YYYY-MM-DD."

