from django import forms
from apps.mpepu_infant.models import InfantStudyDrug, InfantStudyDrugItems, InfantCtxPlaceboAdh
from .base_infant_model_form import BaseInfantModelForm


class InfantStudyDrugForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = super(InfantStudyDrugForm, self).clean()
        # if infant not on CTX/Placebo before this visit then InfantCtxPlaceboAdh is not required """
        if cleaned_data['on_placebo_status'] == 'No':
            if InfantCtxPlaceboAdh.objects.filter(infant_visit=cleaned_data.get('infant_visit')).exists():
                raise forms.ValidationError("Adherence data exists. You wrote infant was not on drug "
                                            "before this visit. Please correct '%s' first." % InfantCtxPlaceboAdh._meta.verbose_name)
        # ensure that if starting or change in CTX/Placebo indicated then drug form should be filled in.
        check_drugs = self.data.get('infantstudydrugitems_set-0-dose_status')
        if cleaned_data.get('drug_status')=='Starting CTX/Placebo today' or cleaned_data.get('drug_status')=='Change in CTX/Placebo since the last scheduled visit or today':
            if not check_drugs:
                raise forms.ValidationError("Please fill out the study drug items as you indicated 'Starting' or 'Change' in CTX/Placebo.")
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
        # status is starting dose shouls be new
        if inf_study_drug.drug_status == 'Starting CTX/Placebo today' and cleaned_data.get('dose_status')!='New':
            raise forms.ValidationError("Drug status is indicated 'Starting CTX/Placebo', dose status must be 'New'. Please correct.")

        reasons = ['Initial dose','Never started', 'Scheduled dose increase', 'completed protocol', 'Death', 'Rash resolved' ]
        if cleaned_data.get('dose_status') == 'Temporarily held':
            for reason in reasons:
                if cleaned_data.get('modification_reason') == reason:
                    raise forms.ValidationError("Dose status is 'Temporarily Held', modification reason cannot be {}.".format(reason))

        return cleaned_data

    class Meta:
        model = InfantStudyDrugItems
