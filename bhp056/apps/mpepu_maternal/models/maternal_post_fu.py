from django.db import models
from django.core.urlresolvers import reverse
from edc.base.model.fields.custom.custom_fields import OtherCharField
from edc.choices.common import YES_NO
from edc.audit.audit_trail import AuditTrail
from mpepu_list.models.maternal_post_fu import ChronicCond
from mpepu_maternal.models import BaseScheduledVisitModel


class MaternalPostFu(BaseScheduledVisitModel):

    """ General post-partum follow-up. """

    mother_weight = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="1. Was the mother's weight measured at this visit?",
        help_text="(If Yes,complete 2a.If No,go to question 3)",
        )
    enter_weight = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        verbose_name="1a.Enter mother's weight  ",
        help_text="kg",
        blank=True,
        null=True,
        )
    breastfeeding = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="2. Has the mother breastfed since the last attended visit? ",
        help_text="(If no,skip to question 4)",
        )
    had_mastitis = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="2a. If yes,since the last attended scheduled visit,has the mother had mastitis at any time? ",
        help_text="",
        blank=True,
        null=True,
        )

    has_chronic_cond = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="4.Since the last attended scheduled visit, has the mother had any of the following chronic health conditions, which were NEW diagnoses (never previously reported)?",
        help_text="",
        )

    chronic_cond = models.ManyToManyField(ChronicCond,
        verbose_name="Tick all that apply",
        help_text="",
        )
    chronic_cond_other = OtherCharField()

    started_ctx = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="7.Since the last attended scheduled visit, has the mother started CTX? ",
        help_text="",
        )

    comment = models.CharField(
        max_length=350,
        verbose_name="8.Comment if any additional pertinent information: ",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Postnatal Follow-Up"
