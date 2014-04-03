from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices import YES_NO

from edc.subject.haart.models import BaseHaartModification
from edc.subject.haart.choices import ARV_STATUS
from base_infant_registered_subject_model import BaseInfantRegisteredSubjectModel
from infant_off_study_mixin import InfantOffStudyMixin


class InfantHaart (BaseInfantRegisteredSubjectModel):

    """ mp016 """

    hiv_positive_date = models.DateField(
        verbose_name="Date infant tested HIV-positive",
        help_text="",
        )
    haart_initiated = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="Has patient been initiated on HAART? ",
        help_text="If no, fill out comment,and indicate the reason HAART has not yet been initiated,otherwise answer question 4",
        )
    haart_date = models.DateField(
        verbose_name="Date of HAART initiation ",
        help_text="",
        blank=True,
        null=True,
        )
    arv_status = models.CharField(
        max_length=15,
        choices=ARV_STATUS,
        verbose_name="What is the status of the participant's antiretroviral treatment / prophylaxis at this visit or since the last visit?",
        help_text="",
        )
    comment = models.CharField(
        max_length=35,
        verbose_name="Comments",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % (self.registered_subject)

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.registered_subject.relative_identifier

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infanthaart_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = 'Infant HAART'


class InfantHaartMod(InfantOffStudyMixin, BaseHaartModification):

    infant_haart = models.ForeignKey(InfantHaart)

    history = AuditTrail()

    def get_report_datetime(self):
        return self.infant_haart.get_report_datetime()

    def get_subject_identifier(self):
        return self.infant_haart.get_subject_identifier()

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.infant_haart.get_consenting_subject_identifier()

    def get_visit(self):
        return self.infant_haart.infant_visit

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = 'Infant HAART: Mods'
