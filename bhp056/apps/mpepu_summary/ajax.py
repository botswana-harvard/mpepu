from datetime import date, datetime
from django.db.models import Max
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from .classes import MedicationSummary

  
@dajaxice_register
def view_summary(request, subject_identifier):
    
    dajax = Dajax()

    medication_summary = MedicationSummary(subject_identifier=subject_identifier)
    
    rendered = render_to_string('medication_summary.html', medication_summary.context )
    
    dajax.assign('#left_table','innerHTML',rendered)
    
    return dajax.json()

