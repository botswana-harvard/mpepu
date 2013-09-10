from django import forms
from django.contrib.auth.models import Group
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer
from bhp_base_form.forms import BaseModelForm
from bhp_data_manager.models import ActionItem


class ActionItemForm(BaseModelForm):

    action_group = forms.ChoiceField(
        label='Action group',
        choices=[(item.get('name'), ' '.join(item.get('name').split('_'))) for item in Group.objects.values('name').all()] + [('no group', '<no group>')],
        help_text='You can only select a group to which you belong. Choices are based on Groups defined in Auth.',
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer))

    class Meta:
        model = ActionItem
