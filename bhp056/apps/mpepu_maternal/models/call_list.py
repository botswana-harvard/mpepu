from dateutil.relativedelta import relativedelta

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from edc.audit.audit_trail import AuditTrail
from edc.base.model.validators import BWCellNumber
from edc.base.model.validators import datetime_not_future, datetime_not_before_study_start
from edc.choices.common import GENDER
from edc.constants import CLOSED, OPEN, NEW
from edc.core.crypto_fields.fields import EncryptedCharField
from edc.core.crypto_fields.fields import EncryptedFirstnameField
from edc.device.sync.models import BaseSyncUuidModel

from ..managers import CallListManager

from .maternal_consent import MaternalConsent


class CallList (BaseSyncUuidModel):

    consent = models.ForeignKey(MaternalConsent)

    site = models.CharField(
        max_length=50)

    subject_identifier = models.CharField(
        max_length=25)

    call_datetime = models.DateTimeField(
        null=True,
        editable=False,
        help_text='last call datetime updated by call log entry',
    )

    app_label = models.CharField(
        max_length=25,
        editable=False
    )

    object_name = models.CharField(
        max_length=25,
        editable=False
    )

    object_pk = models.CharField(
        max_length=50,
        editable=False
    )

    first_name = EncryptedFirstnameField(
        verbose_name='First name',
        editable=False,
    )

    initials = models.CharField(
        verbose_name='Initials',
        max_length=3,
        editable=False,
    )

    gender = models.CharField(
        verbose_name='Gender',
        max_length=1,
        choices=GENDER,
        editable=False,
    )

    age_in_years = models.IntegerField(
        verbose_name=_('Age in years'),
        null=True,
        editable=False,
    )

    consent_datetime = models.DateTimeField(
        verbose_name="Consent date and time",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        help_text=_("From Subject Consent.")
    )

    referral_appt_date = models.DateTimeField(
        verbose_name="Referral date and time",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        null=True,
        help_text=_("From Subject Consent.")
    )

    call_attempts = models.IntegerField(
        default=0
    )

    call_outcome = models.TextField(
        max_length=150,
        null=True,
    )

    call_status = models.CharField(
        max_length=15,
        choices=(
            (NEW, 'New'),
            (OPEN, 'Open'),
            (CLOSED, 'Closed'),
        ),
        default=NEW,
    )

    cell = EncryptedCharField(
        max_length=8,
        verbose_name=_("Cell number"),
        validators=[BWCellNumber, ],
        blank=True,
        null=True,
        help_text="",
    )

    alt_cell = EncryptedCharField(
        max_length=8,
        verbose_name=_("Cell number"),
        validators=[BWCellNumber, ],
        blank=True,
        null=True,
        help_text="",
    )

    label = models.CharField(
        max_length=25,
        null=True,
        help_text="label to group reasons for contact, e.g. T1 preparation"
    )

    contacted = models.BooleanField(default=False)

    history = AuditTrail()

    objects = CallListManager()

    def __unicode__(self):
        return '{} {} {} ({} call)'.format(
            self.subject_identifier,
            self.consent.first_name,
            self.consent.initials,
            self.label,
        )

    def age(self):
        return relativedelta(self.consent_datetime.date(), self.dob).years
    age.allow_tags = True

    class Meta:
        app_label = 'mpepu_maternal'
        unique_together = ['consent', 'label']
