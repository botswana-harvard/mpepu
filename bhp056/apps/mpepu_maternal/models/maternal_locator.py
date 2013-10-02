from django.db import models
from audit_trail.audit import AuditTrail
from bhp_locator.models import BaseLocator
from bhp_common.choices import YES_NO
from bhp_base_model.fields import OtherCharField
from bhp_base_model.validators import BWCellNumber, BWTelephoneNumber
from mpepu_maternal.models import MaternalVisit
from bhp_crypto.fields import EncryptedCharField
from maternal_off_study_mixin import MaternalOffStudyMixin


class MaternalLocator(MaternalOffStudyMixin, BaseLocator):

    maternal_visit = models.ForeignKey(MaternalVisit)

    care_clinic = OtherCharField(
        max_length=35,
        verbose_name="Health clinic where your infant will receive their routine care ",
        help_text="",
        )

    has_caretaker_alt = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="6.Has the participant identified someone who will be responsible for the care of the baby in case of her death, to whom the study team could share information about her baby's health?",
        help_text="",
        )

    caretaker_name = EncryptedCharField(
        max_length=35,
        verbose_name="6a. Full Name of the responsible person",
        help_text="include firstname and surname",
        blank=True,
        null=True,
        )

    caretaker_cell = EncryptedCharField(
        max_length=8,
        verbose_name="6b. Cell number",
        validators=[BWCellNumber, ],
        help_text="",
        blank=True,
        null=True,
        )

    caretaker_tel = EncryptedCharField(
        max_length=8,
        verbose_name="6c. Telephone number",
        validators=[BWTelephoneNumber, ],
        help_text="",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    def get_subject_identifier(self):
        return self.maternal_visit.appointment.registered_subject.subject_identifier

    def get_report_datetime(self):
        return self.maternal_visit.get_report_datetime()

    def save(self, *args, **kwargs):
        if not self.registered_subject:
            self.registered_subject = self.maternal_visit.appointment.registered_subject
        super(MaternalLocator, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % unicode(self.maternal_visit)

    class Meta:
        verbose_name = 'Maternal Locator'
        app_label = 'mpepu_maternal'
