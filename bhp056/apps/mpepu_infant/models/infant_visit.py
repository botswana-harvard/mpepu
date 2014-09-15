from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

from edc.audit.audit_trail import AuditTrail
from edc.entry_meta_data.models import ScheduledEntryMetaData, RequisitionMetaData
from edc.subject.appointment.constants import IN_PROGRESS, DONE, INCOMPLETE, NEW
from edc.subject.entry.models import Entry, LabEntry
from edc.subject.registration.models import RegisteredSubject
from edc.subject.visit_tracking.models.base_visit_tracking import BaseVisitTracking
from edc.subject.visit_tracking.settings import VISIT_REASON_NO_FOLLOW_UP_CHOICES, VISIT_REASON_FOLLOW_UP_CHOICES
from edc.subject.rule_groups.classes import site_rule_groups
from edc.entry_meta_data.helpers import ScheduledEntryMetaDataHelper, RequisitionMetaDataHelper

from apps.mpepu.choices import INFO_PROVIDER
from apps.mpepu.classes.mpepu_meta_data_mixin import MpepuMetaDataMixin
from apps.mpepu_infant.choices import INFANT_VISIT_STUDY_STATUS, ALIVE_DEAD_UNKNOWN, VISIT_REASON
from apps.mpepu_lab.models.panel import Panel

from .infant_off_study_mixin import InfantOffStudyMixin


