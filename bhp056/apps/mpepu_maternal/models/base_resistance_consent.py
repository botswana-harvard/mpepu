from edc.subject.consent.models import BaseConsent
from edc.subject.consent.mixins.bw import IdentityFieldsMixin
from edc.subject.consent.mixins import ReviewAndUnderstandingFieldsMixin

from .maternal_off_study_mixin import MaternalOffStudyMixin
from edc.subject.appointment_helper.models import BaseAppointmentMixin


class BaseResistanceConsent(BaseAppointmentMixin, MaternalOffStudyMixin, BaseConsent):

    """Model for resistance consent and registration model for mothers."""

    def get_subject_type(self):
        return 'maternal'

    def get_subject_identifier(self):
        return self.subject_identifier

    class Meta:
        abstract = True

# add Mixin fields to abstract class
for field in IdentityFieldsMixin._meta.fields:
    if field.name not in [fld.name for fld in BaseResistanceConsent._meta.fields]:
        field.contribute_to_class(BaseResistanceConsent, field.name)

for field in ReviewAndUnderstandingFieldsMixin._meta.fields:
    if field.name not in [fld.name for fld in BaseResistanceConsent._meta.fields]:
        field.contribute_to_class(BaseResistanceConsent, field.name)
