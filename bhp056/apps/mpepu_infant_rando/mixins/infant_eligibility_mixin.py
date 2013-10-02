from datetime import timedelta
from edc.subject.appointment_helper.classes import AppointmentDateHelper


class InfantEligibilityMixin(object):

    def confirm_eligibility_datetime(self, appt_datetime, delivery_datetime, days):
        date_helper = AppointmentDateHelper()
        appt_datetime = date_helper._check_if_allowed_isoweekday(delivery_datetime + timedelta(days=days))
        #print '{0}, {1}'.format(appt_datetime.strftime("%A"), (appt_datetime - delivery_datetime).days)
        while (appt_datetime - delivery_datetime).days < days:
            appt_datetime = appt_datetime + timedelta(days=1)
        #print '{0}, {1}'.format(appt_datetime.strftime("%A"), (appt_datetime - delivery_datetime).days)
        if appt_datetime.strftime("%A") == 'Saturday':
            appt_datetime = appt_datetime + timedelta(days=2)
        #print '{0}, {1}'.format(appt_datetime.strftime("%A"), (appt_datetime - delivery_datetime).days)
        if appt_datetime.strftime("%A") == 'Sunday':
            appt_datetime = appt_datetime + timedelta(days=1)
        #print '{0}, {1}'.format(appt_datetime.strftime("%A"), (appt_datetime - delivery_datetime).days)
        return appt_datetime
