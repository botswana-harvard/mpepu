from django import forms
from apps.mpepu_infant.models import InfantBirth, InfantBirthExam, InfantBirthArv, InfantBirthFeed, InfantBirthData
from ..models import MaternalLabDel
from .base_infant_model_form import BaseInfantModelForm


class InfantBirthForm (BaseInfantModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        # does dob match maternal lab del?
        maternal_identifier = cleaned_data.get('registered_subject', None).relative_identifier
        if MaternalLabDel.objects.filter(maternal_visit__appointment__registered_subject__subject_identifier=maternal_identifier):
            maternal_lab_del = MaternalLabDel.objects.get(maternal_visit__appointment__registered_subject__subject_identifier=maternal_identifier)
            if not cleaned_data.get('dob', None) == maternal_lab_del.delivery_datetime.date():
                raise forms.ValidationError('Infant dob must match maternal delivery date of %s. You wrote %s' % (maternal_lab_del.delivery_datetime.date(), cleaned_data.get('dob', None),))
        else:
            raise forms.ValidationError('Cannot find maternal labour and delivery form for this infant! This is not expected.')
        return cleaned_data

    class Meta:
        model = InfantBirth


class InfantBirthExamForm (BaseInfantModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data

        # physical exam normal, heet exam no required"""
        if cleaned_data.get('physical_exam_result', None) == 'NORMAL' and cleaned_data.get('heent_exam', None) != 'N/A':
            raise forms.ValidationError("If physical exam is normal then heent exam is not required, please correct. You wrote '%s'" % cleaned_data.get('heent_exam', None))
        # physical exam normal, resp exam no required"""
        if cleaned_data.get('physical_exam_result', None) == 'NORMAL' and cleaned_data.get('resp_exam', None) != 'N/A':
            raise forms.ValidationError("If physical exam is normal then respiratory exam is not required, please correct. You wrote '%s'" % cleaned_data.get('resp_exam', None))

        #physical exam normal, cardiac exam no required"""
        if cleaned_data.get('physical_exam_result', None) == 'NORMAL' and cleaned_data.get('cardiac_exam', None) != 'N/A':
            raise forms.ValidationError("If physical exam is normal then heent cardiac is not required, please correct. You wrote '%s'" % cleaned_data.get('cardiac_exam', None))

        #physical exam normal, abdominal exam no required"""
        if cleaned_data.get('physical_exam_result', None) == 'NORMAL' and cleaned_data.get('abdominal_exam', None) != 'N/A':
            raise forms.ValidationError("If physical exam is normal then abdominal exam is not required, please correct. You wrote '%s'" % cleaned_data.get('abdominal_exam', None))

        #physical exam normal, skin exam no required"""
        if cleaned_data.get('physical_exam_result', None) == 'NORMAL' and cleaned_data.get('skin_exam', None) != 'N/A':
            raise forms.ValidationError("If physical exam is normal then skin exam is not required, please correct. You wrote '%s'" % cleaned_data.get('skin_exam', None))

        #physical exam normal, rash observation not required"""
        if cleaned_data.get('physical_exam_result', None) == 'NORMAL' and cleaned_data.get('macular_papular_rash', None) != 'N/A':
            raise forms.ValidationError("If physical exam is normal then heent rash observation required, please correct. You wrote '%s'" % cleaned_data.get('macular_papular_rash', None))

        #physical exam normal, neurologic exam no required"""
        if cleaned_data.get('physical_exam_result', None) == 'NORMAL' and cleaned_data.get('neurologic_exam', None) != 'N/A':
            raise forms.ValidationError("If physical exam is normal then heent neurological exam required, please correct. You wrote '%s'" % cleaned_data.get('neurologic_exam', None))
        return super(InfantBirthExamForm, self).clean()

    class Meta:
        model = InfantBirthExam


class InfantBirthDataForm (BaseInfantModelForm):

    class Meta:
        model = InfantBirthData


class InfantBirthArvForm (BaseInfantModelForm):

    class Meta:
        model = InfantBirthArv


class InfantBirthFeedForm (BaseInfantModelForm):

    class Meta:
        model = InfantBirthFeed
