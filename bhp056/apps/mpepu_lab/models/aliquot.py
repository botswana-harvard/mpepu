from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from lis.specimen.lab_aliquot.managers import AliquotManager
from lis.specimen.lab_aliquot.models import BaseAliquot

from .aliquot_condition import AliquotCondition
from .aliquot_type import AliquotType
from .receive import Receive


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

    def to_process(self):
        url = reverse('admin:mpepu_lab_processing_add')
        return '<a href="{0}?aliquot={1}">process</a>'.format(url, self.pk)
    to_process.allow_tags = True

    class Meta:
        app_label = 'mpepu_lab'
        unique_together = (('receive', 'count'), )
        ordering = ('receive', 'count')
