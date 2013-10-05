from datetime import timedelta
from edc.subject.appointment_helper.classes import AppointmentDateHelper


class InfantEligibilityMixin(object):

    def confirm_eligibility_datetime(self, appt_datetime, delivery_datetime, days):
        date_helper = AppointmentDateHelper()
        appt_datetime = date_helper._check_if_allowed_isoweekday(delivery_datetime + timedelta(days=days))
        while (appt_datetime - delivery_datetime).days < days:
            appt_datetime = appt_datetime + timedelta(days=1)
        if appt_datetime.strftime("%A") == 'Saturday':
            appt_datetime = appt_datetime + timedelta(days=2)
        if appt_datetime.strftime("%A") == 'Sunday':
            appt_datetime = appt_datetime + timedelta(days=1)
        return appt_datetime
