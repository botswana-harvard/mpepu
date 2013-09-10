from bhp_consent.forms import BaseConsentedModelForm
from mpepu_infant.models import InfantVisit


class BaseInfantModelForm(BaseConsentedModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseInfantModelForm, self).__init__(*args, **kwargs)
        try:
            self.fields['infant_visit'].queryset = InfantVisit.objects.filter(pk=self.instance.infant_visit.pk)
        except:
            pass
