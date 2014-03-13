from django import forms

from apps.mpepu_infant.models import InfantEligibility

from .base_maternal_model_form import BaseMaternalModelForm
from ..models import PostNatalInfantFeedingSurvey
from ..models import FeedingChoiceSectionThree


class PostNatalInfantFeedingSurveyForm (BaseMaternalModelForm):
    
    def check_feeeding(self):
        print self.__dict__

    def clean(self):

        cleaned_data = super(PostNatalInfantFeedingSurveyForm, self).clean()  
      
        #validate feeding duration
        if cleaned_data.get('feeding_period') == 'Yes' and cleaned_data.get('feeding_duration'):
            raise forms.ValidationError("Breast feeding duration should be 'None' if participant was satisfied with breastfeeding duration. Please correct.")
        if cleaned_data.get('feeding_period') == 'No' and not cleaned_data.get('feeding_duration'):
            raise forms.ValidationError("Breast feeding duration CANNOT be 'None' if participant was dissatisfied with breastfeeding duration. Please correct.")
        if cleaned_data.get('feeding_period') == 'N/A' and cleaned_data.get('feeding_duration'):
            raise forms.ValidationError("Breast feeding duration must be 'None' as participant formula fed. Please correct.")
            
#         if cleaned_data.get('next_feeding_choice', None) == 'Exclusive FF' and cleaned_data.get('feeding_period', None) != 'N/A':
#             raise forms.ValidationError('Feeding period (3) must be \'not applicable\' if mother is exclusively formula feeding (2)')
#         if cleaned_data.get('next_feeding_choice', None) != 'Exclusive FF' and cleaned_data.get('feeding_period', None) == 'N/A':
#             raise forms.ValidationError('Feeding period (3) must not be \'not applicable\' if mother is exclusively breastfeeding (2)')

        return cleaned_data

    class Meta:
        model = PostNatalInfantFeedingSurvey
