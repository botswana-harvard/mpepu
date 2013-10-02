from django.db import models

from edc.subject.consent.models import BaseConsentUpdate

from .maternal_consent import MaternalConsent
from .maternal_off_study_mixin import MaternalOffStudyMixin


class MaternalConsentUpdate(MaternalOffStudyMixin, BaseConsentUpdate):

    maternal_consent = models.ForeignKey(MaternalConsent, editable=False)

    def __unicode__(self):
        return unicode(self.maternal_consent)

    def save(self, *args, **kwargs):
        """After save, updates the most recent consent version on the "entry" consent."""
        super(MaternalConsentUpdate, self).save(*args, **kwargs)
        self.maternal_consent.consent_version_recent = self.consent_version
        self.maternal_consent.save()

    def get_consent_field_attr_name(self):
        return 'maternal_consent'

    def get_subject_identifier(self):
        return self.maternal_consent.subject_identifier

    class Meta:
        app_label = 'mpepu_maternal'
        unique_together = (('maternal_consent', 'consent_version'), ('maternal_consent', 'consent_datetime'))