class InfantVisit(InfantOffStudyMixin, BaseVisitTracking, MpepuMetaDataMixin):

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
        if self.appointment.visit_definition.code == '2180':
            return dct
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
        if self.appointment.visit_definition.code == '2180':
            app = InfantVisit.objects.filter(appointment__registered_subject=self.registered_subject, appointment__visit_definition__code='2150', reason='missed')
            if app:
                enabled_forms = ['infantoffdrug', 'infantoffstudy']
                for form in enabled_forms:
                    entry = self.query_entry(form, self.appointment.visit_definition)
                    self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)

    def save(self, *args, **kwargs):
        self.recalculate_meta(self)
        if self.reason == 'deferred':
            if self.appointment.visit_definition.code != '2010':
                raise ValidationError('Reason option \'deferred\' may only be used for the 2010 visit')
        if self.reason == 'vital status':
            self.appointment.appt_type = 'telephone'
        self.get_visit_reason_no_follow_up_choices()
        self.requires_infant_eligibility(self)
        self.check_previous_visit_keyed(self)
        self.create_meta_if_visit_reason_is_death_when_sid_is_none()
        self.create_meta_if_visit_reason_is_death_when_sid_is_not_none()
        self.create_meta_if_visit_reason_is_lost_when_sid_is_none()
        self.create_meta_if_visit_reason_is_lost_when_sid_is_not_none()
        self.change_meta_data_status_if_visit_reason_is_off_study()
        self.change_meta_data_status_if_study_status_is_onstudy_rando_offdrug()
        self.change_meta_data_status_if_study_status_is_onstudy_rando_ondrug()
        self.change_meta_data_status_if_survial_status_is_dead()
        self.change_meta_data_status_if_info_source_is_telephone()
        self.change_meta_data_status_on_2180_if_visit_is_missed_at_2150()
        self.disable_dna_pcr_when_feeding_choice_is_formula_feeding()
        self.disable_v4_forms()
        self.enable_2180_forms()
        super(InfantVisit, self).save(*args, **kwargs)

    def create_meta_if_visit_reason_is_death_when_sid_is_none(self):
        if self.reason == 'death':
            rs = RegisteredSubject.objects.get(subject_identifier=self.registered_subject.subject_identifier)
            if not rs.sid:
                forms = ['infantdeath', 'infantprerandoloss', 'infantsurvival', 'infantverbalautopsy', 'infantoffstudy']
                for form in forms:
                    entry = self.query_entry(form, self.appointment.visit_definition)
                    self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)

    def create_meta_if_visit_reason_is_death_when_sid_is_not_none(self):
        if self.reason == 'death':
            rs = RegisteredSubject.objects.get(subject_identifier=self.registered_subject.subject_identifier)
            if rs.sid:
                forms = ['infantdeath', 'infantsurvival', 'infantverbalautopsy', 'infantoffstudy']
                if self.appointment.visit_definition.code != '2000' and self.appointment.visit_definition.code != '2010':
                    forms.append('infantoffdrug')
                for form in forms:
                    entry = self.query_entry(form, self.appointment.visit_definition)
                    self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)

    def create_meta_if_visit_reason_is_lost_when_sid_is_none(self):
        if self.reason == 'lost':
            rs = RegisteredSubject.objects.get(subject_identifier=self.registered_subject.subject_identifier)
            if not rs.sid:
                forms = ['infantprerandoloss', 'infantoffstudy']
                for form in forms:
                    entry = self.query_entry(form, self.appointment.visit_definition)
                    self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)

    def create_meta_if_visit_reason_is_lost_when_sid_is_not_none(self):
        if self.reason == 'lost':
            rs = RegisteredSubject.objects.get(subject_identifier=self.registered_subject.subject_identifier)
            if rs.sid:
                forms = ['infantoffdrug', 'infantoffstudy']
                for form in forms:
                    entry = self.query_entry(form, self.appointment.visit_definition)
                    self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)

    def change_meta_data_status_if_visit_reason_is_off_study(self):
        if self.reason == 'off study':
            form = 'infantoffstudy'
            entry = self.query_entry(form, self.appointment.visit_definition)
            self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)

    def change_meta_data_status_if_study_status_is_onstudy_rando_offdrug(self):
        from .infant_off_drug import InfantOffDrug
        if self.study_status == 'onstudy rando offdrug':
            if not InfantOffDrug.objects.filter(registered_subject=self.registered_subject).exists():
                entry = self.query_entry('infantoffdrug', self.appointment.visit_definition)
                self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)

    def change_meta_data_status_if_study_status_is_onstudy_rando_ondrug(self):
        if self.study_status == 'onstudy rando ondrug':
            entry = self.query_entry('infantoffdrug', self.appointment.visit_definition)
            scheduled_meta_data = self.query_scheduled_meta_data(self.appointment, entry, self.registered_subject)
            if scheduled_meta_data:
                scheduled_meta_data.entry_status = 'NOT_REQUIRED'
                scheduled_meta_data.save()

    def change_meta_data_status_if_survial_status_is_dead(self):
        if self.survival_status == 'DEAD':
            form = 'infantdeath'
            entry = self.query_entry(form, self.appointment.visit_definition)
            self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)

    def change_meta_data_status_if_info_source_is_telephone(self):
        if self.info_source == 'telephone':
            if self.reason != 'vital status':
                marked_forms = ['infantfu', 'infantfuphysical', 'infantfud', 'infantfudx', 'infantfudx2proph', 'infantfunewmed', 'infantfumed']
                for form in marked_forms:
                    entry = self.query_entry(form, self.appointment.visit_definition)
                    scheduled_meta_data = self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)
                    scheduled_meta_data.entry_status = 'NOT_REQUIRED'
                    scheduled_meta_data.save()

    def disable_dna_pcr_when_feeding_choice_is_formula_feeding(self):
        from .infant_eligibility import InfantEligibility
        ff = InfantEligibility.objects.filter(registered_subject=self.registered_subject)
        if ff and ff[0].maternal_feeding_choice == 'FF':
            if self.appointment.visit_definition.code != '2000' and self.appointment.visit_definition.code != '2010' and self.appointment.visit_definition.code != '2015':
                panel = Panel.objects.filter(name='DNA PCR')
                lab_model = 'infantrequisition'
                if panel:
                    lab_entry = self.query_lab_entry(lab_model, panel, self.appointment.visit_definition)
                    requisition_meta_data = self.create_requisition_meta_data(self.appointment, lab_entry, self.registered_subject)
                    requisition_meta_data.entry_status = 'NOT_REQUIRED'
                    requisition_meta_data.save()

    def disable_v4_forms(self):
        new_forms = ['infantstoolcollection']
        lab_model = ['infantrequisition']
        from ...mpepu_maternal.models import MaternalConsent
        check_consent = MaternalConsent.objects.filter(subject_identifier=self.registered_subject.relative_identifier)
        #Ensures that Infant stool is not required for all consent versions less than four
        if check_consent[0].consent_version_recent < 4:
            if self.appointment.visit_definition.code == '2010' or self.appointment.visit_definition.code == '2030' or self.appointment.visit_definition.code == '2060' or self.appointment.visit_definition.code == '2180':
                for form in new_forms:
                    entry = self.query_entry(form, self.appointment.visit_definition)
                    scheduled_meta_data = self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)
                    scheduled_meta_data.entry_status = 'NOT_REQUIRED'
                    scheduled_meta_data.save()
                for lab in lab_model:
                    panel = Panel.objects.get(name='Stool storage')
                    lab_entry = self.query_lab_entry(lab, panel, self.appointment.visit_definition)
                    requisition_meta_data = self.create_requisition_meta_data(self.appointment, lab_entry, self.registered_subject)
                    requisition_meta_data.entry_status = 'NOT_REQUIRED'
                    requisition_meta_data.save()

    def enable_2180_forms(self):
        from .infant_off_drug import InfantOffDrug
        if self.appointment.visit_definition.code == '2180':
            entry = self.query_entry('infantoffstudy', self.appointment.visit_definition)
            self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)
            if not InfantOffDrug.objects.filter(registered_subject=self.appointment.registered_subject):
                entry = self.query_entry('infantoffdrug', self.appointment.visit_definition)
                self.create_scheduled_meta_data(self.appointment, entry, self.registered_subject)
            if self.reason == 'vital status' or self.reason == 'missed':
                entry = self.query_entry('infantstoolcollection', self.appointment.visit_definition)
                scheduled_meta_data = self.query_scheduled_meta_data(self.appointment, entry, self.registered_subject)
                scheduled_meta_data.delete()
                requisitions = RequisitionMetaData.objects.filter(appointment=self.appointment)
                requisitions.delete()

    def recalculate_death_meta(self, scheduled_meta_data, requisition_meta_data):
        flag = False
        count = 0
        for meta_data in scheduled_meta_data:
            if meta_data.entry_status == 'KEYED':
                if meta_data.entry.model_name == 'infantdeath':
                    flag = True
                    count = count + 1
                if meta_data.entry.model_name == 'infantsurvival':
                    flag = True
                    count = count + 1
                if meta_data.entry.model_name == 'infantverbalautopsy':
                    flag = True
                    count = count + 1
                if meta_data.entry.model_name == 'infantoffstudy':
                    flag = True
                    count = count + 1
                if meta_data.entry.model_name == 'infantoffdrug' and self.appointment.visit_definition.code != '2000':
                    flag = True
                    count = count + 1
                if meta_data.entry.model_name == 'infantprerandoloss' and self.appointment.visit_definition.code == '2000':
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
            if meta_data.entry.model_name == 'infantoffstudy':
                flag = True
                count = count + 1
            if not flag:
                meta_data.delete()
        if count > 0:
            return True
        else:
            return False

    def recalculate_meta(self, infant_visit, exception_cls=None):
        """Ensure that the metadata for every visit is always re-calculated with every save"""
        if not exception_cls:
            exception_cls = ValidationError
        # Check if the visit report is being modified and not new
        if self.id is not None:
            scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, registered_subject=self.registered_subject)
            requisition_meta_data = RequisitionMetaData.objects.filter(appointment=self.appointment, registered_subject=self.registered_subject)
            empty = self.remove_all_meta_data(self.appointment, self.registered_subject, scheduled_meta_data, requisition_meta_data)
            if not empty:
                if infant_visit.reason == 'missed':
                    if self.appointment.visit_definition.code != '2180':
                        raise exception_cls('Please delete all filled in forms before you may change the visit to Missed.')
                    else:
                        missed_2180 = infant_visit.recalculate_missed_meta(scheduled_meta_data, requisition_meta_data)
                        if not missed_2180:
                            raise exception_cls('Please delete all filled in forms before you may change the visit to Missed.')
                if infant_visit.reason == 'vital status':
                    if self.appointment.visit_definition.code != '2180':
                        raise exception_cls('Please delete all filled in forms before you may change the visit to Vital Status.')
                    else:
                        vital_status_2180 = infant_visit.recalculate_missed_meta(scheduled_meta_data, requisition_meta_data)
                        if not vital_status_2180:
                            raise exception_cls('Please delete all filled in forms before you may change the visit to Vital Status.')
                if infant_visit.reason == 'death':
                    death = infant_visit.recalculate_death_meta(scheduled_meta_data, requisition_meta_data)
                    if not death:
                        raise exception_cls('Please delete all filled in forms that are not Death forms before you may change the visit to Death.')

    class Meta:
        db_table = 'mpepu_infant_infantvisit'
        app_label = "mpepu_infant"
        verbose_name = "Infant Visit"
