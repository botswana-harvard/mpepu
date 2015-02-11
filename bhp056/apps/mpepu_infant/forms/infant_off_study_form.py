from django import forms
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer

from edc.subject.off_study.forms import BaseOffStudyForm

from apps.mpepu_infant.choices import OFF_STUDY_REASON
from apps.mpepu_infant.models import InfantOffStudy, InfantOffDrug
from apps.mpepu_infant_rando.models import InfantRando


class InfantOffStudyForm (BaseOffStudyForm):

    reason = forms.ChoiceField(
        label='Please code the primary reason participant taken off-study',
        choices=[choice for choice in OFF_STUDY_REASON],
        help_text="",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer),
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('registered_subject'):
            raise forms.ValidationError('This field is required. Please fill it in')

        if not cleaned_data.get('offstudy_date'):
            raise forms.ValidationError('This field is required. Please fill it in')

        #If Infant Drug has not been discontinued and infant is randomised, raise error
        infant_rando = InfantRando.objects.filter(subject_identifier=cleaned_data.get('registered_subject').subject_identifier)
        infant_off_drug = InfantOffDrug.objects.filter(registered_subject=cleaned_data.get('registered_subject'))
        if not infant_off_drug and infant_rando:
            raise forms.ValidationError('Please key in InfantOffDrug before keying in the Off-study form.')

        return super(InfantOffStudyForm, self).clean()

    class Meta:
        model = InfantOffStudy
