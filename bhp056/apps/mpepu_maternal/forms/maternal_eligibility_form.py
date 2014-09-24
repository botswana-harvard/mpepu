from django import forms

from edc.subject.consent.forms import BaseConsentedModelForm

from ..models import MaternalEligibilityPost, MaternalEligibilityAnte


class BaseMaternalEligibilityForm (BaseConsentedModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('registered_subject'):
            raise forms.ValidationError('This field is required. Please fill it in')

        if cleaned_data.get('is_cd4_low') < 250 and cleaned_data.get('feeding_choice') == 'Yes' and cleaned_data.get('maternal_haart') == 'No':
            raise forms.ValidationError('Please Stop. PARTICIPANT IS INELIGIBLE.CD4<250, intends to BF and does not intend to start HAART.')

        return super(BaseMaternalEligibilityForm, self).clean()


class MaternalEligibilityPostForm(BaseMaternalEligibilityForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        #Ensure that the post eligibility form is not filled in when the ante-natal eligibility has been filled in.
        self.instance.ante_natal_check(MaternalEligibilityPost(**cleaned_data), forms.ValidationError)
        return super(MaternalEligibilityPostForm, self).clean()

    class Meta:
        model = MaternalEligibilityPost


class MaternalEligibilityAnteForm(BaseMaternalEligibilityForm):
    def clean(self):
        return super(MaternalEligibilityAnteForm, self).clean()

    class Meta:
        model = MaternalEligibilityAnte
