from django.db.models import Q, get_model
from django import forms
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer

from edc.subject.consent.forms import BaseConsentedModelForm

from ..choices import VISIT_INFO_SOURCE, VISIT_REASON
from ..models import MaternalVisit


class MaternalVisitForm (BaseConsentedModelForm):

    """Based on model visit.

    Attributes reason and info_source override those from the base model so that
    the choices can be custom for this app.
    """

    reason = forms.ChoiceField(
        label='Reason for visit',
        choices=[choice for choice in VISIT_REASON],
        help_text="If 'unscheduled', information is usually reported at the next scheduled visit, but exceptions may arise",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer),
        )
    info_source = forms.ChoiceField(
        label='Source of information',
        choices=[choice for choice in VISIT_INFO_SOURCE],
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer),
        )

    def clean(self):

        cleaned_data = self.cleaned_data

        """validate data"""
        if not cleaned_data.get('report_datetime'):
            raise forms.ValidationError('This field is required. Please fill it in')
        if cleaned_data.get('reason') == 'deferred':
            raise forms.ValidationError('Reason \'deferred\' is not valid for maternal visits. Please correct.')
        if cleaned_data.get('reason') == 'missed' and not cleaned_data.get('reason_missed'):
            raise forms.ValidationError('Please provide the reason the scheduled visit was missed')
        if cleaned_data.get('reason') != 'missed' and cleaned_data.get('reason_missed'):
            raise forms.ValidationError("Reason for visit is NOT 'missed' but you provided a reason missed. Please correct.")
        if cleaned_data.get('info_source') == 'OTHER' and not cleaned_data.get('info_source_other'):
            raise forms.ValidationError("Source of information is 'OTHER', please provide details below your choice")
        if cleaned_data.get('vital status') and not cleaned_data.get('survival_status') and not cleaned_data.get('date_last_alive'):
            raise forms.ValidationError("Visit reason is 'Vital Status', please enter Survival Status and Date Last Alive.")

        cleaned_data = super(MaternalVisitForm, self).clean()

        return cleaned_data

    class Meta:
        model = MaternalVisit
