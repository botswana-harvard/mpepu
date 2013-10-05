from django.db import models
from django.core.urlresolvers import reverse
from edc.choices.common import YES_NO
from edc.subject.code_lists.models import WcsDxAdult
from edc.audit.audit_trail import AuditTrail
from .base_scheduled_visit_model import BaseScheduledVisitModel
from maternal_post_fu import MaternalPostFu


class MaternalPostFuDx(BaseScheduledVisitModel):

    """ Post-partum follow up of diagnosis. """

    maternal_post_fu = models.OneToOneField(MaternalPostFu)

    mother_hospitalized = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="3.Has the mother been hospitalized overnight since the last scheduled visit (or since discharge after delivery, if this is the randomization visit)?",
        help_text="if yes, the primary diagnosis associated with the hospitalization(s) must be recorded in Postnatal diagnosis section",
        )

    new_diagnoses = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="5.Since the last attended scheduled visit, has the mother had any of the following which were NEW (never previously reported, or a NEW episode of a previously resolved* diagnosis)",
        help_text="if yes, tick all that apply, only report grade 3 0r 4 diagnoses",
        )
    who_clinical_stage = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="6.Since the last attended scheduled visit, has the mother ever had any of the diagnoses listed in the WHO Adult/Adolescent HIV clinical staging document which are NEW?",
        help_text="never previously reported, or a NEW episode of a previously resolved diagnosis, and which is NOT reported above in Question 6",
        )
    wcs_dx_adult = models.ManyToManyField(WcsDxAdult,
        verbose_name="6a. List any new WHO Stage III/IV diagnoses that are not reported in Question 6 above:  ",
        )

    history = AuditTrail()

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalpostfudx_change', args=(self.id,))

    def get_report_datetime(self):
        return self.maternal_post_fu.get_report_datetime()

    def get_subject_identifier(self):
        return self.maternal_post_fu.get_subject_identifier()

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Postnatal Follow-Up: Dx"
