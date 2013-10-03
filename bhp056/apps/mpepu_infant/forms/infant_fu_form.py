from django import forms
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer
from edc.subject.adverse_event.choices import GRADING_SCALE_234
from apps.mpepu_infant.models import (InfantFu, InfantFuDx, InfantFuPhysical, InfantFuDxItems, InfantFuD,
                                 InfantFuDx2Proph, InfantFuDx2ProphItems, InfantFuMed, InfantFuNewMed,
                                 InfantFuNewMedItems)
from .base_infant_model_form import BaseInfantModelForm


class InfantFuForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        # if infant had no diarrheal illness, InfantFuD is not required """
        if cleaned_data.get('diarrhea_illness').upper() == 'NO':
            if InfantFuD.objects.filter(infant_fu__infant_visit=cleaned_data.get('infant_visit')).exists():
                raise forms.ValidationError("Graded Infant Diarrhea data exists. You wrote infant had no "
                                            "diarrheal illness. Please correct '%s' first." % InfantFuD._meta.verbose_name)
        # if infant does not have DX, InfantFuDx is not required """
        if cleaned_data.get('has_dx').upper() == 'NO':
            if InfantFuDx.objects.filter(infant_fu__infant_visit=cleaned_data.get('infant_visit')):
                raise forms.ValidationError("Infant diagnosis have been reported for this visit. "
                                            "You wrote infant had no new events/episodes. Please "
                                            "correct '%s' first." % InfantFuDx._meta.verbose_name)
        return cleaned_data

    class Meta:
        model = InfantFu


class InfantFuPhysicalForm (BaseInfantModelForm):

    def clean(self):

        cleaned_data = super(InfantFuPhysicalForm, self).clean()

        # validating hospitalization
        if cleaned_data.get('was_hospitalized') == 'Yes' and not cleaned_data.get('days_hospitalized'):
            raise forms.ValidationError('If patient was hospitalised, give number of days in hospital')
        if cleaned_data.get('was_hospitalized') == 'No' and cleaned_data.get('days_hospitalized'):
            raise forms.ValidationError('Do not give number of hospital days if patient was never hospitalized.')
        return cleaned_data

    class Meta:
        model = InfantFuPhysical


class InfantFuDxForm (BaseInfantModelForm):

    class Meta:
        model = InfantFuDx


class InfantFuDxItemsForm (BaseInfantModelForm):

    grade = forms.ChoiceField(
        label='Grade',
        choices=[choice for choice in GRADING_SCALE_234],
        help_text="Grade of worst episode (3 or 4). Some DX reportable at Grade 2",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer))

    def clean(self):
        cleaned_data = self.cleaned_data
        if 'specify' in cleaned_data.get('fu_dx', None):
            if not cleaned_data.get('fu_dx_specify', None):
                raise forms.ValidationError('please specify \'%s\'' % (cleaned_data.get('fu_dx').replace('specify', ''),))
        if cleaned_data.get('fu_dx', None):
            # check for grade 2 dx codes
            grade_2_reportable_dx = ['Hepatitis:Drug related', 'Rash']
            if cleaned_data.get('fu_dx') not in grade_2_reportable_dx and cleaned_data.get('grade', None) == '2':
                raise forms.ValidationError('{dx} is not reportable at grade 2.'.format(dx=cleaned_data.get('fu_dx')))
        # validating for eae report
        if cleaned_data.get('is_eae_required') == 'Yes' and not cleaned_data.get('eae_reference'):
            raise forms.ValidationError('If eae report is available, give the eae reference number.')

        # if hospitalized, response about hospitalization in InfantPhysical and infantfudxitems should be same
        infant_fu_dx = cleaned_data.get('infant_fu_dx')
        visit = infant_fu_dx.infant_visit
        if InfantFuPhysical.objects.filter(infant_visit=visit).exists():
            infant_fu_physical = InfantFuPhysical.objects.get(infant_visit=visit)

            if infant_fu_physical.was_hospitalized != cleaned_data.get('was_hospitalized'):
                raise forms.ValidationError('Your response about hospitalization in InfantFuPhysical, and whether or not patient was hospitalized in this DX form are not the same. Please correct.')
        # validating that dx_onsetdate is not greater than the visit date
#         print visit
        if visit and cleaned_data.get('onset_date') > visit.report_datetime.date():
            raise forms.ValidationError("Onset date cannot be greater than the visit date. Please correct")

        return cleaned_data

    class Meta:
        model = InfantFuDxItems


class InfantFuDx2ProphForm (BaseInfantModelForm):
    def clean(self):

        cleaned_data = self.cleaned_data
        return cleaned_data

    class Meta:
        model = InfantFuDx2Proph


class InfantFuDx2ProphItemsForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        # relation of medication to study ctx/placebo and infant nvp
        if self.cleaned_data.get('dx') == 'Yes' and not self.cleaned_data.get('ctx') and not self.cleaned_data.get('nvp'):
            raise forms.ValidationError('If Diagnosis is given, provide information about relation to study ctx placebo and relation to infant nvp')

        # validation for ensuring that diagnosis table is only filled when its confirmed that new diagnoses occurred.
        infant_fu_dx = cleaned_data.get('infant_fu_dx')
        if infant_fu_dx.has_dx == 'No':
            raise forms.ValidationError('You are listing diagnosis relation details yet answered \'NO\', no new diagnosis for this patient.')

        return super(InfantFuDx2ProphItemsForm, self).clean()

    class Meta:
        model = InfantFuDx2ProphItems


class InfantFuDForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    class Meta:
        model = InfantFuD


class InfantFuMedForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if 'vaccination' in cleaned_data:
            self.validate_m2m(
                    label=' infant vaccination',
                    leading=cleaned_data.get('vaccines_received'),
                    m2m=cleaned_data.get('vaccination'))
        return cleaned_data

    class Meta:
        model = InfantFuMed


class InfantFuNewMedForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    class Meta:
        model = InfantFuNewMed


class InfantFuNewMedItemsForm (BaseInfantModelForm):

    def clean(self):

        cleaned_data = self.cleaned_data
        # validating that the medication listing is only done when its identified that new meds are given
        infant_fu_med = cleaned_data.get('infant_fu_med')
        if infant_fu_med.new_medications == 'No':
            raise forms.ValidationError('Give new medication listing only when new medication has been received. You answered \'NO\',')
        return super(InfantFuNewMedItemsForm, self).clean()

    class Meta:
        model = InfantFuNewMedItems
