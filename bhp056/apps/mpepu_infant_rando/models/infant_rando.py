from django.db import models
from edc.audit.audit_trail import AuditTrail
from edc.base.model.fields.custom.custom_fields import InitialsField
from bhp_sync.models import BaseSyncUuidModel
from edc.choices.common import YES_NO
from edc.core.crypto_fields.fields import RestrictedRsaEncryptionField
from mpepu_infant_rando.managers import InfantRandoManager
from mpepu_infant_rando.choices import FEEDING_CHOICES, BF_DURATION


class InfantRando (BaseSyncUuidModel):
    """ Stores a prepared infant randomization list.

    If you need to undo a randomization, here is an example of how::
        >>> # To undo a randomization
        >>> subject_identifier = '056-1980294-0-10'
        >>> void_sid = '222222'
        >>> # clear rando record but set to void to not allow it to be used
        >>> infant_rando = InfantRando.objects.get(subject_identifier=subject_identifier, sid=void_sid)
        >>> if infant_rando:
        >>>     infant_rando.subject_identifier='void'
        >>>     infant_rando.randomization_datetime = None
        >>>     infant_rando.initials = 'XX'
        >>>     infant_rando.feeding_choice=None
        >>>     infant_rando.infant_initials='XX'
        >>>     infant_rando.haart_status=None
        >>>     infant_rando.comment = "used in error by %s" % (subject_identifier,)
        >>>     infant_rando.save()
        >>>     print "OK, SID %s is now void" % (void_sid,)
        >>>     # clear SID from registered subject
        >>>     rs = RegisteredSubject.object.get(subject_identifier=subject_identifier, sid=void_sid)
        >>>     rs.sid = None
        >>>     rs.registration_status = None
        >>>     print "OK, RegisteredSubject SID set to None"
        >>> else:
        >>>     print "Error"
"""
    site = models.CharField(
        verbose_name='Site',
        max_length=15)
    stratum = models.CharField(
        verbose_name='Stratum',
        max_length=15)
    sid = models.CharField(
        verbose_name='SID',
        max_length=15,
        unique=True)
    rx = RestrictedRsaEncryptionField(
        verbose_name="Treatment Assignment")
    bf_duration = models.CharField(
        verbose_name="BF Duration (m)",
        choices=BF_DURATION,
        max_length=15,
        null=True,
        blank=True)
    feeding_choice = models.CharField(
        verbose_name="Feeding Choice",
        choices=FEEDING_CHOICES,
        max_length=2,
        null=True,
        blank=True)
    haart_status = models.CharField(
        verbose_name="Maternal HAART Status",
        max_length=10,
        null=True,
        blank=True)
    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=16,
        null=True,
        blank=True)
    randomization_datetime = models.DateTimeField(
        verbose_name='Randomization Datetime',
        null=True,
        blank=True)
    infant_initials = InitialsField()

    dispensed = models.CharField(
        verbose_name='Dispensed',
        max_length=10,
        choices=YES_NO,
        help_text='To be confirmed by pharmacy staff only')
    comment = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        help_text="Comment if any manual changes made to rando list")
    objects = InfantRandoManager()
    history = AuditTrail()

    def __unicode__(self):
        return '%s infant %s' % (self.sid, self.subject_identifier)

    class Meta:
        app_label = "mpepu_infant_rando"
        db_table = 'mpepu_infant_infantrando'
        ordering = ['sid', ]
