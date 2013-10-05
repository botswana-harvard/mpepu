from django import forms

from .base_maternal_model_form import BaseMaternalModelForm
from ..models import MaternalPostFu, MaternalPostFuDx, MaternalPostFuDxT


class MaternalPostFuForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if 'chronic_cond' in cleaned_data.keys():
            self.validate_m2m(
                    label='new chronic condition',
                    leading=cleaned_data['has_chronic_cond'],
                    m2m=cleaned_data['chronic_cond'],
                    other=cleaned_data['chronic_cond_other'])
        # breastfeeding mothers, indicate whether they had mastitis or not
        if cleaned_data.get('breastfeeding', None) == 'Yes' and cleaned_data.get('had_mastitis', None) == 'None':
            raise forms.ValidationError("the mother was breastfeeding, indicate whether she had mastitis or not. You wrote '%s'" % cleaned_data['had_mastitis'])
        return super(MaternalPostFuForm, self).clean()

    class Meta:
        model = MaternalPostFu


class MaternalPostFuDxForm (BaseMaternalModelForm):

    class Meta:
        model = MaternalPostFuDx


class MaternalPostFuDxTForm (BaseMaternalModelForm):

    class Meta:
        model = MaternalPostFuDxT
