from django.db import models, IntegrityError

from edc.subject.registration.models import BaseRegisteredSubjectModel
from edc.entry_meta_data.managers import EntryMetaDataManager

from .infant_off_study_mixin import InfantOffStudyMixin
from .infant_visit import InfantVisit


class BaseInfantRegisteredSubjectModel(InfantOffStudyMixin, BaseRegisteredSubjectModel):

    def safe_delete_appointment(self, code):
        """Deletes an appointment as long as the visit tracking form does not exist."""
        Appointment = models.get_model('appointment', 'Appointment')
        for appointment in Appointment.objects.filter(registered_subject=self.registered_subject, visit_definition__code=code, visit_instance='0'):
            if not InfantVisit.objects.filter(appointment=appointment):
                try:
                    appointment.delete()
                except IntegrityError:
                    pass

    def get_report_datetime(self):
        return self.get_registration_datetime()

    infant_visit = models.OneToOneField(InfantVisit)

    entry_meta_data_manager = EntryMetaDataManager(InfantVisit)

    class Meta:
        abstract = True
