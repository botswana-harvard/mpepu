from django.db import models
from infant_visit import InfantVisit
from infant_base_uuid_model import InfantBaseUuidModel


class BaseScheduledVisitModel(InfantBaseUuidModel):

    infant_visit = models.OneToOneField(InfantVisit)

    def get_visit(self):
        return self.infant_visit

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.infant_visit.appointment.registered_subject.relative_identifier

    class Meta:
        abstract = True
