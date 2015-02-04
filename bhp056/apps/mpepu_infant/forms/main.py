from django import forms
from datetime import date

from edc.subject.adverse_event.forms import BaseInfantDeathForm
from edc.subject.consent.forms import BaseConsentedModelForm

from apps.mpepu_infant.models import (InfantDeath, InfantPrerandoLoss, InfantStudyDrugInit, InfantNvpAdherence,
                                      InfantSurvival, InfantArvProph, InfantArvProphMod, InfantHaart, InfantHaartMod,
                                      InfantCtxPlaceboAdh, InfantFeeding, InfantVerbalAutopsy, InfantVerbalAutopsyItems)
from .base_infant_model_form import BaseInfantModelForm


class InfantDeathForm (BaseInfantDeathForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('death_reason_hospitalized'):
            if 'specify' in cleaned_data.get('death_reason_hospitalized').name and not cleaned_data.get('death_reason_hospitalized_other'):
                raise forms.ValidationError('Please specify further details for the reason hospitalized.')

        if not cleaned_data.get('death_cause_info'):
            raise forms.ValidationError("This field is required. Please fill it in.")
        return super(InfantDeathForm, self).clean()

    class Meta:
        model = InfantDeath


class InfantPrerandoLossForm(BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if  not cleaned_data.get('registered_subject'):
            raise forms.ValidationError('This field is required. Please fill it in')
        return super(InfantPrerandoLossForm, self).clean()

    class Meta:
        model = InfantPrerandoLoss


# class InfantStudyDrugInitForm (forms.ModelForm):
# 
#     class Meta:
#         model = InfantStudyDrugInit


class InfantSurvivalForm (forms.ModelForm):

    class Meta:
        model = InfantSurvival


class InfantArvProphForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        arv_status = cleaned_data.get('arv_status')
        check_mod = self.data.get('infantarvprophmod_set-0-arv_code')

        if not cleaned_data.get('infant_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')

        if cleaned_data.get('prophylatic_nvp') == 'No':
            if arv_status == 'no_mod' or 'arv_status' == 'modified':
                raise forms.ValidationError("You have indicated that the infant is not on NVP yet the status is ' %s. Please correct'"
                                        % arv_status)

        if cleaned_data.get('arv_status') == 'start' or cleaned_data.get('arv_status') == 'modified':
            if not check_mod:
                raise forms.ValidationError('Please fill in the NVP/AZT Prop modification form as it is required or change the arv status.')

        # if baby is not supposed to be on prophylactic NVP,then the InfantNvpAdherence is not required """
        # if infant had no diarrheal illness, InfantFuD is not required """
        if cleaned_data.get('prophylatic_nvp') == 'No':
            if InfantNvpAdherence.objects.filter(infant_visit=cleaned_data.get('infant_visit')).exists():
                forms.ValidationError("NVP data is available, You wrote 'infant was not supposed to be on NVP. "
                                      "Please correct '%s' first." % InfantNvpAdherence._meta.verbose_name)

        return super(InfantArvProphForm, self).clean()

    class Meta:
        model = InfantArvProph


class InfantArvProphModForm (forms.ModelForm):
    def clean(self):
        cleaned_data = super(InfantArvProphModForm, self).clean()
        infant_arv_proph = cleaned_data.get('infant_arv_proph')
        if infant_arv_proph.arv_status == 'N/A' or infant_arv_proph.arv_status == 'never started':
            if cleaned_data.get('arv_code'):
                raise forms.ValidationError('You cannot fill in NVP/AZT Proph modification form with the arv status you chose. Please correct.')
        # Ensure cannot enter discountinuation for the same arv more than once
        if cleaned_data.get('dose_status') == 'Permanently discontinued':
            check_arvs = InfantArvProphMod.objects.filter(arv_code=cleaned_data.get('arv_code'), 
                    dose_status='Permanently discontinued', infant_arv_proph__infant_visit__subject_identifier=cleaned_data.get('infant_arv_proph').infant_visit.subject_identifier)
            if check_arvs:
                raise forms.ValidationError('You cannot indicate "Permanently discontinued" for {} as it has already been discontinued at {}'
                                            .format(cleaned_data.get('arv_code'), check_arvs[0].infant_arv_proph.infant_visit.appointment.visit_definition.code))
        return cleaned_data

    class Meta:
        model = InfantArvProphMod


class InfantHaartForm (forms.ModelForm):

    class Meta:
        model = InfantHaart


class InfantHaartModForm (forms.ModelForm):

    class Meta:
        model = InfantHaartMod


class InfantNvpAdherenceForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('infant_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')

        if cleaned_data.get('days_missed') > 0 and not cleaned_data.get('reason_missed'):
            raise forms.ValidationError('You indicated that days of NVP were missed. Please provide a reason.')

        if cleaned_data.get('days_missed') == 0 and cleaned_data.get('reason_missed') is not None:
            raise forms.ValidationError('You indicated that no entire days of NVP were missed and provided a reason missed. Please correct.')

        return super(InfantNvpAdherenceForm, self).clean()

    class Meta:
        model = InfantNvpAdherence


class InfantCtxPlaceboAdhForm (BaseInfantModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('infant_visit'):
            raise forms.ValidationError('This field is required. Please fill it in')
        # ensuring that when no drug is missed that reason becomes N/A
        if cleaned_data.get('day_missed_drug') == 0 and cleaned_data.get('reason_missed') != 'N/A':
            raise forms.ValidationError('if no entire days where missed, your reason missed should be NOT APPLICABLE')
    # When days missed are greater than zero, other options other than N/A should be selected
        if cleaned_data.get('day_missed_drug') > 0 and cleaned_data.get('reason_missed') == 'N/A':
            raise forms.ValidationError('if days missed is greater than zero, reason misssed cannot be N/A')
    # validating that other,specify is given if other reason is selected
        if cleaned_data.get('reason_missed') == 'OTHER' and not cleaned_data.get('reason_missed_other'):
            raise forms.ValidationError('If reason missed is other, please specify the reason in field provided')
        return super(InfantCtxPlaceboAdhForm, self).clean()

    class Meta:
        model = InfantCtxPlaceboAdh


class InfantFeedingForm (BaseInfantModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        visit = cleaned_data.get('infant_visit')

        # validating that the weaning date is not greater than the visit/today's date
        if cleaned_data.get('formula_date') and visit:
            if cleaned_data.get('formula_date') > visit.report_datetime.date():
                raise forms.ValidationError('Date participant first received formula milk cannot be greater than today\'s date. Please correct.')
            if cleaned_data.get('formula_date') < visit.appointment.registered_subject.dob:
                raise forms.ValidationError('Date participant first received formula milk cannot be less than the date of birth of {}'.format(visit.appointment.registered_subject.dob))
        if cleaned_data.get('most_recent_bm') and visit:
            if cleaned_data.get('most_recent_bm') > visit.report_datetime.date():
                raise forms.ValidationError('The most recent breast feeding date cannot be greater than today\'s date. Please correct.')
            if cleaned_data.get('most_recent_bm') < visit.appointment.registered_subject.dob:
                raise forms.ValidationError('The most recent breast feeding date cannot be less than the date of birth of {}'.format(visit.appointment.registered_subject.dob))

        # infants should either be FF or BF they cannot be neither
        if cleaned_data.get('other_feeding', None) != 'Yes' and cleaned_data.get('ever_breastfeed', None) != 'Yes':
            raise forms.ValidationError('Its impossible for infant to neither FF/liquids/BF. Infant has to either formula feed (2) or breast feed (8) Please correct')

        # Other feeding validaions
        if cleaned_data.get('other_feeding') == 'No':
            if cleaned_data.get('juice') == 'Yes':
                raise forms.ValidationError("You indicated that infant has not received other foods or liquids other than breast milk(Q3) and yet selected infant received juice. Please correct")
            if cleaned_data.get('cow_milk') == 'Yes':
                raise forms.ValidationError("You indicated that infant has not received other foods or liquids other than breast milk(Q3) and yet selected infant received cows milk. Please correct")
            if cleaned_data.get('other_milk') == 'Yes':
                raise forms.ValidationError("You indicated that infant has not received other foods or liquids other than breast milk(Q3) and yet selected infant received other animal milk. Please correct")
            if cleaned_data.get('fruits_veg') == 'Yes':
                raise forms.ValidationError("You indicated that infant has not received other foods or liquids other than breast milk(Q3) and yet selected infant received fruits and veggies. Please correct")
            if cleaned_data.get('cereal_porridge') == 'Yes':
                raise forms.ValidationError("You indicated that infant has not received other foods or liquids other than breast milk(Q3) and yet selected infant received cereal and porridge. Please correct")
            if cleaned_data.get('solid_liquid') == 'Yes':
                raise forms.ValidationError("You indicated that infant has not received other foods or liquids other than breast milk(Q3) and yet selected infant received cereal and porridge. Please correct")
            if cleaned_data.get('rehydration_salts') == 'Yes':
                raise forms.ValidationError("You indicated that infant has not received other foods or liquids other than breast milk(Q3) and yet selected infant received rehydration salts. Please correct")
        if cleaned_data.get('other_feeding') == 'Yes':
            if (cleaned_data.get('juice') == 'No' and cleaned_data.get('cow_milk') == 'No' 
                and cleaned_data.get('other_milk') == 'No' and cleaned_data.get('fruits_veg') == 'No' 
                and cleaned_data.get('cereal_porridge') == 'No' and cleaned_data.get('solid_liquid') == 'No'):
                raise forms.ValidationError('You indicated that infant has received other foods or liquids yet did NOT indicate any solids or liquids received.')
        return super(InfantFeedingForm, self).clean()

    class Meta:
        model = InfantFeeding


class InfantVerbalAutopsyForm (BaseInfantModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        check_items = self.data.get('infantverbalautopsyitems_set-0-sign_symptom')
        if  not cleaned_data.get('registered_subject'):
            raise forms.ValidationError('This field is required. Please fill it in')
        #
        if cleaned_data.get('sign_symptoms') =='Yes' and not check_items:
            raise forms.ValidationError('You indicated that there were signs and symptoms. Please provide them.')
        return super(InfantVerbalAutopsyForm, self).clean()

    class Meta:
        model = InfantVerbalAutopsy


class InfantVerbalAutopsyItemsForm(BaseInfantModelForm):
    def clean(self):
        cleaned_data = super(InfantVerbalAutopsyItemsForm, self).clean()
        verbal_autopsy = cleaned_data.get('verbal_autopsy')

        if verbal_autopsy.sign_symptoms == 'No':
            raise forms.ValidationError('You answered that the participant did not experience any sign or symptoms, yet you listed them. Please correct.')
        return cleaned_data

    class Meta:
        model = InfantVerbalAutopsyItems
