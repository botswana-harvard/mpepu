from django import forms

from edc.subject.consent.forms import BaseConsentedModelForm

from ..models import MaternalEligibilityPost, MaternalEligibilityAnte


class BaseMaternalEligibilityForm (BaseConsentedModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        
        if cleaned_data.get('is_cd4_low')<250 and cleaned_data.get('feeding_choice')=='Yes' and cleaned_data.get('maternal_haart')=='No':
            raise forms.ValidationError('Please Stop. PARTICIPANT IS INELIGIBLE.CD4<250, intends to BF and does not intend to start HAART.')
            
        return super(BaseMaternalEligibilityForm, self).clean()


class MaternalEligibilityPostForm(BaseMaternalEligibilityForm):
    def clean(self):
        return super(MaternalEligibilityPostForm,self).clean()

    class Meta:
        model = MaternalEligibilityPost


class MaternalEligibilityAnteForm(BaseMaternalEligibilityForm):
    def clean(self):
        return super(MaternalEligibilityAnteForm, self).clean()

    class Meta:
        model = MaternalEligibilityAnte
