from django.core.exceptions import ValidationError

from edc.subject.consent.forms import BaseConsentedModelForm

from ..models import ArvResistanceDiscontinuation

class ArvDiscontinuationForm(BaseConsentedModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        #
        if cleaned_data.get('stopped_once')=='Yes' and not cleaned_data.get('last_arv_date'):
            raise ValidationError('You indicated that antiretrovirals were stopped. Please provide a date')
        if cleaned_data.get('stopped_once')=='No' and cleaned_data.get('last_arv_date'):
            raise ValidationError('You indicated that antiretrovirals were not stopped without a tail yet you provided a date. Please correct')
        if cleaned_data.get('stopped_once')=='Yes' and cleaned_data.get('last_ftc_date') or cleaned_data.get('last_tdf_date') or cleaned_data.get('last_3tc_date'):
            raise ValidationError('You indicated that antiretrovitals were stopped all at once. Please correct. ')
        
        return super(ArvDiscontinuationForm, self).clean()
    
    class Meta:
        model = ArvResistanceDiscontinuation