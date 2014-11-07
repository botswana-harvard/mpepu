from django import forms

from .base_maternal_model_form import BaseMaternalModelForm
from ..models import (FeedingChoice, FeedingChoiceSectionOne, FeedingChoiceSectionTwo, 
    FeedingChoiceSectionThree, MaternalEnroll )


class FeedingChoiceForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('maternal_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')

        #Cannot change first_time_feeding to Yes if FeedingChoiceSectionOne has been filled in.
        if cleaned_data.get('first_time_feeding') == 'Yes':
            if FeedingChoiceSectionOne.objects.filter(maternal_visit__subject_identifier=cleaned_data.get('maternal_visit').subject_identifier).exists():
                raise forms.ValidationError('Please delete form "FeedingChoiceSectionOne" before you can change'
                    ' question  "This pregnancy represents the first time I have had to make an infant feeding choice" to Yes.')

        #validate against maternal enrollment
        maternal_enroll = MaternalEnroll.objects.filter(maternal_visit__subject_identifier=cleaned_data.get('maternal_visit').subject_identifier)
        if maternal_enroll:
            if maternal_enroll[0].prev_pregnancies > 0 and cleaned_data.get('first_time_feeding') =='Yes':
                raise forms.ValidationError('You have indicated that participant had {} previous pregnancies in'
                   '"MaternalEnrollment" yet answered that this is the first time a feeding choice is being made.'
                   ' Please correct'.format(maternal_enroll[0].prev_pregnancies))
            if maternal_enroll[0].prev_pregnancies == 0 and cleaned_data.get('first_time_feeding') =='No':
                raise forms.ValidationError('You have indicated that participant had {} previous pregnancies in'
                   '"MaternalEnrollment" yet answered that this is NOT the first time a feeding choice is being made.'
                   ' Please correct'.format(maternal_enroll[0].prev_pregnancies))
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
            raise forms.ValidationError("You indicated that participants feeding choice will be influenced by work. "
                "You CANNOT indicate 'Not Applicable' for when the participant plans to return to work.")

        if cleaned_data.get('work_influence') == 'No' and cleaned_data.get('work_return') != 'NA':
            raise forms.ValidationError("You indicated that participants feeding choice will NOT be influenced by work."
                " You should indicate 'Not Applicable' for when the participant plans to return to work.")

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
