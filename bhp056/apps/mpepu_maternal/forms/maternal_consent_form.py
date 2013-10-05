from edc.subject.consent.forms import BaseSubjectConsentForm, BaseConsentUpdateForm

from ..models import MaternalConsent, MaternalConsentUpdate


class MaternalConsentForm (BaseSubjectConsentForm):

    class Meta:
        model = MaternalConsent


class MaternalConsentUpdateForm (BaseConsentUpdateForm):

    def clean(self):
        return super(MaternalConsentUpdateForm, self).clean('maternal_consent', self.cleaned_data.get('maternal_consent', None))

    class Meta:
        model = MaternalConsentUpdate
