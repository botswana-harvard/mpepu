from django import forms

from .base_maternal_model_form import BaseMaternalModelForm
from ..models import FeedingChoice, FeedingChoiceSectionOne, FeedingChoiceSectionTwo, FeedingChoiceSectionThree


class FeedingChoiceForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('maternal_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')
        return super(FeedingChoiceForm, self).clean()

    class Meta:
        model = FeedingChoice


class FeedingChoiceSectionOneForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('maternal_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')

        return super(FeedingChoiceSectionOneForm, self).clean()

    class Meta:
        model = FeedingChoiceSectionOne


class FeedingChoiceSectionTwoForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('maternal_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')

        if cleaned_data.get('work_influence') == 'Yes' and cleaned_data.get('work_return') == 'NA':
            raise forms.ValidationError("You indicated that participants feeding choice will be influenced by work. You CANNOT indicate 'Not Applicable' for when the participant plans to return to work.")

        if cleaned_data.get('work_influence') == 'No' and cleaned_data.get('work_return') != 'NA':
            raise forms.ValidationError("You indicated that participants feeding choice will NOT be influenced by work. You should indicate 'Not Applicable' for when the participant plans to return to work.")

        return super(FeedingChoiceSectionTwoForm, self).clean()

    class Meta:
        model = FeedingChoiceSectionTwo


class FeedingChoiceSectionThreeForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('maternal_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')
        return super(FeedingChoiceSectionThreeForm, self).clean()

    class Meta:
        model = FeedingChoiceSectionThree
