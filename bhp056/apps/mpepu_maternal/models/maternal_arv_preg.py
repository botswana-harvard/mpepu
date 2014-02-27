from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO, YES_NO_UNKNOWN
from edc.subject.haart.models import BaseHaartHistory

from apps.mpepu.choices import ARV_INTERRUPTION_REASON

from ..managers import MaternalArvManager
from .base_scheduled_visit_model import BaseScheduledVisitModel
from .maternal_off_study_mixin import MaternalOffStudyMixin


class MaternalArvPreg (BaseScheduledVisitModel):

    """ Maternal arv for current pregnancy. """

    # if yes, complete MaternalArvPregHistory
    took_arv = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Did the mother receive any ARVs during this pregnancy?",
        help_text="(NOT including single -dose NVP in labour)",
        )

    sd_nvp = models.CharField(
        max_length=10,
        choices=YES_NO_UNKNOWN,
        verbose_name="Was single-dose NVP received by the mother during labour(or false labour)? ",
        help_text="",
        )

    # if yes, complete MaternalArvPostPart
    start_pp = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Did the mother START any antiretroviral drugs during the immediate postpartum period (before discharge from maternity)?",
        help_text="",
        )

    history = AuditTrail()

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalarvpreg_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = 'Maternal ARV In This Preg'


class MaternalArvPregHistory(BaseScheduledVisitModel):

    """ Maternal arv for current pregnancy (transactions). """

    maternal_arv_preg = models.ForeignKey(MaternalArvPreg)

    is_interrupt = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Was there an interruption in the ARVs received during pregnancy through delivery of >/=3days?",
        help_text="",
        )
    
    interrupt = models.CharField(
        verbose_name="Please give reason for interruption",
        choices=ARV_INTERRUPTION_REASON,
        max_length=50,
        help_text="",
        default='N/A',
        )
    
    interrupt_other = models.TextField(
        max_length=250,
        verbose_name="Other, specify ",
        blank=True,
        null=True,
        )

    comment = models.TextField(
        max_length=250,
        verbose_name="Comments on pregnancy regimens: ",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalarvpreghistory_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = 'Maternal ARV In This Preg: Pregnancy'


class MaternalArvPPHistory(BaseScheduledVisitModel):

    """ Maternal arv for post-partum (transactions). """

    maternal_arv_preg = models.ForeignKey(MaternalArvPreg)

    comment = models.CharField(
        max_length=35,
        verbose_name="8. Comments postpartum regimens: ",
        blank=True,
        null=True,
        )

    history = AuditTrail()      

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalarvpphistory_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = 'Maternal ARV In This Preg: PostPart'


class MaternalArv (MaternalOffStudyMixin, BaseHaartHistory):

    """ Maternal arv history (current and post-partum). """

    maternal_arv_preg_history = models.ForeignKey(MaternalArvPregHistory,
        null=True,
        blank=True,
        )

    maternal_arv_pp_history = models.ForeignKey(MaternalArvPPHistory,
        null=True,
        blank=True,
        )

    transaction_flag = models.CharField(
        verbose_name="Transaction flag",
        max_length=15,
        null=True,
        blank=True,
        )

    history = AuditTrail()

    objects = MaternalArvManager()

    def natural_key(self):
        return super(MaternalArv, self).natural_key() + self.maternal_arv_preg_history.natural_key()

    def get_report_datetime(self):
        return self.maternal_arv_pp_history.report_datetime

    def get_subject_identifier(self):
        return self.maternal_arv_pp_history.get_subject_identifier()

    def get_visit(self):
        return self.maternal_arv_pp_history.maternal_visit

    def __unicode__(self):
        return unicode(self.get_visit())

    def save(self, *args, **kwargs):

        if self.maternal_arv_pp_history:
            self.transaction_flag = 'POSTPARTUM'
        elif self.maternal_arv_preg_history:
            self.transaction_flag = 'PREGNANCY'
        else:
            raise TypeError('cannot determine transaction_flag')
        super(MaternalArv, self).save(*args, **kwargs)

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = 'Maternal ARV'
