from edc.subject.consent.forms import BaseConsentedModelForm
from mpepu_infant.models import InfantVitalStatus


class InfantVitalStatusForm(BaseConsentedModelForm):

    class Meta:
        model = InfantVitalStatus
