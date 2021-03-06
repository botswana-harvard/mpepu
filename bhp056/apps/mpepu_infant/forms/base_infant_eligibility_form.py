from django.db.models import get_model
from django import forms

from edc.subject.consent.classes import ConsentHelper
from edc.subject.registration.models import RegisteredSubject

from apps.mpepu_infant_rando.classes import Eligibility

from .base_infant_model_form import BaseInfantModelForm
from ..models import InfantEligibility


class BaseInfantEligibilityForm (BaseInfantModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        if  not cleaned_data.get('registered_subject'):
            raise forms.ValidationError('This field is required. Please fill it in')
        if not cleaned_data.get('registered_subject').subject_identifier:
            raise forms.ValidationError('Randomization failed. Cannot determine subject_identifier from RegisteredSubject table. Contact the Data Manager.')
        if not cleaned_data.get('registered_subject').dob:
            raise forms.ValidationError('Randomization failed. Cannot determine dob from RegisteredSubject table. Contact the Data Manager.')
        if not cleaned_data.get('registered_subject').relative_identifier:
            raise forms.ValidationError('Randomization failed. Cannot determine maternal subject-identifier from RegisteredSubject table. Contact the Data Manager.')
        registered_subject = cleaned_data.get('registered_subject')
        current_consent_version = ConsentHelper(self._meta.model(**cleaned_data), forms.ValidationError).validate_versioned_fields()
        if not current_consent_version:
            raise forms.ValidationError('Randomization failed. Cannot determine version of the maternal consent. Contact the Data Manager.')
        dob = registered_subject.dob

        weight = None
        if 'weight' in cleaned_data:
            weight = cleaned_data.get('weight', None)

        clinical_jaundice = None
        if 'clinical_jaundice' in cleaned_data:
            clinical_jaundice = cleaned_data.get('clinical_jaundice', None)

        anemia_neutropenia = None
        if 'anemia_neutropenia' in cleaned_data:
            anemia_neutropenia = cleaned_data.get('anemia_neutropenia', None)

        MaternalLabDel = get_model('mpepu_maternal', 'MaternalLabDel')
        maternal_lab_del = MaternalLabDel.objects.get(maternal_visit__appointment__registered_subject__subject_identifier=registered_subject.relative_identifier)
        #if abs((date.today() - dob).days) < 13:
        #    raise forms.ValidationError('Randomization failed. Infant must be 14 days of life or older to verify eligiblity.')
        allow_rando = Eligibility().check(
            current_consent_version=current_consent_version,
            dob=dob,
            ga=maternal_lab_del.ga,
            weight=weight,
            clinical_jaundice=clinical_jaundice,
            anemia_neutropenia=anemia_neutropenia,
            suppress_exception=self.suppress_eligibility_exception)
        return super(BaseInfantEligibilityForm, self).clean()
