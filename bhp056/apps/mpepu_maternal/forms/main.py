from django import forms

from base_maternal_model_form import BaseMaternalModelForm

from ..models import MaternalDeath, MaternalLocator


class MaternalDeathForm (BaseMaternalModelForm):

    class Meta:
        model = MaternalDeath


class MaternalLocatorForm (BaseMaternalModelForm):
    def clean(self):
        cleaned_data = super(MaternalLocatorForm, self).clean()

        if cleaned_data.get('home_visit_permission') == 'Yes' and not cleaned_data.get('physical_address'):
            raise forms.ValidationError('You indicated that participant consented to for home visits. Please provide physical address.')

        if cleaned_data.get('may_follow_up') == 'Yes' or cleaned_data.get('may_sms_follow_up') == 'Yes':
            if not cleaned_data.get('subject_cell'):
                raise forms.ValidationError('You indicated that participant consented to phonecall/sms followup. Please provide cell number.')

        if cleaned_data.get('may_call_work') == 'Yes' and not cleaned_data.get('subject_work_place'):
            raise forms.ValidationError('You indicated that participant consented to being contacted at work. Please provide work details.')

        if cleaned_data.get('may_contact_someone') == 'Yes':
            if not cleaned_data.get('contact_name') or not cleaned_data.get('contact_rel') or not cleaned_data.get('contact_physical_address'):
                raise forms.ValidationError('You indicated that participant consented to contacting another person for followup. Please provide full details.')

        if cleaned_data.get('has_caretaker_alt') == 'Yes' and not cleaned_data.get('caretaker_name'):
            raise forms.ValidationError('You indicated that participant has identified an alternate caretaker in case of death. Please provide full details.')

        return cleaned_data

    class Meta:
        model = MaternalLocator
