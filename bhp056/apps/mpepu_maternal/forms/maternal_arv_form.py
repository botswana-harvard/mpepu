from django import forms

from edc.subject.consent.forms import BaseConsentedModelForm

from .base_maternal_model_form import BaseMaternalModelForm
from ..models import MaternalArvPost, MaternalArvPostMod, MaternalArvPostAdh, MaternalArvPregHistory, MaternalArvPPHistory, MaternalArvPreg, MaternalArv


class MaternalArvPostForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = super(MaternalArvPostForm, self).clean()
        check_arvs = self.data.get('maternalarvpostmod_set-0-arv_code')
        # if mother is not supposed to be on ARVS,then the MaternalArvPostAdh is not required
        if cleaned_data['haart_last_visit'].lower() == 'no' or  cleaned_data['arv_status'].lower() == 'never started':
            if MaternalArvPostAdh.objects.filter(maternal_visit=cleaned_data.get('maternal_visit')):
                raise forms.ValidationError("ARV history exists. You wrote mother did NOT receive ARVs "
                                            "in this pregnancy. Please correct '%s' first." % MaternalArvPostAdh._meta.verbose_name)
                
        if cleaned_data.get('haart_last_visit')=='No' and cleaned_data.get('haart_reason')!='N/A':
            raise forms.ValidationError('You indicated that participant was not on HAART. You CANNOT provide a reason. Please correct.')
        if cleaned_data.get('haart_last_visit')=='Yes' and cleaned_data.get('haart_reason')=='N/A':
            raise forms.ValidationError("You indicated that participant was on HAART. Reason CANNOT be 'Not Applicable'. Please correct.")
        
        if cleaned_data.get('arv_status') != 'N/A' or cleaned_data.get('arv_status') != 'no_mod':
            if not check_arvs:
                raise forms.ValidationError('You indicated that the participants ARV status has changed. Please provide details.')

        return cleaned_data

    class Meta:
        model = MaternalArvPost


class MaternalArvPostModForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = super(MaternalArvPostModForm, self).clean()
        
        if cleaned_data.get('maternal_arv_post').arv_status =='N/A' or cleaned_data.get('maternal_arv_post').arv_status =='no_mod':
            if cleaned_data.get('arv_code'):
                raise forms.ValidationError("You cannot indicate arv modifaction as you indicated 'Not applicable' or 'No modifications above.")
        return cleaned_data

    class Meta:
        model = MaternalArvPostMod


class MaternalArvPostAdhForm (BaseMaternalModelForm):
    # TODO: can you check if the combination is legal????
    #if is_legal_combination(cleaned_data):
        #pass
        #raise ValidationError('Drug combination is unknown.')
    class Meta:
        model = MaternalArvPostAdh


class MaternalArvPregForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['took_arv'].lower() == 'no':
            if MaternalArvPPHistory.objects.filter(maternal_visit=cleaned_data.get('maternal_visit')):
                raise forms.ValidationError("ARV history exists. You wrote mother did NOT receive ARVs in this pregnancy. "
                                            "Please correct '%s' first." % MaternalArvPregHistory._meta.verbose_name)
        if cleaned_data.get('start_pp').lower() == 'no':
            if MaternalArvPPHistory.objects.filter(maternal_visit=cleaned_data.get('maternal_visit')):
                raise forms.ValidationError("ARV history exists. You wrote mother did NOT start ARVs "
                                            "post partum. Please correct '%s' first." % MaternalArvPPHistory._meta.verbose_name)
        return super(MaternalArvPregForm, self).clean()

    class Meta:
        model = MaternalArvPreg


class MaternalArvPregHistoryForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = super(MaternalArvPregHistoryForm, self).clean()
        check_arvs = self.data.get('maternalarv_set-0-arv_code')
        took_arv = cleaned_data.get('maternal_arv_preg').took_arv
        # if yes is indicated for any arv's started in Maternal ARV in This Preg then list must be provided
        if took_arv == 'Yes' and not check_arvs:
            raise forms.ValidationError("You indicated that participant started ARV(s) during this pregnancy on 'Maternal ARV in This Preg'. Please list them or correct 'Maternal ARV in This Preg'.")
        # if no is indicated for any arv's started in Maternal ARV in This Preg then list must be provided
        if took_arv == 'No' and check_arvs:
            raise forms.ValidationError("You indicated that ARV(s) were NOT started during this pregnancy on 'Maternal ARV in This Preg'. You cannot provide a list or correct 'Maternal ARV in This Preg'.")
        
        if cleaned_data.get('is_interrupt')=='Yes' and cleaned_data.get('interrupt')=='N/A':
            raise forms.ValidationError("'You indicated there was an interruption in the ARVs received. Reason cannot be 'Not applicable'")
        
        if cleaned_data.get('is_interrupt')=='No' and cleaned_data.get('interrupt')!='N/A':
            raise forms.ValidationError("'You indicated there was no interruption in the ARVs received. Reason cannot be 'Not applicable'")
            
        return cleaned_data

    class Meta:
        model = MaternalArvPregHistory


class MaternalArvPPHistoryForm (BaseMaternalModelForm):
    def clean(self):       
        cleaned_data = super(MaternalArvPPHistoryForm, self).clean()
        start_pp = cleaned_data.get('maternal_arv_preg').start_pp
        check_arvs = self.data.get('maternalarv_set-0-arv_code')
        
        # if yes is indicated for any arv's started immediately postpartum Maternal ARV in This Preg then list must be provided
        if start_pp == 'Yes' and not check_arvs:
            raise forms.ValidationError("You indicated that participant started ARV(s) immediately postpartum on 'Maternal ARV in This Preg'. Please provide a list or correct 'Maternal ARV in This Preg'.")
        
        # if no is indicated for any arv's started immediately postpartum Maternal ARV in This Preg then list must be provided
        if start_pp == 'No' and check_arvs:
            raise forms.ValidationError("You indicated that ARV(s) were NOT started immediately postpartum on 'Maternal ARV in This Preg'. You cannot provide a list. or correct 'Maternal ARV in This Preg'.")
        
        return cleaned_data

    class Meta:
        model = MaternalArvPPHistory

class MaternalArvForm(BaseConsentedModelForm):
    def clean(self):
        cleaned_data = super(MaternalArvForm, self).clean()
        if cleaned_data.get('arv_code') and not cleaned_data.get('date_start'):
            raise forms.ValidationError('Please provide the date ARV(s) were started.')
        
        return cleaned_data
    
    class Meta:
        model = MaternalArv