from datetime import datetime, date

from django import forms

from .base_maternal_model_form import BaseMaternalModelForm
from ..models import MaternalLabDel, MaternalLabDelMed, MaternalLabDelClinic, MaternalLabDelDx, MaternalLabDelDxT


class MaternalLabDelForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('maternal_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')

        #validate that if gestational age is known that the age in weeks should be provided
        if cleaned_data.get('has_ga') == 'Yes' and not cleaned_data.get('ga'):
            raise forms.ValidationError('If patient gestational age is known, give the gestational age in weeks')

        if cleaned_data.get('has_ga') == 'No' and cleaned_data.get('ga'):
            raise forms.ValidationError('If patient gestational age is NOT known, you CANNOT provide the gestational age. Please correct')

        #if its confirmed that there is a delivery complication, confirm listing. If other selected, describe the complication
        if 'del_comp' in cleaned_data.keys():
            self.validate_m2m(
                    label='delivery complication',
                    leading=cleaned_data.get('has_del_comp'),
                    m2m=cleaned_data.get('del_comp'),
                    other=cleaned_data.get('del_comp_other'),
            )

        #to ensure that maternal labour delivery is not greater than today
        if cleaned_data.get('delivery_datetime'):
            if cleaned_data.get('delivery_datetime') > datetime.today():
                raise forms.ValidationError('Maternal Labour Delivery date cannot be greater than today\'s date. Please correct.')

        #still born validations
        if cleaned_data.get('still_borns') > 0 and cleaned_data.get('still_born_has_congen_abn') == 'N/A':
            raise forms.ValidationError("You indicated there were still births yet selected 'Not applicable' for congenital abonormality. Please correct.")
        if cleaned_data.get('still_born_has_congen_abn') == 'Yes' and not cleaned_data.get('still_born_congen_abn'):
            raise forms.ValidationError('You indicated that stillborns did have congenital abnormalities. Please specify.')
        if cleaned_data.get('still_born_has_congen_abn') != 'Yes' and cleaned_data.get('still_born_congen_abn'):
            raise forms.ValidationError('You indicated that stillborns did not have congenital abnormalities and yet provided specifications. Please correct.')

        #validate that number of live_infants_to_register cannot be 0
        if cleaned_data.get('live_infants_to_register') == 0:
            raise forms.ValidationError('Number of live infants to register may not be 0!.')

        #validate birth number vs registerning number
        if cleaned_data.get('live_infants_to_register') > cleaned_data.get('live_infants'):
            raise forms.ValidationError("You indicated that you are registering "+repr(cleaned_data.get('live_infants_to_register')) +" Yet there are "+repr(cleaned_data.get('live_infants'))+" live births. Please correct.")

        return super(MaternalLabDelForm, self).clean()

    class Meta:
        model = MaternalLabDel


class MaternalLabDelMedForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('maternal_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')
        if 'health_cond' in cleaned_data.keys():
            self.validate_m2m(
                    label='health condition',
                    leading=cleaned_data.get('has_health_cond'),
                    m2m=cleaned_data.get('health_cond'),
                    other=cleaned_data.get('health_cond_other'))
        if 'ob_comp' in cleaned_data.keys():
            self.validate_m2m(
                    label='obstetric complication',
                    leading=cleaned_data.get('has_ob_comp'),
                    m2m=cleaned_data.get('ob_comp'),
                    other=cleaned_data.get('ob_comp_other'))
        return super(MaternalLabDelMedForm, self).clean()

    class Meta:
        model = MaternalLabDelMed


class MaternalLabDelClinicForm (BaseMaternalModelForm):
    def clean(self):

        cleaned_data = self.cleaned_data
        if not cleaned_data.get('maternal_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')
        if 'suppliment' in cleaned_data.keys():
            self.validate_m2m(
                    label='pregnancy suppliment',
                    leading=cleaned_data.get('took_suppliments'),
                    m2m=cleaned_data.get('suppliment'))

        # cd4 was done, enter cd4 date
        if cleaned_data.get('has_cd4') == 'Yes':
            if not cleaned_data.get('cd4_date') or not cleaned_data.get('cd4_result'):
                raise forms.ValidationError("You indicated CD4 test was done, enter cd4 date and result.")

        # cd4 was not done, you cannot enter cd4 date
        if cleaned_data.get('has_cd4') == 'No':
            if cleaned_data.get('cd4_date') or cleaned_data.get('cd4_result'):
                raise forms.ValidationError("You indicated CD4 test was NOT done, you cannot enter cd4 date and result.")

        # if viral load was done, date and result should be provided
        if cleaned_data.get('has_vl') == 'Yes':
            if not cleaned_data.get('vl_date') or not cleaned_data.get('vl_result'):
                raise forms.ValidationError("You indicated that the Viral Load test was done. Enter date and result.")

        # if viral load was not done, date and result should be not be provided
        if cleaned_data.get('has_vl') == 'No':
            if cleaned_data.get('vl_date') or cleaned_data.get('vl_result'):
                raise forms.ValidationError("You indicated that the Viral Load test was NOT done. You cannot enter date and result.")
        return super(MaternalLabDelClinicForm, self).clean()

    class Meta:
        model = MaternalLabDelClinic


class MaternalLabDelDxForm (BaseMaternalModelForm):
    def clean(self):
#         cleaned_data = super(MaternalLabDelDxForm,self).clean()
        cleaned_data = self.cleaned_data
        check_dx = self.data.get('maternallabdeldxt_set-0-lab_del_dx')
        if not cleaned_data.get('maternal_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')

        #WHO validations
        if not cleaned_data.get('wcs_dx_adult'):
            raise forms.ValidationError("You cannot leave WHO diagnosis blank. Please selct an option")
        if cleaned_data.get('has_who_dx') == 'Yes' and [True for item in cleaned_data.get('wcs_dx_adult') if (item.short_name.lower() == 'not applicable' or item.short_name.lower() == 'asymptomatic')]:
            raise forms.ValidationError("You stated there are ARE WHO diagnoses. Please indicate them.")
        if cleaned_data.get('has_who_dx') == 'No' and not [True for item in cleaned_data.get('wcs_dx_adult') if (item.short_name.lower() == 'not applicable' or item.short_name.lower() == 'asymptomatic')]:
            raise forms.ValidationError("You stated there are NO WHO diagnoses. Please correct.")

        #Validate diagnosis
        if cleaned_data.get('has_preg_dx') == 'Yes' and not check_dx:
            raise forms.ValidationError('You indicated that participant had diagnosis. Please list them.')

#         return super(MaternalLabDelDxForm,self).clean()
        return cleaned_data

    class Meta:
        model = MaternalLabDelDx


class MaternalLabDelDxTForm (BaseMaternalModelForm):

    def clean(self):
        cleaned_data = super(MaternalLabDelDxTForm,self).clean()
        maternal_lab_del_dx = cleaned_data.get('maternal_lab_del_dx')

        if maternal_lab_del_dx.has_preg_dx == 'No' and cleaned_data.get('lab_del_dx'):
            raise forms.ValidationError('You have indicated that the participant did NOT have diagnosis and yet provided them. Please correct.')
        return cleaned_data

    class Meta:
        model = MaternalLabDelDxT
