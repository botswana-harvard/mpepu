from django import forms
from django.core.exceptions import ValidationError

from edc.subject.consent.forms import BaseSubjectConsentForm
from ..models import ResistanceDisc, ResistanceConsent, ResistanceEligibility, MaternalConsent
from .base_maternal_model_form import BaseMaternalModelForm
from edc.subject.consent.forms import BaseConsentedModelForm


class ResistanceConsentForm(BaseSubjectConsentForm):

    def clean(self):

        cleaned_data = self.cleaned_data
        maternal_consent = MaternalConsent.objects.filter(first_name=cleaned_data.get('first_name'), last_name=cleaned_data.get('last_name'), identity=cleaned_data.get('identity'))
        if not maternal_consent.exists():
            raise forms.ValidationError('Unable to locate Maternal Consent using the first_name, '
                                        'last_name and identity number provided. '
                                        'Enter the Maternal Consent first or check your criteria.')
        return cleaned_data

    class Meta:
        model = ResistanceConsent


class ResistanceEligibilityForm (BaseConsentedModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('lates_cd4') > 350:
            raise ValidationError('CD4 count is greater than 350, participant is INELIGIBLE')
        return super(ResistanceEligibilityForm, self).clean()

    class Meta:
        model = ResistanceEligibility


class ResistanceDiscForm(BaseMaternalModelForm):

    def clean(self):

        cleaned_data = self.cleaned_data

        if cleaned_data.get('stopped_once') == 'Yes' and not cleaned_data.get('last_arv_date'):
            raise ValidationError('You indicated that antiretrovirals were stopped. Please provide a date')
        if cleaned_data.get('stopped_once') == 'No' and cleaned_data.get('last_arv_date'):
            raise ValidationError('You indicated that antiretrovirals were not stopped without a tail yet you provided a date. Please correct')
        if cleaned_data.get('stopped_once') == 'Yes' and cleaned_data.get('last_ftc_date') or cleaned_data.get('last_tdf_date') or cleaned_data.get('last_3tc_date'):
            raise ValidationError('You indicated that antiretrovitals were stopped all at once. Please correct. ')

        return super(ResistanceDiscForm, self).clean()

    class Meta:
        model = ResistanceDisc
