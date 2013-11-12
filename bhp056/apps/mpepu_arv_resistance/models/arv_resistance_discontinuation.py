from django.db import models
from datetime import datetime

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO

from apps.mpepu_maternal.models import BaseScheduledVisitModel, MaternalVisit

from ..choices import ARV_REGIMEN, DRUG_TAKE, INFO_SOURCE


class ArvResistanceDiscontinuation(BaseScheduledVisitModel):
    regimen = models.CharField(
        choices=ARV_REGIMEN,
        verbose_name="What antiretroviral regimen was the mother taking when she stopped ARVs postpartum:",
        max_length=15,
        )
    
    date_arv_started = models.DateField(
        verbose_name="Date antiretrovirals (listed in 1 above)was started:",
        )
    
    discontinued_by = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Was HAART discontinued by health provider?",
        )
    
    stopped_once = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Were all antiretrovirals stopped at once (no tail)?",
        )
    
    last_arv_date = models.DateField(
        verbose_name="If Yes, what was the last date antiretrovirals were taken?",
        null=True,
        blank=True,
        )
    
    last_ftc_date = models.DateField(
        verbose_name="If No, what was the last date you took TDF/FTC?",
        null=True,
        blank=True,
        )
    
    last_tdf_date = models.DateField(
        verbose_name="What was the last date you took TDF?",
        null=True,
        blank=True,
        )
    
    last_3tc_date = models.DateField(
        verbose_name="What was the last date you took 3TC?",
        null=True,
        blank=True,
        )
    
    as_prescribed = models.CharField(
        verbose_name="On average, how would you rate your ability to take all your antiretrovirals as prescribed, before they were stopped?",
        choices=DRUG_TAKE,
        max_length=50,
        )
    
    info_source = models.CharField(
        verbose_name="What is the source of the information collected in #1,2 & 3 above?",
        choices=INFO_SOURCE,
        help_text='Tick all that applies',
        max_length=15,
        )
    
    history = AuditTrail()
    
    def save(self, *args, **kwargs):
        if self.maternal_visit.report_datetime:
            self.report_datetime = self.maternal_visit.report_datetime
        else: 
            self.report_datetime = datetime.today()
        super(ArvResistanceDiscontinuation, self).save(*args, **kwargs)
    
    class Meta:
        app_label = 'mpepu_arv_resistance'
        verbose_name = 'ARV Resistance Discontinuation'
        verbose_name_plural='ARV Resistance Discontinuation'
