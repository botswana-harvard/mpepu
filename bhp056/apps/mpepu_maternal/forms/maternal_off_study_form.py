from django import forms
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer
from bhp_off_study.forms import BaseOffStudyForm
from mpepu_maternal.choices import OFF_STUDY_REASON
from mpepu_maternal.models import MaternalOffStudy


class MaternalOffStudyForm (BaseOffStudyForm):

    reason = forms.ChoiceField(
        label='Please code the primary reason participant taken off-study',
        choices=[choice for choice in OFF_STUDY_REASON],
        help_text="",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer),
        )

    class Meta:
        model = MaternalOffStudy
