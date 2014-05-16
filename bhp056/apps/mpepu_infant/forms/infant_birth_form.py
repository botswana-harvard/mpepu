from django import forms

from edc.subject.registration.models import RegisteredSubject

from apps.mpepu_infant.models import InfantBirth, InfantBirthExam, InfantBirthArv, InfantBirthFeed, InfantBirthData

from ..models import MaternalLabDel
from .base_infant_model_form import BaseInfantModelForm


class InfantBirthForm (BaseInfantModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('infant_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')
        # does dob match maternal lab del?
        maternal_identifier = cleaned_data.get('registered_subject', None)
        if maternal_identifier:
            maternal_identifier = maternal_identifier.relative_identifier
        if MaternalLabDel.objects.filter(maternal_visit__appointment__registered_subject__subject_identifier=maternal_identifier):
            maternal_lab_del = MaternalLabDel.objects.get(maternal_visit__appointment__registered_subject__subject_identifier=maternal_identifier)
            if not cleaned_data.get('dob', None) == maternal_lab_del.delivery_datetime.date():
                raise forms.ValidationError('Infant dob must match maternal delivery date of %s. You wrote %s' % (maternal_lab_del.delivery_datetime.date(), cleaned_data.get('dob', None),))
        else:
            raise forms.ValidationError('Cannot find maternal labour and delivery form for this infant! This is not expected.')
        # if multiple birth, cannot have the same birth order
        infants = RegisteredSubject.objects.filter(relative_identifier=cleaned_data.get('registered_subject').relative_identifier).order_by('subject_identifier')
        index = 0
        for infant in infants:
            index = index+1
            if infant == cleaned_data.get('registered_subject'):
                if cleaned_data.get('birth_order') != index:
                    raise forms.ValidationError('Birth order for this infant can only be {0}, you indicated {1}. Please correct'.format(index, cleaned_data.get('birth_order')))
        return super(InfantBirthForm, self).clean()

    class Meta:
        model = InfantBirth


class InfantBirthExamForm (BaseInfantModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        birth = cleaned_data.get('infant_birth')

        if not cleaned_data.get('infant_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')

        #validate other general activity
        if cleaned_data.get('general_activity') == 'ABNORMAL' and not cleaned_data.get('abnormal_activity'):
            raise forms.ValidationError('You indicated that the general activity was abnormal. Please specify abnormality.')

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
            raise forms.ValidationError("If physical exam is normal then heent rash observation not required, please correct. You wrote '%s'" % cleaned_data.get('macular_papular_rash', None))

        #physical exam normal, neurologic exam no required"""
        if cleaned_data.get('physical_exam_result', None) == 'NORMAL' and cleaned_data.get('neurologic_exam', None) != 'N/A':
            raise forms.ValidationError("If physical exam is normal then heent neurological exam not required, please correct. You wrote '%s'" % cleaned_data.get('neurologic_exam', None))

        #physical exam abnormal and no abnormalities indicated
        if cleaned_data.get('physical_exam_result') == 'ABNORMAL':
            if (cleaned_data.get('heent_exam') != 'Yes' and cleaned_data.get('resp_exam') != 'Yes' and cleaned_data.get('cardiac_exam') != 'Yes' and cleaned_data.get('abdominal_exam') != 'Yes'
                and cleaned_data.get('skin_exam') != 'Yes' and cleaned_data.get('macular_papular_rash') != 'Yes' and cleaned_data.get('neurologic_exam') != 'Yes'):
                raise forms.ValidationError('You indicated that participant had abnormal findings for the physical exam. Please indicate at least one.')

        #HEENT exam abnormal, specify abnormality
        if cleaned_data.get('heent_exam', None) == 'Yes' and not cleaned_data.get('heent_no_other'):
            raise forms.ValidationError('You indicated HEENT exam was abnormal. Please specify.')

        #Respiratory exam  abnormal, specify abnormality
        if cleaned_data.get('resp_exam', None) == 'Yes' and not cleaned_data.get('resp_exam_other'):
            raise forms.ValidationError('You indicated Respiratory exam was abnormal. Please specify.')

        #Cardiac exam  abnormal, specify abnormality
        if cleaned_data.get('cardiac_exam', None) == 'Yes' and not cleaned_data.get('cardiac_exam_other'):
            raise forms.ValidationError('You indicated Cardiac exam was abnormal. Please specify.')

        #Abdominal exam  abnormal, specify abnormality
        if cleaned_data.get('abdominal_exam', None) == 'Yes' and not cleaned_data.get('abdominal_exam_other'):
            raise forms.ValidationError('You indicated Abdominal exam was abnormal. Please specify.')

        #Skin exam  abnormal, specify abnormality
        if cleaned_data.get('skin_exam', None) == 'Yes' and not cleaned_data.get('skin_exam_other'):
            raise forms.ValidationError('You indicated Skin exam was abnormal. Please specify.')

        #Neurological exam  abnormal, specify abnormality
        if cleaned_data.get('neurologic_exam', None) == 'Yes' and not cleaned_data.get('neuro_exam_other'):
            raise forms.ValidationError('You indicated neurological exam was abnormal. Please specify.')

        #validate gender with Infant Birth
        if birth.gender != 'U' or cleaned_data.get('gender') != 'U':
            if birth.gender != cleaned_data.get('gender'):
                raise forms.ValidationError('The gender does not correspond to gender as indicated in Infant Birth. Please correct Infant Birth first. ')

        return super(InfantBirthExamForm, self).clean()

    class Meta:
        model = InfantBirthExam


class InfantBirthDataForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('infant_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')
        #apgar score results required
        if cleaned_data.get('apgar_score') == 'Yes':
            if not cleaned_data.get('apgar_score_min_1') or not cleaned_data.get('apgar_score_min_5') or not cleaned_data.get('apgar_score_min_10'):
                raise forms.ValidationError("You indicated that apgar score was performed. Please provide the results.")

        #apgar score results should not be entered
        if cleaned_data.get('apgar_score') == 'No':
            if cleaned_data.get('apgar_score_min_1') or cleaned_data.get('apgar_score_min_5') or cleaned_data.get('apgar_score_min_10'):
                raise forms.ValidationError("You indicated that apgar score NOT was performed. Yet you provided results, please correct.")
        return super(InfantBirthDataForm, self).clean()

    class Meta:
        model = InfantBirthData


class InfantBirthArvForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        birth = cleaned_data.get('infant_birth')

        if not cleaned_data.get('infant_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')
        #validate azt
        if cleaned_data.get('azt_after_birth') == 'Yes' and not cleaned_data.get('azt_dose_date'):
            raise forms.ValidationError('You indicated that AZT was given after birth, please provide the date it was administered')

        if cleaned_data.get('azt_after_birth') == 'No' and cleaned_data.get('azt_dose_date'):
            raise forms.ValidationError('You indicated that AZT was NOT given after birth and yet provided the date it was administered. Please correct.')
        #validate nvp
        if cleaned_data.get('sdnvp_after_birth') == 'Yes' and not cleaned_data.get('nvp_dose_date'):
            raise forms.ValidationError('You indicated that NVP was given after birth, please provide the date it was administered')

        if cleaned_data.get('sdnvp_after_birth') == 'No' and cleaned_data.get('nvp_dose_date'):
            raise forms.ValidationError('You indicated that NVP was NOT given after birth and yet provided the date it was administered. Please correct.')

        #ensure dates given not before dob
        if cleaned_data.get('azt_dose_date') and birth:
            if cleaned_data.get('azt_dose_date') < birth.dob:
                raise forms.ValidationError('AZT dose date is before Date of Birth. Please correct.')

        if cleaned_data.get('nvp_dose_date') and birth:
            if cleaned_data.get('nvp_dose_date') < birth.dob:
                raise forms.ValidationError('NVP dose date is before Date of Birth. Please correct.')
        return super(InfantBirthArvForm, self).clean()

    class Meta:
        model = InfantBirthArv


class InfantBirthFeedForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('infant_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')
        return super(InfantBirthFeedForm, self).clean()

    class Meta:
        model = InfantBirthFeed
