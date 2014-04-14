from django.core.urlresolvers import reverse
from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.subject.visit_tracking.models import BaseVisitTracking
from edc.subject.visit_tracking.settings import VISIT_REASON_NO_FOLLOW_UP_CHOICES
from edc.entry_meta_data.models import ScheduledEntryMetaData
from edc.subject.entry.models import Entry


from .maternal_off_study_mixin import MaternalOffStudyMixin
from ..choices import VISIT_REASON, ALIVE_DEAD_UNKNOWN


class MaternalVisit(MaternalOffStudyMixin, BaseVisitTracking):

    """ Maternal visit form that links all follow-up forms """

    history = AuditTrail()

    survival_status = models.CharField(
        max_length=10,
        verbose_name="Survival status",
        choices=ALIVE_DEAD_UNKNOWN,
        null=True,
        blank=False)

    date_last_alive = models.DateField(
        verbose_name="Date last known alive",
        help_text="",
        null=True,
        blank=True
        )

    @property
    def registered_subject(self):
        return self.get_registered_subject()

    def __unicode__(self):
        return unicode(self.appointment)

    def get_visit_reason_choices(self):
        return VISIT_REASON

    def get_visit_reason_no_follow_up_choices(self):
        """Returns the visit reasons that do not imply any data collection; that is, the subject is not available."""
        dct = {}
        for item in VISIT_REASON_NO_FOLLOW_UP_CHOICES:
            dct.update({item: item})
        del dct['death']
        dct.update({'vital status': 'vital status'})
        return dct

    def save(self, *args, **kwargs):
        if self.reason == 'vital status':
            self.appointment.appt_type = 'telephone'
        self.change_meta_status_if_visit_reason_is_death()
        super(MaternalVisit, self).save(*args, **kwargs)

    def change_meta_status_if_visit_reason_is_death(self):
        if self.reason == 'death':
            entry = Entry.objects.get(model_name='maternaldeath', visit_definition_id=self.appointment.visit_definition_id)
            scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject, entry_status='NEW')
            return scheduled_meta_data

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalvisit_change', args=(self.id,))

    class Meta:
        db_table = 'mpepu_maternal_maternalvisit'
        verbose_name = "Maternal Visit"
        app_label = "mpepu_maternal"
