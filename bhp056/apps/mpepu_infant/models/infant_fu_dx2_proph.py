from django.db import models
from django.core.urlresolvers import reverse
from audit_trail.audit import AuditTrail
from bhp_code_lists.models import WcsDxPed
from bhp_common.choices import YES_NO
from mpepu_infant.models import BaseScheduledVisitModel
from infant_fu import InfantFu


class InfantFuDx2Proph(BaseScheduledVisitModel):

    infant_fu = models.ForeignKey(InfantFu)

    has_dx = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="4.Since the last attended scheduled visit, did one of the new diagnoses listed below occur",
        help_text="please indicate relationship of this diagnoses to the study CTX/placebo and to infant NVP prophylaxis in the table below",
        )
    who_diagnosis = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="5. Since the last attended scheduled visit,has the infant ever had any of the diagnoses in the WHO pediatric HIV clinical staging document which were NEW(never previously reported,or a NEW episode of a previously resolved* diagnosis),and which are not reported above?",
        help_text="if this is the randomization visit,include the time period from birth through the randomization visit",
        )
    wcs_dx_ped = models.ManyToManyField(WcsDxPed,
        verbose_name="5a. List any new WHO Stage III/IV diagnoses that are not reported in Question 6 above:  ",
        )

    history = AuditTrail()

    def __unicode__(self):
        return unicode(self.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantfudx2proph_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant FollowUp: Dx to Proph"
        verbose_name_plural = "Infant FollowUp: Dx to Proph"
