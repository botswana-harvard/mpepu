from django import forms
from .base_infant_model_form import BaseInfantModelForm
from apps.mpepu_infant.models import InfantStoolCollection


class InfantStoolCollectionForm(BaseInfantModelForm):

    def clean(self):
        cleaned_data = super(InfantStoolCollectionForm, self).clean()
        # validating no sample collection
        if cleaned_data.get('sample_obtained', None) == 'No' and cleaned_data.get('axi_temp', None):
            raise forms.ValidationError('If no sample is obtained, do not give temp')
        if cleaned_data.get('sample_obtained', None) == 'No' and cleaned_data.get('past_diarrhea', None) or cleaned_data.get('diarrhea_past_24hrs', None):
            raise forms.ValidationError('If no sample is obtained, do not give diarrhea info')
        if cleaned_data.get('sample_obtained', None) == 'No' and cleaned_data.get('antibiotics_7days', None) or cleaned_data.get('antibiotic_dose_24hrs', None):
            raise forms.ValidationError('If no sample is obtained, do not give antibiotic details')

        # validating collection of sample
        if cleaned_data.get('sample_obtained', None) == 'Yes' and not cleaned_data.get('axi_temp', None):
            raise forms.ValidationError('If you were able to collect stool sample, please give axillary temperature')
        if cleaned_data.get('sample_obtained', None) == 'Yes' and not cleaned_data.get('past_diarrhea', None):
            raise forms.ValidationError('If you were able to collect stool sample, please give info about any diarrhoea')

        #validating past diarrhea
        if cleaned_data.get('past_diarrhea', None) == 'Yes' and not cleaned_data.get('diarrhea_past_24hrs', None):
            raise forms.ValidationError('If the child had diarrhea for the past 7days, has the child\'s diarrhea continued in the past 24hours?')
        if cleaned_data.get('past_diarrhea', None) == 'Yes' and cleaned_data.get('diarrhea_past_24hrs', None) == 'N/A':
            raise forms.ValidationError('If the child had diarrhea for the past 7days, info about diarrhea in the past 24hours CANNOT be N/A')
        if cleaned_data.get('past_diarrhea', None) == 'No' and cleaned_data.get('diarrhea_past_24hrs', None) != 'N/A':
            raise forms.ValidationError('If the child did not have diarrhea for the past 7days, info about diarrhea in the past 24hours SHOULD BE N/A')

        #validation antibiotics
        if cleaned_data.get('antibiotics_7days', None) == 'Yes' and cleaned_data.get('antibiotic_dose_24hrs', None) == 'N/A':
            raise forms.ValidationError('If the child took antibiotics in the past 7days, info about antibiotics in the past 24hours CANNOT be N/A')
        if cleaned_data.get('antibiotics_7days', None) == 'No' and cleaned_data.get('antibiotic_dose_24hrs', None) != 'N/A':
            raise forms.ValidationError('If the child took antibiotics in the past 7days, info about antibiotics in the past 24hours MUST BE N/A')

        return cleaned_data

    class Meta:
        model = InfantStoolCollection
