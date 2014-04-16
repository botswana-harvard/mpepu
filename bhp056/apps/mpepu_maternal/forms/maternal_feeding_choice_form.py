from django import forms

from .base_maternal_model_form import BaseMaternalModelForm
from ..models import FeedingChoice, FeedingChoiceSectionOne, FeedingChoiceSectionTwo, FeedingChoiceSectionThree


class FeedingChoiceForm (BaseMaternalModelForm):

    class Meta:
        model = FeedingChoice


class FeedingChoiceSectionOneForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = super(FeedingChoiceSectionOneForm, self).clean()

        return cleaned_data

    class Meta:
        model = FeedingChoiceSectionOne


class FeedingChoiceSectionTwoForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data

        if cleaned_data.get('work_influence') == 'Yes' and cleaned_data.get('work_return') == 'NA':
            raise forms.ValidationError("You indicated that participants feeding choice will be influenced by work. You CANNOT indicate 'Not Applicable' for when the participant plans to return to work.")

        if cleaned_data.get('work_influence') == 'No' and cleaned_data.get('work_return') != 'NA':
            raise forms.ValidationError("You indicated that participants feeding choice will NOT be influenced by work. You should indicate 'Not Applicable' for when the participant plans to return to work.")

        return super(FeedingChoiceSectionTwoForm, self).clean()

    class Meta:
        model = FeedingChoiceSectionTwo


class FeedingChoiceSectionThreeForm (BaseMaternalModelForm):

    class Meta:
        model = FeedingChoiceSectionThree
