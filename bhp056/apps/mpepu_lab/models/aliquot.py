from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from edc.subject.registration.models import RegisteredSubject

from lis.specimen.lab_aliquot.managers import AliquotManager
from lis.specimen.lab_aliquot.models import BaseAliquot

from .aliquot_condition import AliquotCondition
from .aliquot_type import AliquotType
from .receive import Receive
from .infant_requisition import InfantRequisition


class Aliquot(BaseAliquot):

    receive = models.ForeignKey(Receive,
        editable=False)

    aliquot_type = models.ForeignKey(AliquotType,
        verbose_name="Aliquot Type",
        null=True)

    aliquot_condition = models.ForeignKey(AliquotCondition,
        verbose_name="Aliquot Condition",
        null=True,
        blank=True)

    objects = AliquotManager()

    def save(self, *args, **kwargs):
        self.subject_identifier = self.receive.registered_subject.subject_identifier
        if self.source_aliquot and not self.primary_aliquot:
            raise ValidationError('Primary aliquot may not be None')
        super(Aliquot, self).save(*args, **kwargs)

    @property
    def specimen_identifier(self):
        return self.aliquot_identifier[:-4]

    def get_visit(self):
        from apps.mpepu_infant.models import InfantVisit
        visit = self.get_visit_model()
        requisition = InfantRequisition.objects.get(requisition_identifier=self.aliquot_identifier[4:-4])
        if visit == InfantVisit:
            return requisition.infant_visit
        else:
            return requisition.maternal_visit
        return visit

    def get_visit_model(self):
        from apps.mpepu_infant.models import InfantVisit
        from apps.mpepu_maternal.models import MaternalVisit
        registered_subject = RegisteredSubject.objects.get(subject_identifier=self.subject_identifier)
        if registered_subject.subject_type.lower() == 'infant':
            return InfantVisit
        else:
            return MaternalVisit

    def to_process(self):
        url = reverse('admin:mpepu_lab_processing_add')
        return '<a href="{0}?aliquot={1}">process</a>'.format(url, self.pk)
    to_process.allow_tags = True

    class Meta:
        app_label = 'mpepu_lab'
        unique_together = (('receive', 'count'), )
        ordering = ('receive', 'count')
