from django.db import models

from ..managers import ScheduledModelManager
from .maternal_visit import MaternalVisit
from .maternal_base_uuid_model import MaternalBaseUuidModel


class BaseScheduledVisitModel(MaternalBaseUuidModel):

    """ Base model for all scheduled models (adds key to :class:`MaternalVisit`). """

    maternal_visit = models.OneToOneField(MaternalVisit)

    objects = ScheduledModelManager()

    def natural_key(self):
        return self.subject_visit.natural_key()

    def __unicode__(self):
        return unicode(self.maternal_visit)

    def get_report_datetime(self):
        return self.maternal_visit.report_datetime

    def get_subject_identifier(self):
        return self.maternal_visit.appointment.registered_subject.subject_identifier

    def get_visit(self):
        return self.maternal_visit

    class Meta:
        abstract = True
