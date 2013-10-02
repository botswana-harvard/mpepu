from django.db import models
from django.core.urlresolvers import reverse
from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO
from bhp_base_model.validators import date_not_future
from apps.mpepu.choices import INFANT_DRUG_INITIATION
from .base_scheduled_visit_model import BaseScheduledVisitModel


class InfantStudyDrugInit(BaseScheduledVisitModel):

    """ CTX / Placebo """

    initiated = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="1. Did the participant start CTX or placebo study drug? ",
        help_text="If 'No' skip to question 3",
        )

    first_dose_date = models.DateField(
        verbose_name="2. Date of first known dose",
        blank=True,
        null=True,
        help_text="",
        validators=[
            date_not_future, ],
        )

    reason_not_init = models.CharField(
        verbose_name="3. Reason for not starting CTX or placebo Study Drug?",
        max_length=25,
        choices=INFANT_DRUG_INITIATION,
        help_text="If contra-indicated please complete Off Study Form (AF004)",
        default='N/A',
        )

    reason_not_survive = models.CharField(
        verbose_name='If "Survival to 18 months unlikely", describe',
        max_length=250,
        blank=True,
        null=True,
        )
    reason_not_init_other = models.CharField(
        verbose_name='If "Other", specify',
        max_length=250,
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % (self.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantstudydruginit_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Study Drug Initiation"
