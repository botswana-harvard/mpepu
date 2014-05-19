from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

from edc.audit.audit_trail import AuditTrail
from edc.subject.visit_tracking.models.base_visit_tracking import BaseVisitTracking
from edc.subject.visit_tracking.settings import VISIT_REASON_NO_FOLLOW_UP_CHOICES
from edc.entry_meta_data.models import ScheduledEntryMetaData, RequisitionMetaData
from edc.subject.entry.models import Entry, LabEntry
from edc.subject.registration.models import RegisteredSubject
from edc.lab.lab_clinic_api.models import Panel

from apps.mpepu.choices import INFO_PROVIDER
from apps.mpepu_infant.choices import INFANT_VISIT_STUDY_STATUS, ALIVE_DEAD_UNKNOWN, VISIT_REASON

from .infant_off_study_mixin import InfantOffStudyMixin


class InfantVisit(InfantOffStudyMixin, BaseVisitTracking):

    information_provider = models.CharField(
        verbose_name="Please indicate who provided most of the information for this child's visit",
        choices=INFO_PROVIDER,
        max_length=20,
        help_text="",
        )

    information_provider_other = models.CharField(
        verbose_name=" if information provider is Other, please specify",
        max_length=20,
        help_text="",
        blank=True,
        null=True,
        )

    study_status = models.CharField(
        verbose_name="What is the participant's current study status",
        max_length=50,
        choices=INFANT_VISIT_STUDY_STATUS,
        )
    #additional v2 fields
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

    history = AuditTrail()

    objects = models.Manager()

    def __unicode__(self):
        return unicode(self.appointment)

    def get_visit_reason_choices(self):
        return VISIT_REASON

    def get_visit_reason_no_follow_up_choices(self):
        """Returns the visit reasons that do not imply any data collection; that is, the subject is not available."""
        dct = {}
        for item in VISIT_REASON_NO_FOLLOW_UP_CHOICES:
            dct.update({item: item})
        dct.update({'deferred': 'deferred'})
        dct.update({'vital status': 'vital status'})
        del dct['death']
        del dct['lost']
        return dct

    @property
    def registered_subject(self):
        return self.get_registered_subject()

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantvisit_change', args=(self.id,))

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.appointment.registered_subject.relative_identifier

    def requires_infant_eligibility(self, infant_visit, exception_cls=None):
        """Requires InfantEligibility to be completed for any visit after 2000 or InfantPreEligibility for 2015 ."""
        if not exception_cls:
            exception_cls = ValidationError
        # must have InfantEligibility or InfantPreEligibility
        InfantEligibility = models.get_model('mpepu_infant', 'InfantEligibility')
        has_infant_eligibility = InfantEligibility.objects.filter(registered_subject=infant_visit.appointment.registered_subject).exists()
        InfantPreEligibility = models.get_model('mpepu_infant', 'InfantPreEligibility')
        has_infant_pre_eligibility = InfantPreEligibility.objects.filter(registered_subject=infant_visit.appointment.registered_subject).exists()
        if not has_infant_eligibility and not has_infant_pre_eligibility:
            if infant_visit.appointment.visit_definition.code != '2000' and infant_visit.reason in ['scheduled', 'unscheduled']:
                raise exception_cls('Please complete the Infant Eligibility or Infant Pre-eligibility before conducting scheduled visits beyond visit 2000.')
        if not has_infant_eligibility and has_infant_pre_eligibility:
            if infant_visit.appointment.visit_definition.code != '2000' and infant_visit.reason in ['scheduled', 'unscheduled']:
                raise exception_cls('Please complete the Infant Eligibility before conducting scheduled visits beyond visit 2000.')

    def check_previous_visit_keyed(self, infant_visit, exception_cls=None):
        """Check that previous visit has been keyed before allowing saving of current visit"""
        if not exception_cls:
            exception_cls = ValidationError
        e_codes = ['2000', '2010', '2020', '2030', '2060', '2090', '2120', '2150', '2180']
        pre_codes = ['2000', '2010', '2015', '2020', '2030', '2060', '2090', '2120', '2150', '2180']
        InfantPreEligibility = models.get_model('mpepu_infant', 'InfantPreEligibility')
        has_infant_pre_eligibility = InfantPreEligibility.objects.filter(registered_subject=infant_visit.appointment.registered_subject)

        if has_infant_pre_eligibility:
            index = pre_codes.index(infant_visit.appointment.visit_definition.code)
            prev_visit = InfantVisit.objects.filter(subject_identifier=infant_visit.registered_subject.subject_identifier, appointment__visit_definition__code=pre_codes.pop(index - 1))
        else:
            index = e_codes.index(infant_visit.appointment.visit_definition.code)
            prev_visit = InfantVisit.objects.filter(subject_identifier=infant_visit.registered_subject.subject_identifier, appointment__visit_definition__code=e_codes.pop(index - 1))

        if not prev_visit and index != 0:
            raise exception_cls('You cannot complete an Infant Visit, when previous visit has not been keyed. Please go back and key it in.')
        return True

    def change_meta_data_status_on_2180_if_visit_is_missed_at_2150(self):
        check = InfantVisit.objects.filter(appointment__registered_subject=self.registered_subject, appointment__visit_definition__code='2180').exists()
        if check:
            app = InfantVisit.objects.filter(appointment__registered_subject=self.registered_subject, appointment__visit_definition__code='2150', reason='missed')
            if app:
                enabled_forms = ['infantoffdrug', 'infantoffstudy']
                for required_form in enabled_forms:
                    entry = Entry.objects.filter(model_name=required_form, visit_definition_id=self.appointment.visit_definition_id)
                    if entry:
                        scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry[0], registered_subject=self.registered_subject)
                        if not scheduled_meta_data:
                            scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry[0], registered_subject=self.registered_subject)
                        else:
                            scheduled_meta_data = scheduled_meta_data[0]
                        scheduled_meta_data.entry_status = 'NEW'
                        scheduled_meta_data.save()

    def save(self, *args, **kwargs):
        if self.reason == 'deferred':
            if self.appointment.visit_definition.code != '2010':
                raise ValidationError('Reason option \'deferred\' may only be used for the 2010 visit')
        if self.reason == 'vital status':
            self.appointment.appt_type = 'telephone'
        self.get_visit_reason_no_follow_up_choices()
        self.requires_infant_eligibility(self)
