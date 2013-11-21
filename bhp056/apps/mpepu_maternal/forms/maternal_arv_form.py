from django import forms

from .base_maternal_model_form import BaseMaternalModelForm
from ..models import MaternalArvPost, MaternalArvPostMod, MaternalArvPostAdh, MaternalArvPregHistory, MaternalArvPPHistory, MaternalArvPreg


class MaternalArvPostForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        # if mother is not supposed to be on ARVS,then the MaternalArvPostAdh is not required
        if cleaned_data['haart_last_visit'].lower() == 'no' or  cleaned_data['arv_status'].lower() == 'never started':
            if MaternalArvPostAdh.objects.filter(maternal_visit=cleaned_data.get('maternal_visit')):
                raise forms.ValidationError("ARV history exists. You wrote mother did NOT receive ARVs "
                                            "in this pregnancy. Please correct '%s' first." % MaternalArvPostAdh._meta.verbose_name)

        return super(MaternalArvPostForm, self).clean()

    class Meta:
        model = MaternalArvPost


class MaternalArvPostModForm (BaseMaternalModelForm):

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
        
        if cleaned_data.get('is_interrupt')=='Yes' and cleaned_data.get('interrupt')=='N/A':
            raise forms.ValidationError("'You indicated there was an interruption in the ARVs received. Reason cannot be 'Not applicable'")
        
        if cleaned_data.get('is_interrupt')=='No' and cleaned_data.get('interrupt')!='N/A':
            raise forms.ValidationError("'You indicated there was no interruption in the ARVs received. Reason cannot be 'Not applicable'")
            
        return cleaned_data

    class Meta:
        model = MaternalArvPregHistory


class MaternalArvPPHistoryForm (BaseMaternalModelForm):

    class Meta:
        model = MaternalArvPPHistory
