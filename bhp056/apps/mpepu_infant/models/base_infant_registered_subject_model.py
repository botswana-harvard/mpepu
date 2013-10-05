from django.db import models

from edc.subject.registration.models import BaseRegisteredSubjectModel

from .infant_off_study_mixin import InfantOffStudyMixin
from .infant_visit import InfantVisit


class BaseInfantRegisteredSubjectModel(InfantOffStudyMixin, BaseRegisteredSubjectModel):

    def safe_delete_appointment(self, code):
        """Deletes an appointment as long as the visit tracking form does not exist."""
        Appointment = models.get_model('bhp_appointment', 'Appointment')
        appointment = Appointment.objects.filter(registered_subject=self.registered_subject, visit_definition__code=code, visit_instance='0')
        if appointment:
            if not InfantVisit.objects.filter(appointment=appointment):
                appointment.delete()

    def get_report_datetime(self):
        return self.get_registration_datetime()

    class Meta:
        abstract = True
