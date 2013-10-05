import sys,os
sys.path.append('/home/erikvw/source/')
sys.path.append('/home/erikvw/source/bhp056/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bhp056.settings'
from django.core.management import setup_environ
from bhp056 import settings

setup_environ(settings)

from edc.subject.registration.models import RegisteredSubject
from edc.subject.appointment.models import Appointment
from ..models import MaternalPostReg, MaternalEligibilityPost, MaternalEligibilityAnte

"""maternal registration forms """

for rs in RegisteredSubject.objects.filter(subject_type='maternal').order_by('subject_identifier'):
    if MaternalPostReg.objects.filter(registered_subject=rs):
        membership_form = MaternalPostReg.objects.get(registered_subject=rs)
        Appointment.objects.create_appointments( 
            registered_subject = rs, 
            model_name = membership_form.__class__.__name__.lower(),
            )
        print rs.subject_identifier            


for rs in RegisteredSubject.objects.filter(subject_type='maternal'):
    if MaternalEligibilityPost.objects.filter(registered_subject=rs):
        membership_form = MaternalEligibilityPost.objects.get(registered_subject=rs)
        Appointment.objects.create_appointments( 
            registered_subject = rs, 
            base_appt_datetime = membership_form.created, 
            model_name = membership_form.__class__.__name__.lower(),
            )
        print rs.subject_identifier            


for rs in RegisteredSubject.objects.filter(subject_type='maternal'):
    if MaternalEligibilityAnte.objects.filter(registered_subject=rs):
        membership_form = MaternalEligibilityAnte.objects.get(registered_subject=rs)
        Appointment.objects.create_appointments( 
            registered_subject = rs, 
            base_appt_datetime = membership_form.created, 
            model_name = membership_form.__class__.__name__.lower(),
            )
        print rs.subject_identifier
        
        
rs = RegisteredSubject.objects.get(subject_identifier='056-4980421-1')       
membership_form = MaternalPostReg.objects.get(registered_subject=rs)
Appointment.objects.create_appointments( 
    registered_subject = rs, 
    base_appt_datetime = membership_form.created, 
    model_name = membership_form.__class__.__name__.lower(),
    )
print rs.subject_identifier            
