from datetime import datetime, date

from django import forms

from .base_maternal_model_form import BaseMaternalModelForm
from ..models import MaternalLabDel, MaternalLabDelMed, MaternalLabDelClinic, MaternalLabDelDx, MaternalLabDelDxT


class MaternalLabDelForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        
        #validate that if gestational age is known that the age in weeks should be provided
        if cleaned_data['has_ga'] == 'Yes' and not cleaned_data['ga']:
            raise forms.ValidationError('If patient gestational age is known, give the gestational age in weeks')
 
        #if its confirmed that there is a delivery complication, confirm listing. If other selected, describe the complication
        if 'del_comp' in cleaned_data.keys():
            self.validate_m2m(
                    label='delivery complication',
                    leading=cleaned_data['has_del_comp'],
                    m2m=cleaned_data['del_comp'],
                    other=cleaned_data['del_comp_other'],
            )
        
        #to ensure that maternal labour delivery is not greater than today
        if cleaned_data.get('delivery_datetime'):
            if cleaned_data.get('delivery_datetime') > datetime.today():
                raise forms.ValidationError('Maternal Labour Delivery date cannot be greater than today\'s date. Please correct.')
        
        return super(MaternalLabDelForm, self).clean()

    class Meta:
        model = MaternalLabDel


class MaternalLabDelMedForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if 'health_cond' in cleaned_data.keys():
            self.validate_m2m(
                    label='health condition',
                    leading=cleaned_data['has_health_cond'],
                    m2m=cleaned_data['health_cond'],
                    other=cleaned_data['health_cond_other'])
        if 'ob_comp' in cleaned_data.keys():
            self.validate_m2m(
                    label='obstetric complication',
                    leading=cleaned_data['has_ob_comp'],
                    m2m=cleaned_data['ob_comp'],
                    other=cleaned_data['ob_comp_other'])
        return super(MaternalLabDelMedForm, self).clean()

    class Meta:
        model = MaternalLabDelMed


class MaternalLabDelClinicForm (BaseMaternalModelForm):
    def clean(self):

        cleaned_data = self.cleaned_data
        if 'suppliment' in cleaned_data.keys():
            self.validate_m2m(
                    label='pregnancy suppliment',
                    leading=cleaned_data['took_suppliments'],
                    m2m=cleaned_data['suppliment'])
        # cd4 was done, enter cd4 date
        if cleaned_data['has_cd4'] == 'Yes' and cleaned_data['cd4_date'] == 'blank' or cleaned_data['cd4_date'] == 'null':
            raise forms.ValidationError("the cd4 test was done, enter cd4 date. You wrote '%s'" % cleaned_data['cd4_date'])
        return super(MaternalLabDelClinicForm, self).clean()

    class Meta:
        model = MaternalLabDelClinic


class MaternalLabDelDxForm (BaseMaternalModelForm):

    class Meta:
        model = MaternalLabDelDx


class MaternalLabDelDxTForm (BaseMaternalModelForm):

    class Meta:
        model = MaternalLabDelDxT
