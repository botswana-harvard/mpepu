from bhp_visit.models import VisitDefinition, ScheduleGroup, Appointment

def create_appointment( ** kwargs ):
    
    """create appointments based on a list of visit definitions if given model_name is a member of a schedule group
    
    Only create for visit_instance = 0
    If appointment exists, just update the appt_datetime
    """
    
    registered_subject = kwargs.get("registered_subject")
    model_name = kwargs.get("model_name")
    base_appt_datetime = kwargs.get("base_appt_datetime")
    
    if ScheduleGroup.objects.filter(membership_form__model = model_name):
        visits = VisitDefinition.objects.filter(schedule_group = ScheduleGroup.objects.get(membership_form__model = model_name))
        for visit in visits:
            if Appointment.objects.filter(registered_subject = registered_subject, visit_definition = visit, visit_instance = 0):
                appt = Appointment.objects.get(
                    registered_subject = registered_subject, 
                    visit_definition = visit, 
                    visit_instance = 0)
                appt.app_datetime = base_appt_datetime
                appt.save()
            else:
                Appointment.objects.create(
                    registered_subject = registered_subject,
                    visit_definition = visit,
                    visit_instance = 0,
                    appt_datetime = base_appt_datetime,
                    )



