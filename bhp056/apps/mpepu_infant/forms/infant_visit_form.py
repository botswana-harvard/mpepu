import re
from django import forms
from django.db import models
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

        cleaned_data = self.cleaned_data
        """validate data"""
        if not cleaned_data.get('appointment'):
            raise forms.ValidationError('This field is required. please fill it in')
        if cleaned_data.get('reason') == 'deferred':
            if cleaned_data.get('appointment').visit_definition.code != '2010':
                raise forms.ValidationError('Reason \'deferred\' may only be used on visit 2010. Please correct.')
        if cleaned_data.get('reason') == 'missed' and not cleaned_data.get('reason_missed'):
            raise forms.ValidationError('Please provide the reason the scheduled visit was missed')
        if cleaned_data.get('reason') != 'missed' and cleaned_data.get('reason_missed'):
            raise forms.ValidationError("Reason for visit is NOT 'missed' but you provided a reason missed. Please correct.")
        if cleaned_data.get('info_source') == 'OTHER' and not cleaned_data.get('info_source_other'):
            raise forms.ValidationError("Source of information is 'OTHER', please provide details below your choice")

        if cleaned_data.get('survival_status') == 'DEAD' and not cleaned_data.get('date_last_alive'):
            raise forms.ValidationError('Please provide date information, when infant was last known to be alive')

        if cleaned_data.get('reason') == 'death' and cleaned_data.get('info_source') == 'telephone':
            raise forms.ValidationError("If visit reason is death, info source cannot be {}. Please select another info source or 'Other contact with participant (for example telephone call)' if it is telephone")

        # check study status
        study_status_display = [choice[1] for choice in InfantVisit._meta.get_field('study_status').choices if choice[0] == cleaned_data.get('study_status')]
        if re.search('onstudy', cleaned_data.get('study_status')):
            registered_subject = cleaned_data.get('appointment').registered_subject
            # check birth
            if not InfantBirth.objects.filter(registered_subject=registered_subject):
                # not born, cannot be on study
                raise forms.ValidationError("Study status cannot be 'On Study'. Infant Birth Record not available. You wrote %s" % study_status_display)
            elif re.search('drug', cleaned_data.get('study_status')):
                if not registered_subject.sid:
                    # not on drug, etc because has not rando'ed
                    raise forms.ValidationError("Infant has not yet randomized. Study status cannot be 'On Drug', 'Off Drug' or 'Not Yet Started Drug'. You wrote %s" % study_status_display)
            elif re.search('notrando', cleaned_data.get('study_status')):
                if registered_subject.sid:
                    # is rando'ed, so no...
                    raise forms.ValidationError("Infant is randomized. Please choose the correct study status. You wrote %s" % study_status_display)

        #validate that you cant save infant visit greater that 2000 if infant eligibility has not been filled in
        self.instance.requires_infant_eligibility(InfantVisit(**cleaned_data), forms.ValidationError)
        #Meta data validations
        self.instance.recalculate_meta(InfantVisit(**cleaned_data), forms.ValidationError)
        #validate that you cant save infant visit if previous visit has not been saved.
        self.instance.check_previous_visit_keyed(InfantVisit(**cleaned_data), forms.ValidationError)
        return super(InfantVisitForm, self).clean()

    class Meta:
        model = InfantVisit
