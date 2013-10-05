from django import forms
from apps.mpepu_infant.models import InfantStudyDrug, InfantStudyDrugItems, InfantCtxPlaceboAdh
from .base_infant_model_form import BaseInfantModelForm


class InfantStudyDrugForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = super(InfantStudyDrugForm, self).clean()
        # if infant not on CTX/Placebo before this visit then InfantCtxPlaceboAdh is not required """
        if cleaned_data['on_placebo_status'].upper() == 'NO':
            if InfantCtxPlaceboAdh.objects.filter(infant_visit=cleaned_data.get('infant_visit')).exists():
                raise forms.ValidationError("Adherence data exists. You wrote infant was not on drug "
                                            "before this visit. Please correct '%s' first." % InfantCtxPlaceboAdh._meta.verbose_name)
        return cleaned_data

    class Meta:
        model = InfantStudyDrug


class InfantStudyDrugItemsForm (BaseInfantModelForm):

    def clean(self):
        cleaned_data = super(InfantStudyDrugItemsForm, self).clean()
        #drug listing dependent upon the participants CTX/placebo status
        inf_study_drug = cleaned_data.get('inf_study_drug')
        if inf_study_drug.drug_status == 'No modification' or inf_study_drug.drug_status == 'Never started':
            raise forms.ValidationError('Do not fill out the study drug items because you have stated that there was \'NO modification, never started\' drugs')
        return cleaned_data

    class Meta:
        model = InfantStudyDrugItems
