from django.db import models
from audit_trail.audit import AuditTrail
from django.core.urlresolvers import reverse
from bhp_common.choices import YES_NO
from bhp_haart.choices import ARV_STATUS_WITH_NEVER
from bhp_haart.models import BaseHaartModification
from mpepu.choices import REASON_FOR_HAART
from mpepu_maternal.models import BaseScheduledVisitModel
from mpepu_maternal.managers import MaternalArvPostModManager
from maternal_off_study_mixin import MaternalOffStudyMixin


class MaternalArvPost (BaseScheduledVisitModel):

    """ Maternal ARV post-partum (mp007). """

    haart_last_visit = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="1. Was the mother supposed to be on HAART any time since the last attended scheduled visit?",
        help_text="If 'NO' End. Otherwise continue go to section one",
        )
    haart_reason = models.CharField(
        verbose_name="2. Reason for HAART ",
        max_length=25,
        choices=REASON_FOR_HAART,
        default='N/A',
        help_text="",
        )
    haart_reason_other = models.TextField(
        max_length=35,
        verbose_name="2a. if other, specify",
        blank=True,
        null=True,
        )
    arv_status = models.CharField(
        verbose_name="3.What is the status of the participant's antiretroviral treatment / prophylaxis at this visit or since the last visit? ",
        max_length=25,
        choices=ARV_STATUS_WITH_NEVER,
        help_text="",
        default='N/A',
        )

    history = AuditTrail()

    def visit(self):
        return self.maternal_visit

    def __unicode__(self):
        return "%s" % (self.maternal_visit)

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal ARVs Post"


class MaternalArvPostMod(MaternalOffStudyMixin, BaseHaartModification):

    """ Maternal ARV modifications post-partum.

    if art_status never, no_mod or N/A then this is not required"""

    maternal_arv_post = models.ForeignKey(MaternalArvPost)

    history = AuditTrail()

    objects = MaternalArvPostModManager()

    def get_visit(self):
        return self.maternal_arv_post.maternal_visit

    def __unicode__(self):
        return "%s" % (self.maternal_arv_post)

    def get_report_datetime(self):
        return self.maternal_arv_post.get_report_datetime()

    def get_subject_identifier(self):
        return self.maternal_arv_post.get_subject_identifier()

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalarvpostmod_change', args=(self.id,))

    def natural_key(self):
        return super(MaternalArvPostMod, self).natural_key() + self.maternal_arv_post.natural_key()

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = 'Maternal ARVs Post: Mods'
        unique_together = ('maternal_arv_post', 'arv_code', 'modification_date')


class MaternalArvPostAdh(BaseScheduledVisitModel):

    """Maternal ARV adherence post-partum.

    complete if YES for  haart_last_visit in MaternalArvPost """

    maternal_arv_post = models.OneToOneField(MaternalArvPost)

    missed_doses = models.IntegerField(
        verbose_name="4. Since the last attended last scheduled visit, how many doses of HAART were missed? ",
        help_text="",
        )
    missed_days = models.IntegerField(
        verbose_name="5. Since the last attended scheduled visit, how many entire days was HAART not taken?  ",
        help_text="",
        default='0',
        )
    missed_days_discnt = models.IntegerField(
        verbose_name="6. If HAART discontinued by health provider, how many days was HAART missed prior to HAART discontinuation?  ",
        help_text="",
        default='0',
        )
    comment = models.TextField(
        max_length=250,
        verbose_name="7. Comment",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % (self.maternal_arv_post)

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalarvspostadherence_change', args=(self.id,))

    def get_report_datetime(self):
        return self.maternal_arv_post.get_report_datetime()

    def get_subject_identifier(self):
        return self.maternal_arv_post.get_subject_identifier()

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal ARVs Post: Adherence"
