from django import forms
from .base_infant_model_form import BaseInfantModelForm
from apps.mpepu_infant.models import InfantStoolCollection


class InfantStoolCollectionForm(BaseInfantModelForm):

    def clean(self):
        cleaned_data = super(InfantStoolCollectionForm, self).clean()
        # validating collection of sample
        if cleaned_data.get('sample_obtained', None) == 'Yes' and not cleaned_data.get('stool_texture', None):
            raise forms.ValidationError('If you were able to collect stool sample, please describe the texture')
        if cleaned_data.get('sample_obtained', None) == 'Yes' and not cleaned_data.get('axi_temp', None):
            raise forms.ValidationError('If you were able to collect stool sample, please give auxillary temperature')
        if cleaned_data.get('sample_obtained', None) == 'Yes' and not cleaned_data.get('past_illness', None):
            raise forms.ValidationError('If you were able to collect stool sample, has the child been ill in the past days?')
        #validating past illness
        if cleaned_data.get('past_illness', None) == 'Yes' and not cleaned_data.get('currently_ill', None):
            raise forms.ValidationError('If the child has been ill for the past 7days, is the child currently ill?')
        if cleaned_data.get('past_illness', None) == 'Yes' and not cleaned_data.get('illness_classification', None):
            raise forms.ValidationError('If the child has been ill for the past 7days, please classify the illness')
        #validation gastro illness
        if cleaned_data.get('illness_classification', None) == 'gastro_illness' and not cleaned_data.get('stools_past_24hrs', None):
            raise forms.ValidationError('If the illness classified is gastro_illness, and child currently has diarrhoea, how many stools has the child passed in the last 24hours?')
        if cleaned_data.get('illness_classification', None) == 'gastro_illness' and not cleaned_data.get('diarrhoea_bloody', None):
            raise forms.ValidationError('If the illness classified is gastro_illness, and child currently has diarrhoea, is there blood in the diarrhoea?')
        if cleaned_data.get('illness_classification', None) == 'gastro_illness' and not cleaned_data.get('continuous_loose_stools', None):
            raise forms.ValidationError('If the illness classified is gastro_illness, and child currently has diarrhoea and it has been continuous, let the mother give an estimate of the number of loose stools passed per day')
        return cleaned_data

    class Meta:
        model = InfantStoolCollection
