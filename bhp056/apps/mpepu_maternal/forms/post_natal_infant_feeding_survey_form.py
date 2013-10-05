from django import forms

from .base_maternal_model_form import BaseMaternalModelForm
from ..models import PostNatalInfantFeedingSurvey


class PostNatalInfantFeedingSurveyForm (BaseMaternalModelForm):

    def clean(self):

        cleaned_data = self.cleaned_data

        if cleaned_data.get('next_feeding_choice', None) == 'Exclusive FF' and cleaned_data.get('feeding_period', None) != 'N/A':
            raise forms.ValidationError('Feeding period (3) must be \'not applicable\' if mother is exclusively formula feeding (2)')
        if cleaned_data.get('next_feeding_choice', None) != 'Exclusive FF' and cleaned_data.get('feeding_period', None) == 'N/A':
            raise forms.ValidationError('Feeding period (3) must not be \'not applicable\' if mother is exclusively breastfeeding (2)')

        return cleaned_data

    class Meta:
        model = PostNatalInfantFeedingSurvey
