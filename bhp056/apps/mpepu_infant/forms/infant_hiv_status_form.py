from django import forms
from mpepu_infant.models import InfantHivStatus
from base_infant_model_form import BaseInfantModelForm


class InfantHivStatusForm (BaseInfantModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data

        #validation for HIV positive result
        if cleaned_data.get('physical_exam_result', None) == 'POS' and not cleaned_data['date_first_pos']:
            raise forms.ValidationError("If patient HIV test is positive, when was the date of first +VE test?. You wrote '%s'" % cleaned_data.get('date_first_pos', None))

        if cleaned_data.get('infant_haart', None) == 'Yes' and not cleaned_data['infant_haart_date']:
            raise forms.ValidationError("If infant is on HAART, when did infant start HAART?. You wrote '%s'" % cleaned_data.get('date_first_pos', None))

        return super(InfantHivStatusForm, self).clean()

    class Meta:
        model = InfantHivStatus
