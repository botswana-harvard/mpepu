from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO, YES_NO_NA, YES_NO_UNKNOWN_NA

from .base_scheduled_visit_model import BaseScheduledVisitModel
from ..choices import STOOL_TEXTURE_DESC, ILLNESS_CLASSIFICATION, STOOLS_PAST_24HOURS, CONTINUOUS_LOOSE_STOOLS


class InfantStoolCollection(BaseScheduledVisitModel):

    """Infant stool collection. Processed in consent version 4.0 and at rando, 3, 6 and 18mnths"""

    sample_obtained = models.CharField(
        verbose_name="A stool sample/specimen can be obtained from the nappy of this child today ",
        choices=YES_NO,
        max_length=3,
        help_text=("If a stool samples/specimen cannot be obtained today, do not complete the"
                   " remainder of this form"),
        )
    stool_texture = models.CharField(
        verbose_name="If you were able to collect stool today, please describe the texture of the stool",
        max_length=45,
        null=True,
        blank=False,
        choices=STOOL_TEXTURE_DESC,
        help_text="",
        )
    axi_temp = models.DecimalField(
        verbose_name="Record the child's axillary temperature",
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=False,
        help_text="",
        )
    past_illness = models.CharField(
        verbose_name="Has this infant/child been ill in the last 7 days?",
        choices=YES_NO,
        max_length=3,
        null=True,
        blank=False,
        help_text="",
        )
    currently_ill = models.CharField(
        verbose_name="If this infant/child has been ill in the last 7 days, is the child currently ill?",
        max_length=15,
        choices=YES_NO_NA,
        null=True,
        blank=False,
        help_text="",
        )
    illness_classification = models.CharField(
        verbose_name="If this infant/child has been ill in the last 7 days, please classify the illness",
        max_length=75,
        choices=ILLNESS_CLASSIFICATION,
        null=True,
        blank=False,
        help_text="",
        )
    stools_past_24hrs = models.CharField(
        verbose_name=("If the answer to question 6 was 'Gastrointestinal illness' and the child"
                      " currently has diarrhea, approximately how many stools has the child had in"
                      " the past 24 hours"),
        max_length=15,
        choices=STOOLS_PAST_24HOURS,
        null=True,
        blank=False,
        help_text="",
        )
    diarrhoea_bloody = models.CharField(
        verbose_name="If this child currently has diarrhea, is it bloody?",
        max_length=15,
        choices=YES_NO_UNKNOWN_NA,
        null=True,
        blank=False,
        help_text="",
        )
    continuous_loose_stools = models.CharField(
        verbose_name=("If this child currently has diarrhea, please have the mother/care giver"
                      " estimate the number of continuous days with three or more loose stools"
                      " per day that are different from the normal pattern of stool."),
        max_length=45,
        choices=CONTINUOUS_LOOSE_STOOLS,
        null=True,
        blank=False,
        help_text="",
        )

    history = AuditTrail()

    objects = models.Manager()

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Stool Collection"
        verbose_name_plural = "Infant Stool Collection"
