from django import forms

from .base_maternal_model_form import BaseMaternalModelForm
from ..models import MaternalPostFu, MaternalPostFuDx, MaternalPostFuDxT


class MaternalPostFuForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = super(MaternalPostFuForm, self).clean()
        if 'chronic_cond' in cleaned_data.keys():
            self.validate_m2m(
                    label='new chronic condition',
                    leading=cleaned_data['has_chronic_cond'],
                    m2m=cleaned_data['chronic_cond'],
                    other=cleaned_data['chronic_cond_other'])
        # breastfeeding mothers, indicate whether they had mastitis or not
        if cleaned_data.get('breastfeeding', None) == 'Yes' and cleaned_data.get('had_mastitis', None) == 'None':
            raise forms.ValidationError("the mother was breastfeeding, indicate whether she had mastitis or not. You wrote '%s'" % cleaned_data['had_mastitis'])
        return cleaned_data

    class Meta:
        model = MaternalPostFu


class MaternalPostFuDxForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
#         cleaned_data = super(MaternalPostFuDxForm, self).clean()
        check_dx = self.data.get('maternalpostfudxt_set-0-post_fu_dx')
#         if 'wcs_dx_adult' in cleaned_data.keys():
#             self.validate_m2m(
#                     label = 'WHO stage III/IV Diagnosis',
#                     leading = cleaned_data['who_clinical_stage'],
#                     m2m = cleaned_data['wcs_dx_adult'])
        if cleaned_data.get('new_diagnoses') == 'Yes' and not check_dx:
            raise forms.ValidationError('You indicated that participant had new diagnosis and yet did not provide them. Please correct.')     

        return cleaned_data

    class Meta:
        model = MaternalPostFuDx


class MaternalPostFuDxTForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        
        if cleaned_data.get('maternal_post_fu').new_diagnoses =='No' and cleaned_data.get('post_fu_dx'):
            raise forms.ValidationError('You indicated that there was NO new diagnosis and yet provided a diagnosis. Please correct.')
        
        if cleaned_data.get('post_fu_dx'):
            if not cleaned_data.get('post_fu_specify') or not cleaned_data.get('grade') or not cleaned_data.get('hospitalized'):
                raise forms.ValidationError('Please fill in all diagnosis information.')
            
        if cleaned_data.get('maternal_post_fu').mother_hospitalized =='No' and cleaned_data.get('hospitalized'):
            raise forms.ValidationError('You indicated that participant was not hospitalized above. Please correct.')
            
        return cleaned_data

    class Meta:
        model = MaternalPostFuDxT
