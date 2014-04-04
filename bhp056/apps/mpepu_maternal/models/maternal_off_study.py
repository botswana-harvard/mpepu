from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.subject.off_study.models.base_off_study import BaseOffStudy
from edc.entry_meta_data.managers import EntryMetaDataManager

from .maternal_visit import MaternalVisit


class MaternalOffStudy(BaseOffStudy):

    """ Maternal Off-Study.

    * Complete this form to record permanent discontinuation from all follow-up for each participant (Mother).
    * Header date equals "Off-Study Date", unless there is a death.In the event of death "Off-study Date"="Date of Death". """

    history = AuditTrail()

    maternal_visit = models.OneToOneField(MaternalVisit)

    entry_meta_data_manager = EntryMetaDataManager(MaternalVisit)

    def __unicode__(self):
        return '%s ' % (self.registered_subject)

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternaloffstudy_change', args=(self.id,))

    class Meta:
        verbose_name = "Maternal Off-Study"
        verbose_name_plural = "Maternal Off-Study"
        app_label = "mpepu_maternal"
