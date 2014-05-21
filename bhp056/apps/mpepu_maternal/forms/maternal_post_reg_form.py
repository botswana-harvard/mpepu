from django import forms

from apps.mpepu_infant_rando.models import InfantRando

from .base_maternal_model_form import BaseMaternalModelForm
from ..models import MaternalPostReg


class MaternalPostRegForm (BaseMaternalModelForm):
    def clean(self):

        cleaned_data = self.cleaned_data
        if not cleaned_data.get('registered_subject'):
            raise forms.ValidationError('This field is required. Please fill it in')

        registered_subject = cleaned_data.get('registered_subject', None)
        if registered_subject:
            if not registered_subject.__class__.objects.filter(relative_identifier=registered_subject.subject_identifier):
                raise forms.ValidationError('Maternal Post-Partum Registration cannot be submitted before Infant Birth Record.')
            if registered_subject.__class__.objects.filter(relative_identifier=registered_subject.subject_identifier):
                for rs in registered_subject.__class__.objects.filter(relative_identifier=registered_subject.subject_identifier):
                    if not InfantRando.objects.filter(subject_identifier=rs.subject_identifier):
                        raise forms.ValidationError('Maternal Post-Partum Registration cannot be submitted before Infant Randomization.')
        return super(MaternalPostRegForm, self).clean()

    class Meta:
        model = MaternalPostReg
