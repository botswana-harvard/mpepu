from datetime import datetime, date

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models, IntegrityError

from edc.audit.audit_trail import AuditTrail
from edc.entry_meta_data.models import ScheduledEntryMetaData, RequisitionMetaData
from edc.subject.visit_tracking.models import BaseVisitTracking
from edc.subject.visit_tracking.settings import VISIT_REASON_NO_FOLLOW_UP_CHOICES

from apps.mpepu.classes.mpepu_meta_data_mixin import MpepuMetaDataMixin

from .maternal_off_study_mixin import MaternalOffStudyMixin
from ..choices import VISIT_REASON, ALIVE_DEAD_UNKNOWN


class MaternalVisit(MaternalOffStudyMixin, BaseVisitTracking, MpepuMetaDataMixin):

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
        if self.appointment.visit_definition.code == '2180M':
            return dct
        else:
            for item in VISIT_REASON_NO_FOLLOW_UP_CHOICES:
                dct.update({item: item})
            dct.update({'vital status': 'vital status'})
            del dct['death']
            del dct['lost']
            return dct

    def save(self, *args, **kwargs):
        self.recalculate_meta(self)
        if self.reason == 'vital status':
            self.appointment.appt_type = 'telephone'
        self.create_meta_status_if_visit_reason_is_death()
        self.create_meta_status_if_visit_reason_is_off_study()
        self.avail_forms_on_visit_2000M_only_when_consent_version_is_greater_than_two()
        self.enable_2180M_forms()
        self.change_meta_if_visit_reason_lost()
        super(MaternalVisit, self).save(*args, **kwargs)

    def maternal_mpepu_cessation_post_save(self):
        if self.reason != 'scheduled':
            if self.report_datetime.date() >= date(2015, 4, 7):
                forms = ['maternaloffstudy']
                scheduled_meta = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, registered_subject=self.registered_subject)
                for meta in scheduled_meta:
                    if meta.entry.model_name not in forms:
                        meta.delete()
                requisition_meta = RequisitionMetaData.objects.filter(appointment=self.appointment, registered_subject=self.registered_subject)
                requisition_meta.delete()

    def create_meta_status_if_visit_reason_is_death(self):
        if self.reason == 'death':
            forms = ['maternaldeath', 'maternaloffstudy']
            for form in forms:
                entry = self.query_entry(form, self.appointment.visit_definition)
                self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)

    def create_meta_status_if_visit_reason_is_off_study(self):
        if self.reason == 'off study':
            form = 'maternaloffstudy'
            entry = self.query_entry(form, self.appointment.visit_definition)
            self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)

    def avail_forms_on_visit_2000M_only_when_consent_version_is_greater_than_two(self):
        from .maternal_consent import MaternalConsent
        confirm_consent = MaternalConsent.objects.get(subject_identifier=self.registered_subject.subject_identifier)
        if confirm_consent.consent_version_recent >= 2 or confirm_consent.consent_datetime >= datetime(2013, 1, 21, 7, 0):
            if self.appointment.visit_definition.code == '2000M' or self.appointment.visit_definition.code == '1000M':
                if self.reason != 'death':
                    avail_forms = ['feedingchoice', 'feedingchoicesectionone', 'feedingchoicesectiontwo', 'feedingchoicesectionthree']
                    for form in avail_forms:
                        entry = self.query_entry(form, self.appointment.visit_definition)
                        self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)

    def enable_2180M_forms(self):
        if self.appointment.visit_definition.code == '2180M':
            entry = self.query_entry('maternaloffstudy', self.appointment.visit_definition)
            self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)

    def change_meta_if_visit_reason_lost(self):
        if self.reason == 'lost':
            form = 'maternaloffstudy'
            entry = self.query_entry(form, self.appointment.visit_definition)
            self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalvisit_change', args=(self.id,))

    def recalculate_death_meta(self, scheduled_meta_data, requisition_meta_data):
        flag = False
        count = 0
        for meta_data in scheduled_meta_data:
            if meta_data.entry_status == 'KEYED':
                if meta_data.entry.model_name == 'maternaldeath':
                    flag = True
                    count = count + 1
                if meta_data.entry.model_name == 'maternaloffstudy':
                    flag = True
                    count = count + 1
                if not flag:
                    meta_data.delete()
        if count > 0:
            return True
        else:
            return False

    def recalculate_missed_meta(self, scheduled_meta_data, requisition_meta_data):
        flag = False
        count = 0
        for meta_data in scheduled_meta_data:
            if meta_data.entry.model_name == 'maternaloffstudy':
                flag = True
                count = count + 1
            if not flag:
                meta_data.delete()
        if count > 0:
            return True
        else:
            return False

    def recalculate_meta(self, maternal_visit, exception_cls=None):
        """Ensure that the metadata for every visit is always re-calculated with every save"""
        if not exception_cls:
            exception_cls = ValidationError
        # Check if the visit report is being modified and not new
        if self.id is not None:
            scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, registered_subject=self.registered_subject)
            requisition_meta_data = RequisitionMetaData.objects.filter(appointment=self.appointment, registered_subject=self.registered_subject)
            empty = self.remove_all_meta_data(self.appointment, self.registered_subject, scheduled_meta_data, requisition_meta_data)
            if not empty:
                if maternal_visit.reason == 'missed':
                    if self.appointment.visit_definition.code != '2180M':
                        raise exception_cls('Please delete all filled in forms before you may change the visit to Missed.')
                    else:
                        missed_2180 = maternal_visit.recalculate_missed_meta(scheduled_meta_data, requisition_meta_data)
                        if not missed_2180:
                            raise exception_cls('Please delete all filled in forms before you may change the visit to Missed.')
                if maternal_visit.reason == 'vital status':
                    if self.appointment.visit_definition.code != '2180M':
                        raise exception_cls('Please delete all filled in forms before you may change the visit to Vital Status.')
                    else:
                        vital_status_2180 = maternal_visit.recalculate_missed_meta(scheduled_meta_data, requisition_meta_data)
                        if not vital_status_2180:
                            raise exception_cls('Please delete all filled in forms before you may change the visit to Vital Status.')
                if maternal_visit.reason == 'death':
                    death = maternal_visit.recalculate_death_meta(scheduled_meta_data, requisition_meta_data)
                    if not death:
                        raise exception_cls('Please delete all filled in forms that are not Death forms before you may change the visit to Death.')

    class Meta:
        db_table = 'mpepu_maternal_maternalvisit'
        verbose_name = "Maternal Visit"
        app_label = "mpepu_maternal"
