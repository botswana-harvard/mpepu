from django import forms

from apps.mpepu_infant.models import InfantPreEligibility

from .base_infant_eligibility_form import BaseInfantEligibilityForm


class InfantPreEligibilityForm (BaseInfantEligibilityForm):

    suppress_eligibility_exception = True

    def clean(self):
        cleaned_data = super(InfantPreEligibilityForm, self).clean()
        #Infant Pre Eligibility checks
        self.instance.pre_eligibility_checks(InfantPreEligibility(**cleaned_data), forms.ValidationError)
        return cleaned_data

    class Meta:
        model = InfantPreEligibility
