import re
from django import forms
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer
from apps.mpepu_infant.choices import VISIT_INFO_SOURCE, VISIT_REASON
from apps.mpepu_infant.models import InfantVisit, InfantBirth
from .base_infant_model_form import BaseInfantModelForm


class InfantVisitForm (BaseInfantModelForm):

    """Based on model maternal_visit.

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

        cleaned_data = super(InfantVisitForm, self).clean()
        """validate data"""
        if cleaned_data.get('reason') == 'deferred':
            if cleaned_data.get('appointment').visit_definition.code != '2010':
                raise forms.ValidationError('Reason \'deferred\' may only be used on visit 2010. Please correct.')
        if cleaned_data['reason'] == 'missed' and not cleaned_data['reason_missed']:
            raise forms.ValidationError('Please provide the reason the scheduled visit was missed')
        if cleaned_data['reason'] != 'missed' and cleaned_data['reason_missed']:
            raise forms.ValidationError("Reason for visit is NOT 'missed' but you provided a reason missed. Please correct.")
        if cleaned_data['info_source'] == 'OTHER' and not cleaned_data['info_source_other']:
            raise forms.ValidationError("Source of information is 'OTHER', please provide details below your choice")

        if cleaned_data['survival_status'] == 'DEAD' and not cleaned_data['date_last_alive']:
            raise forms.ValidationError('Please provide date information, when infant was last known to be alive')

        # check study status
        study_status_display = [choice[1] for choice in InfantVisit._meta.get_field('study_status').choices if choice[0] == cleaned_data['study_status']]
        if re.search('onstudy', cleaned_data['study_status']):
            registered_subject = cleaned_data['appointment'].registered_subject
            # check birth
            if not InfantBirth.objects.filter(registered_subject=registered_subject):
                # not born, cannot be on study
                raise forms.ValidationError("Study status cannot be 'On Study'. Infant Birth Record not available. You wrote %s" % study_status_display)
            elif re.search('drug', cleaned_data['study_status']):
                if not registered_subject.sid:
                    # not on drug, etc because has not rando'ed
                    raise forms.ValidationError("Infant has not yet randomized. Study status cannot be 'On Drug', 'Off Drug' or 'Not Yet Started Drug'. You wrote %s" % study_status_display)
            elif re.search('notrando', cleaned_data['study_status']):
                if registered_subject.sid:
                    # is rando'ed, so no...
                    raise forms.ValidationError("Infant is randomized. Please choose the correct study status. You wrote %s" % study_status_display)
        return cleaned_data

    class Meta:
        model = InfantVisit