#         self.check_previous_visit_keyed(self)
        self.create_meta_if_visit_reason_is_death_when_sid_is_none()
        self.create_meta_if_visit_reason_is_death_when_sid_is_not_none()
        self.create_meta_if_visit_reason_is_lost_when_sid_is_none()
        self.create_meta_if_visit_reason_is_lost_when_sid_is_not_none()
        self.change_meta_data_status_if_visit_reason_is_off_study()
        self.change_meta_data_status_if_study_status_is_onstudy_rando_offdrug()
        self.change_meta_data_status_if_survial_status_is_dead()
        self.change_meta_data_status_if_info_source_is_telephone()
        self.change_meta_data_status_on_2180_if_visit_is_missed_at_2150()
        self.disable_dna_pcr_when_feeding_choice_is_formula_feeding()
        self.get_new_v4_forms()
        super(InfantVisit, self).save(*args, **kwargs)

    def create_meta_if_visit_reason_is_death_when_sid_is_none(self):
        if self.reason == 'death':
            rs = RegisteredSubject.objects.get(subject_identifier=self.registered_subject.subject_identifier)
            if not rs.sid:
                forms = ['infantdeath', 'infantprerandoloss', 'infantsurvival', 'infantverbalautopsy', 'infantoffstudy']
                for form in forms:
                    entry = Entry.objects.get(model_name=form, visit_definition_id=self.appointment.visit_definition_id)
                    scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
                    if not scheduled_meta_data:
                        scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
                    else:
                        scheduled_meta_data = scheduled_meta_data[0]
                    scheduled_meta_data.entry_status = 'NEW'
                    scheduled_meta_data.save()

    def create_meta_if_visit_reason_is_death_when_sid_is_not_none(self):
        if self.reason == 'death':
            rs = RegisteredSubject.objects.get(subject_identifier=self.registered_subject.subject_identifier)
            if rs.sid:
                forms = ['infantdeath', 'infantsurvival', 'infantverbalautopsy', 'infantoffstudy']
                if self.appointment.visit_definition.code != '2000' and self.appointment.visit_definition.code != '2010':
                    forms.append('infantoffdrug')
                for form in forms:
                    entry = Entry.objects.get(model_name=form, visit_definition_id=self.appointment.visit_definition_id)
                    scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
                    if not scheduled_meta_data:
                        scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
                    else:
                        scheduled_meta_data = scheduled_meta_data[0]
                    scheduled_meta_data.entry_status = 'NEW'
                    scheduled_meta_data.save()

    def create_meta_if_visit_reason_is_lost_when_sid_is_none(self):
        if self.reason == 'lost':
            rs = RegisteredSubject.objects.get(subject_identifier=self.registered_subject.subject_identifier)
            if not rs.sid:
                forms = ['infantprerandoloss', 'infantoffstudy']
                for form in forms:
                    entry = Entry.objects.get(model_name=form, visit_definition_id=self.appointment.visit_definition_id)
                    scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
                    if not scheduled_meta_data:
                        scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
                    else:
                        scheduled_meta_data = scheduled_meta_data[0]
                    scheduled_meta_data.entry_status = 'NEW'
                    scheduled_meta_data.save()

    def create_meta_if_visit_reason_is_lost_when_sid_is_not_none(self):
        if self.reason == 'lost':
            rs = RegisteredSubject.objects.get(subject_identifier=self.registered_subject.subject_identifier)
            if rs.sid:
                forms = ['infantoffdrug', 'infantoffstudy']
                for form in forms:
                    entry = Entry.objects.get(model_name=form, visit_definition_id=self.appointment.visit_definition_id)
                    scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
                    if not scheduled_meta_data:
                        scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
                    else:
                        scheduled_meta_data = scheduled_meta_data[0]
                    scheduled_meta_data.entry_status = 'NEW'
                    scheduled_meta_data.save()

    def change_meta_data_status_if_visit_reason_is_off_study(self):
        if self.reason == 'off study':
            entry = Entry.objects.get(model_name='infantoffstudy', visit_definition_id=self.appointment.visit_definition_id)
            scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
            if not scheduled_meta_data:
                scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
            else:
                scheduled_meta_data = scheduled_meta_data[0]
            scheduled_meta_data.entry_status = 'NEW'
            scheduled_meta_data.save()
            return scheduled_meta_data

    def change_meta_data_status_if_study_status_is_onstudy_rando_offdrug(self):
        if self.study_status == 'onstudy rando offdrug':
            entry = Entry.objects.get(model_name='infantoffdrug', visit_definition_id=self.appointment.visit_definition_id)
            scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
            if not scheduled_meta_data:
                scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
            else:
                scheduled_meta_data = scheduled_meta_data[0]
            scheduled_meta_data.entry_status = 'NEW'
            scheduled_meta_data.save()
            return scheduled_meta_data

    def change_meta_data_status_if_survial_status_is_dead(self):
        if self.survival_status == 'DEAD':
            entry = Entry.objects.get(model_name='infantdeath', visit_definition_id=self.appointment.visit_definition_id)
            scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
            if not scheduled_meta_data:
                scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
            else:
                scheduled_meta_data = scheduled_meta_data[0]
            scheduled_meta_data.entry_status = 'NEW'
            scheduled_meta_data.save()
            return scheduled_meta_data

    def change_meta_data_status_if_info_source_is_telephone(self):
        if self.info_source == 'telephone':
            if self.reason != 'vital status':
                marked_forms = ['infantfu', 'infantfuphysical', 'infantfud', 'infantfudx', 'infantfudx2proph', 'infantfunewmed', 'infantfumed']
                for forms in marked_forms:
                    entry = Entry.objects.get(model_name=forms, visit_definition_id=self.appointment.visit_definition_id)
                    scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
                    if not scheduled_meta_data:
                        scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry, registered_subject=self.registered_subject)
                    else:
                        scheduled_meta_data = scheduled_meta_data[0]
                    scheduled_meta_data.entry_status = 'NOT_REQUIRED'
                    scheduled_meta_data.save()

    def disable_dna_pcr_when_feeding_choice_is_formula_feeding(self):
        from ...mpepu_maternal.models import MaternalConsent
        check_consent = MaternalConsent.objects.filter(subject_identifier=self.registered_subject.relative_identifier)
        if check_consent[0].consent_version_recent >= 4:
            from .infant_eligibility import InfantEligibility
            ff = InfantEligibility.objects.filter(registered_subject=self.registered_subject)
            if ff and ff[0].maternal_feeding_choice == 'FF':
                if self.appointment.visit_definition.code != '2000' and self.appointment.visit_definition.code != '2010' and self.appointment.visit_definition.code != '2015':
                    panel = Panel.objects.filter(edc_name='DNA PCR')
                    if panel:
                        lab_entry = LabEntry.objects.get(model_name='infantrequisition', requisition_panel_id=panel[0].id, visit_definition_id=self.appointment.visit_definition_id)
                        requisition_meta_data = RequisitionMetaData.objects.filter(appointment_id=self.appointment.id, lab_entry_id=lab_entry.id, registered_subject_id=self.registered_subject.id)
                        if requisition_meta_data:
                            requisition_meta_data.entry_status = 'NOT_REQUIRED'
                            requisition_meta_data.save()

    def get_new_v4_forms(self):
        new_forms = ['infantstoolcollection']
        lab_model = ['infantrequisition']
        from ...mpepu_maternal.models import MaternalConsent
        check_consent = MaternalConsent.objects.filter(subject_identifier=self.registered_subject.relative_identifier)
        if check_consent[0].consent_version_recent >= 4:
            if self.appointment.visit_definition.code == '2010' and self.appointment.visit_definition.code == '2030' and self.appointment.visit_definition.code == '2060' and self.appointment.visit_definition.code == '2180':
                for form in new_forms:
                    entry = Entry.objects.filter(model_name=form, visit_definition_id=self.appointment.visit_definition_id)
                    if entry:
                        scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry[0], registered_subject=self.registered_subject)
                        if not scheduled_meta_data:
                            scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry[0], registered_subject=self.registered_subject)
                        else:
                            scheduled_meta_data = scheduled_meta_data[0]
                        scheduled_meta_data.entry_status = 'NEW'
                        scheduled_meta_data.save()
                for new_lab in lab_model:
                    panel = Panel.objects.get(edc_name='Stool storage')
                    lab_entry = LabEntry.objects.filter(model_name=new_lab, requisition_panel_id=panel.id, visit_definition_id=self.appointment.visit_definition_id)
                    if lab_entry:
                        requisition_meta_data = RequisitionMetaData.objects.filter(appointment=self.appointment, lab_entry=lab_entry[0], registered_subject=self.registered_subject)
                        if not requisition_meta_data:
                            requisition_meta_data = RequisitionMetaData.objects.create(appointment=self.appointment, lab_entry=lab_entry[0], registered_subject=self.registered_subject)
                        else:
                            requisition_meta_data = requisition_meta_data[0]
                        requisition_meta_data.entry_status = 'NEW'
                        requisition_meta_data.save()

    class Meta:
        db_table = 'mpepu_infant_infantvisit'
        app_label = "mpepu_infant"
        verbose_name = "Infant Visit"
