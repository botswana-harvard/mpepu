from django import forms

from edc.subject.consent.forms import BaseSubjectConsentForm, BaseConsentUpdateForm

from ..models import MaternalConsent, MaternalConsentUpdate


class MaternalConsentForm (BaseSubjectConsentForm):
    def clean(self):
        raise forms.ValidationError('Enrollment for this study has ceased.You cannot consent an individual for this study.')

    class Meta:
        model = MaternalConsent


class MaternalConsentUpdateForm (BaseConsentUpdateForm):

    def clean(self):
        return super(MaternalConsentUpdateForm, self).clean('maternal_consent', self.cleaned_data.get('maternal_consent', None))

    class Meta:
        model = MaternalConsentUpdate
