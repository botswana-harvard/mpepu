from datetime import date

from django import forms

from apps.mpepu_infant.models import InfantStudyDrug, InfantStudyDrugItems, InfantCtxPlaceboAdh, InfantStudyDrugInit

from .base_infant_model_form import BaseInfantModelForm


class InfantStudyDrugForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data

        if not cleaned_data.get('infant_visit'):
            raise forms.ValidationError('This field is required. Please fill it in.')
        # Ensure all required fields are keyed
        if not cleaned_data.get('on_placebo_status') or not cleaned_data.get('drug_status'):
            raise forms.ValidationError('This field is required. please fill it in.')
        # if infant not on CTX/Placebo before this visit then InfantCtxPlaceboAdh is not required """
        if cleaned_data.get('on_placebo_status') == 'No':
            if InfantCtxPlaceboAdh.objects.filter(infant_visit=cleaned_data.get('infant_visit')).exists():
                raise forms.ValidationError("Adherence data exists. You wrote infant was not on drug "
                                            "before this visit. Please correct '%s' first." 
                                            % InfantCtxPlaceboAdh._meta.verbose_name)
        # If Visit is 2010, then infant could not have been on study drug
        if cleaned_data.get('infant_visit').appointment.visit_definition.code == '2010':
            if cleaned_data.get('on_placebo_status') == 'Yes':
                raise forms.ValidationError('This is the 2010 Visit. Infant could NOT have been on Study Drug.'
                 'Please correct.')
        # ensure that if starting or change in CTX/Placebo indicated then drug form should be filled in.
        check_drugs = self.data.get('infantstudydrugitems_set-0-dose_status')
        if cleaned_data.get('drug_status')=='Starting CTX/Placebo today' or cleaned_data.get('drug_status')=='Change in CTX/Placebo since the last scheduled visit or today': 
            if not check_drugs:
                raise forms.ValidationError("Please fill out the study drug items as you indicated 'Starting' or 'Change' in CTX/Placebo.")
        # If study drug nerver start, provide a reason
        if cleaned_data.get('drug_status')=='Never started' and not check_drugs:
            raise forms.ValidationError('Please provide a reason why the study drug was not initiated.')
        return super(InfantStudyDrugForm, self).clean()

    class Meta:
        model = InfantStudyDrug


