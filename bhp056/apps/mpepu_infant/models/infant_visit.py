from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

from edc.audit.audit_trail import AuditTrail
from edc.subject.visit_tracking.models.base_visit_tracking import BaseVisitTracking
from edc.subject.visit_tracking.settings import VISIT_REASON_NO_FOLLOW_UP_CHOICES

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
        return dct

    @property
    def registered_subject(self):
        return self.get_registered_subject()

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantvisit_change', args=(self.id,))

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.appointment.registered_subject.relative_identifier

    def requires_infant_eligibility(self, exception_cls=None):
        """Requires InfantEligibility to be completed for any visit after 2000 or InfantPreEligibility for 2015 ."""
        if not exception_cls:
            exception_cls = ValidationError
        # must have InfantEligibility or InfantPreEligibility
        InfantEligibility = models.get_model('mpepu_infant', 'InfantEligibility')
        has_infant_eligibility = InfantEligibility.objects.filter(registered_subject=self.appointment.registered_subject).exists()
        InfantPreEligibility = models.get_model('mpepu_infant', 'InfantPreEligibility')
        has_infant_pre_eligibility = InfantPreEligibility.objects.filter(registered_subject=self.appointment.registered_subject).exists()
        if not has_infant_eligibility and not has_infant_pre_eligibility:
            if self.appointment.visit_definition.code != '2000' and self.reason in ['scheduled', 'unscheduled']:
                raise exception_cls('Please complete the Infant Eligibility or Infant Pre-eligibility before conducting scheduled visits beyond visit 2000.')
        if not has_infant_eligibility and has_infant_pre_eligibility:
            if self.appointment.visit_definition.code not in ['2000', '2010'] and self.reason in ['scheduled', 'unscheduled']:
                raise exception_cls('Please complete the Infant Eligibility or Infant Pre-eligibility before conducting scheduled visits beyond visit 2000.')

#     def check_previous_visit_keyed(self, infant_visit, exception_cls=None):
#         """Check that previous visit has been keyed before allowing saving of current visit"""
#         if not exception_cls:
#             exception_cls = ValidationError
#         e_codes = ['2000','2010','2020','2030','2060','2090','2120','2150','2180']
#         pre_codes = ['2000','2010','2015','2020','2030','2060','2090','2120','2150','2180']
#         InfantPreEligibility = models.get_model('mpepu_infant', 'InfantPreEligibility')
#         has_infant_pre_eligibility = InfantPreEligibility.objects.filter(registered_subject=self.appointment.registered_subject)
# 
#         if has_infant_pre_eligibility:
#             index = pre_codes.index(self.appointment.visit_definition.code)
#             prev_visit = InfantVisit.objects.filter(subject_identifier=self.registered_subject.subject_identifier, appointment__visit_definition__code=pre_codes.pop(index-1))
#         else:
#             index = e_codes.index(self.appointment.visit_definition.code)
#             prev_visit = InfantVisit.objects.filter(subject_identifier=self.registered_subject.subject_identifier, appointment__visit_definition__code=e_codes.pop(index-1))
# 
#         if not prev_visit and index != 0:
#             raise exception_cls('You cannot complete an Infant Visit, when previous visit has not been keyed. Please go back and key it in.')
#         return True

    def save(self, *args, **kwargs):
        if self.reason == 'deferred':
            if self.appointment.visit_definition.code != '2010':
                raise ValidationError('Reason option \'deferred\' may only be used for the 2010 visit')
        if self.reason == 'vital status':
            self.appointment.appt_type = 'telephone'
        self.requires_infant_eligibility()
        self.check_previous_visit_keyed()
        super(InfantVisit, self).save(*args, **kwargs)

    class Meta:
        db_table = 'mpepu_infant_infantvisit'
        app_label = "mpepu_infant"
        verbose_name = "Infant Visit"
