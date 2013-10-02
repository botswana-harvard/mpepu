from django import forms
from datetime import datetime, date 
from bhp_adverse.forms import BaseInfantDeathForm
from mpepu_infant.models import *
from base_infant_model_form import BaseInfantModelForm


class InfantDeathForm (BaseInfantDeathForm):
    def clean(self):
        cleaned_data = super(InfantDeathForm, self).clean()
        # 6
        if cleaned_data['death_reason_hospitalized']:
            if 'specify' in cleaned_data['death_reason_hospitalized'].name.lower() and not cleaned_data['death_reason_hospitalized_other']:
                raise forms.ValidationError('Please specify further details for the reason hospitalized.')
        return cleaned_data

    class Meta:
        model = InfantDeath


class InfantPrerandoLossForm(BaseInfantModelForm):

    class Meta:
        model = InfantPrerandoLoss


class InfantStudyDrugInitForm (forms.ModelForm):

    class Meta:
        model = InfantStudyDrugInit


class InfantSurvivalForm (forms.ModelForm):

    class Meta:
        model = InfantSurvival


class InfantArvProphForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        # if baby is not supposed to be on prophylactic NVP,then the InfantNvpAdherence is not required """
        # if infant had no diarrheal illness, InfantFuD is not required """
        if cleaned_data['prophylatic_nvp'].lower() == 'no':
            if InfantNvpAdherence.objects.filter(infant_visit=cleaned_data.get('infant_visit')).exists():
                forms.ValidationError("NVP data is available, You wrote 'infant was not supposed to be on NVP. "
                                      "Please correct '%s' first." % InfantNvpAdherence._meta.verbose_name)

        return cleaned_data

    class Meta:
        model = InfantArvProph


class InfantArvProphModForm (forms.ModelForm):

    class Meta:
        model = InfantArvProphMod


class InfantHaartForm (forms.ModelForm):

    class Meta:
        model = InfantHaart


class InfantHaartModForm (forms.ModelForm):

    class Meta:
        model = InfantHaartMod


class InfantNvpAdherenceForm (BaseInfantModelForm):
    
    class Meta:
        model = InfantNvpAdherence


class InfantCtxPlaceboAdhForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
    #ensuring that when no drug is missed that reason becomes N/A   
        if cleaned_data['day_missed_drug'] == 0 and cleaned_data['reason_missed'] != 'N/A':
            raise forms.ValidationError('if no entire days where missed, your reason missed should be NOT APPLICABLE')
    #When days missed are greater than zero, other options other than N/A should be selected   
        if cleaned_data['day_missed_drug'] > 0 and cleaned_data['reason_missed'] =='N/A':
            raise forms.ValidationError('if days missed is greater than zero, reason misssed cannot be N/A')
    #validating that other,specify is given if other reason is selected
        if cleaned_data['reason_missed'] == 'OTHER' and not cleaned_data['reason_missed_other']:
            raise forms.ValidationError('If reason missed is other, please specify the reason in field provided')
        return cleaned_data
    class Meta:
        model = InfantCtxPlaceboAdh


class InfantFeedingForm (BaseInfantModelForm):
    
    def clean(self):
        cleaned_data = self.cleaned_data
        
        #validating that the weaning date is not greater than the visit/today's date
        if cleaned_data.get('formula_date'):
            if cleaned_data.get('formula_date') > date.today():
                raise forms.ValidationError('Date participant first received formula milk cannot be greater than today\'s date. Please correct.')
        if cleaned_data.get('most_recent_bm'):
            if cleaned_data.get('most_recent_bm') > date.today():
                raise forms.ValidationError('The most recent breast feeding date cannot be greater than today\'s date. Please correct.')
        
        #infants should either be FF or BF they cannot be neither
        if cleaned_data.get('other_feeding', None) != 'Yes' and cleaned_data.get('ever_breastfeed', None) != 'Yes':
            raise forms.ValidationError('Its impossible for infant to neither FF/liquids/BF. Infant has to either formula feed (2) or breast feed (8) Please correct')
        
        return cleaned_data

    class Meta:
        model = InfantFeeding


class InfantVerbalAutopsyForm (forms.ModelForm):

    class Meta:
        model = InfantVerbalAutopsy


class InfantCongenitalAnomaliesForm (forms.ModelForm):

    class Meta:
        model = InfantCongenitalAnomalies