class InfantStudyDrugItemsForm (BaseInfantModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        #drug listing dependent upon the participants CTX/placebo status
        if cleaned_data.get('inf_study_drug'):
            inf_study_drug = cleaned_data.get('inf_study_drug')
            visit_code = inf_study_drug.infant_visit.appointment.visit_definition.code
            rando_date = inf_study_drug.infant_visit.appointment.registered_subject.randomization_datetime.date()
            if inf_study_drug.drug_status == 'No modification' and self.cleaned_data.get('dose_status'):
                raise forms.ValidationError('Do not fill out the study drug items because you have stated that there was \'NO modification\' to drugs')
            # status is starting dose should be new
            if inf_study_drug.drug_status == 'Starting CTX/Placebo today' and cleaned_data.get('dose_status')!='New':
                raise forms.ValidationError("Drug status is indicated 'Starting CTX/Placebo', dose status must be 'New'. Please correct.")
            if cleaned_data.get('dose_status') == 'Permanently discontinued' and cleaned_data.get('modification_reason') == 'completed protocol':
                if inf_study_drug.infant_visit.appointment.visit_definition.code != '2150' and inf_study_drug.infant_visit.appointment.visit_definition.code != '2180':
                    raise forms.ValidationError("You indicated Completion of protocol as reason study drug is permanently discontinued yet this is visit {}."
                                            .format(inf_study_drug.infant_visit.appointment.visit_definition.code))
        # if status is  'NEW' then reason can only be 'Initial Dose'
        if cleaned_data.get('dose_status') == 'New' and cleaned_data.get('modification_reason') != 'Initial dose':
            raise forms.ValidationError("You indicated that the dose status is 'New', modification reason should be 'Initial dose'. Please correct.")

        reasons = ['Initial dose','Never started', 'Scheduled dose increase', 'completed protocol', 'Death', 'Rash resolved' ]
        if cleaned_data.get('dose_status') == 'Temporarily held':
            for reason in reasons:
                if cleaned_data.get('modification_reason') == reason:
                    raise forms.ValidationError("Dose status is 'Temporarily Held', modification reason cannot be {}.".format(reason))

        # Validate dose status vs modification reason
        if cleaned_data.get('dose_status') == 'Permanently discontinued' and cleaned_data.get('modification_reason') == 'Initial dose':
            raise forms.ValidationError('You indicated dose status as "Permanently discontinued", You CANNOT indicate modification reason as "Initial dose". Please correct')
        no_start_reasons = ['Initial dose', 'Scheduled dose increase', 'completed protocol', 'Rash resolved', 'Completed postpartum tail', 'Completed PMTCT intervention']
        if cleaned_data.get('dose_status') == 'Not initiated':
            if cleaned_data.get('modification_reason') in no_start_reasons:
                raise forms.ValidationError('You indicated dose status as "Not initiated". Modification reason cannot be {}. Please correct'
                                        .format(cleaned_data.get('modification_reason')))
        # Ensure cannot start study drug more than once
        if cleaned_data.get('dose_status') == 'New':
            check_drugs = InfantStudyDrugItems.objects.filter(inf_study_drug__infant_visit__appointment__registered_subject__subject_identifier=inf_study_drug.infant_visit.appointment.registered_subject.subject_identifier, dose_status='New')
            if check_drugs and check_drugs[0].inf_study_drug.infant_visit.appointment.visit_definition.code != visit_code:
                raise forms.ValidationError('Study Drug has already been initiated at {}. Please correct.'.format(check_drugs[0].inf_study_drug.infant_visit.appointment.visit_definition.code))
            # Ensure start date is not before randomization

            if cleaned_data.get('ingestion_date') < rando_date:
                raise forms.ValidationError('Study initiation date CANNOT be before randomization date.')
        # Ensure cannot discontinue study drug more than once
        if cleaned_data.get('dose_status') == 'Permanently discontinued':
            check_drugs = InfantStudyDrugItems.objects.filter(inf_study_drug__infant_visit__appointment__registered_subject__subject_identifier=inf_study_drug.infant_visit.appointment.registered_subject.subject_identifier, dose_status='Permanently discontinued')
            if check_drugs and check_drugs[0].inf_study_drug.infant_visit.appointment.visit_definition.code != visit_code:
                raise forms.ValidationError('Study Drug has already been discontinued at {}. Please correct.'.format(check_drugs[0].inf_study_drug.infant_visit.appointment.visit_definition.code))
        return super(InfantStudyDrugItemsForm, self).clean()

    class Meta:
        model = InfantStudyDrugItems


class InfantStudyDrugInitForm(BaseInfantModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('infant_visit'):
            raise forms.ValidationError('This field is required. Please fill it in.')

        # Validate initiation date and wether infant was indicated to start drug
        if cleaned_data.get('initiated') == 'No' and cleaned_data.get('first_dose_date'):
            raise forms.ValidationError("You indicated that Study Drug was not initiated yet you provided an initiation date. Please correct.")
        if cleaned_data.get('initiated') == 'Yes' and not cleaned_data.get('first_dose_date'):
            raise forms.ValidationError("You indicated that Study Drug was initiated yet you did not provide the initiation date. Please correct.")

        # Ensure that reason not initiated is filled if study drug not initiated and vice versa
        if cleaned_data.get('initiated') == 'Yes' and cleaned_data.get('reason_not_init')!= 'N/A':
            raise forms.ValidationError("You indicated that Study Drug was initiated. Reason not initiated should be 'Not Applicable.' Please correct.")
        if cleaned_data.get('initiated') == 'No' and cleaned_data.get('reason_not_init') == 'N/A':
            raise forms.ValidationError("You indicated that Study Drug was NOT initiated. Reason not initiated cannot be 'Not Applicable.' Please provide a reason.")

        # Validate against form MP011
        study_drug = InfantStudyDrug.objects.filter(infant_visit = cleaned_data.get('infant_visit'))
        study_drug_items = InfantStudyDrugItems.objects.filter(inf_study_drug=study_drug)
        if study_drug:
            if study_drug[0].drug_status == 'Starting CTX/Placebo today' and cleaned_data.get('initiated') == 'No':
                raise forms.ValidationError("You indicated that Study Drug was being initiated on {}. Please correct".format(study_drug[0]._meta.verbose_name))
            if study_drug[0].drug_status == 'Never started' or study_drug[0].drug_status =='No modification':
                if cleaned_data.get('initiated') == 'Yes':
                    raise forms.ValidationError("You indicated that Study Drug was Not being initiated on {}. Please correct".format(study_drug[0]._meta.verbose_name))
        if study_drug_items:
            if study_drug_items[0].ingestion_date != cleaned_data.get('first_dose_date'):
                if study_drug_items[0].dose_status=='New':
                    raise forms.ValidationError("You indicated that Study Drug initiation date was {0}, yet indicated {1} on {2}. Please correct"
                                                .format(cleaned_data.get('first_dose_date'), study_drug_items[0].ingestion_date,study_drug_items[0]._meta.verbose_name))
        #Ensure first dose date is not before randomization date
        rando_date = cleaned_data.get('infant_visit').appointment.registered_subject.randomization_datetime.date()
        if cleaned_data.get('first_dose_date') and cleaned_data.get('first_dose_date') < rando_date:
            raise forms.ValidationError('First dose date cannot be before randomization date. Please correct.')
        return super(InfantStudyDrugInitForm, self).clean()

    class Meta:
        model = InfantStudyDrugInit
