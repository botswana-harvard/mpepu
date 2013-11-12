from django import forms

from edc.subject.consent.forms import BaseSubjectConsentForm

from apps.mpepu_maternal.models import MaternalConsent

from ..models import ArvResistanceConsent

class ArvResistanceConsentForm(BaseSubjectConsentForm):
    def clean(self):

        cleaned_data = self.cleaned_data
        if not MaternalConsent.objects.filter(first_name=cleaned_data.get('first_name'),
                                                     last_name=cleaned_data.get('last_name'),
                                                     identity=cleaned_data.get('identity')).exists():
            raise forms.ValidationError('Unable to locate Post Survey consent using the first_name, '
                                        'last_name and identity number provided. '
                                        'Enter the Post Survey consent first or check your criteria.')
        return cleaned_data

    class Meta:
        model = ArvResistanceConsent