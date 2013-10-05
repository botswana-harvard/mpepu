from django import forms
from apps.mpepu_infant.models import InfantRandoDeferral
from .base_infant_model_form import BaseInfantModelForm


class InfantRandoDeferralForm (BaseInfantModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        self._meta.model(**cleaned_data).requires_appointment_2010(forms.ValidationError)
        weight = cleaned_data.get('weight')
        clinical_jaundice = cleaned_data.get('clinical_jaundice')
        anemia_neutropenia = cleaned_data.get('anemia_neutropenia')
        if weight >= 2.5 and clinical_jaundice == 'No' and anemia_neutropenia == 'No':
            raise forms.ValidationError('Either weight must be less than 2.5 or the infant have clinical jaundice, anemia or neutropenia')
        return super(InfantRandoDeferralForm, self).clean()

    class Meta:
        model = InfantRandoDeferral
