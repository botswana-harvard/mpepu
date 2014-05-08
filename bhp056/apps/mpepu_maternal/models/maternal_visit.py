from django.core.urlresolvers import reverse
from django.db import models, IntegrityError

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
        dct.update({'vital status': 'vital status'})
        del dct['death']
        return dct

    def save(self, *args, **kwargs):
        if self.reason == 'vital status':
            self.appointment.appt_type = 'telephone'
        self.create_meta_status_if_visit_reason_is_death()
        self.create_meta_status_if_visit_reason_is_off_study()
        self.avail_forms_on_visit_2000M_only_when_consent_version_is_greater_than_two()
        super(MaternalVisit, self).save(*args, **kwargs)

    def create_meta_status_if_visit_reason_is_death(self):
        if self.reason == 'death':
            forms = ['maternaldeath', 'maternaloffstudy']
            for add_forms in forms:
                entry = Entry.objects.get(model_name=add_forms, visit_definition_id=self.appointment.visit_definition_id)
                scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
                if not scheduled_meta_data:
                    scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
                else:
                    scheduled_meta_data = scheduled_meta_data[0]
                scheduled_meta_data.entry_status = 'NEW'
                scheduled_meta_data.save()
            return scheduled_meta_data

    def create_meta_status_if_visit_reason_is_off_study(self):
        if self.reason == 'off study':
            entry = Entry.objects.get(model_name='maternaloffstudy', visit_definition_id=self.appointment.visit_definition_id)
            scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
            if not scheduled_meta_data:
                scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
            else:
                scheduled_meta_data = scheduled_meta_data[0]
            scheduled_meta_data.entry_status = 'NEW'
            scheduled_meta_data.save()
            return scheduled_meta_data

    def avail_forms_on_visit_2000M_only_when_consent_version_is_greater_than_two(self):
        from .maternal_consent import MaternalConsent
        confirm_consent = MaternalConsent.objects.get(subject_identifier=self.registered_subject.subject_identifier)
        if confirm_consent.consent_version_recent >= 2:
            check = self.appointment.visit_definition.code == '2000M'
            if check and self.reason != 'death':
                avail_forms = ['feedingchoice', 'feedingchoicesectionone', 'feedingchoicesectiontwo', 'feedingchoicesectionthree']
                for forms in avail_forms:
                    entry = Entry.objects.get(model_name=forms, visit_definition_id=self.appointment.visit_definition_id)
                    scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
                    if not scheduled_meta_data:
                        scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
                    else:
                        scheduled_meta_data = scheduled_meta_data[0]
                    scheduled_meta_data.entry_status = 'NEW'
                    scheduled_meta_data.save()

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalvisit_change', args=(self.id,))

    class Meta:
        db_table = 'mpepu_maternal_maternalvisit'
        verbose_name = "Maternal Visit"
        app_label = "mpepu_maternal"
