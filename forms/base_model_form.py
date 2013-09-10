import re
from django import forms
from django.db.models.query import QuerySet
from django.conf import settings
from django.db.models import OneToOneField, ForeignKey, get_model
from bhp_visit_tracking.models import BaseVisitTracking
from bhp_base_form.classes import LogicCheck


class BaseModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseModelForm, self).__init__(*args, **kwargs)
        self.logic = LogicCheck(self._meta.model)
        # if in admin edit mode, populate visit model's queryset
        # if not in admin, e.g. coming from the dashboard, might
        # throw an exception.
        if self.instance:
            if 'get_visit' in dir(self.instance):
                try:
                    # but if self.instance.maternal_visit DoesNotExist, will throw an exception
                    # when get_visit() is called
                    if self.instance.get_visit():
                        try:
                            attr = self.instance.get_visit()._meta.object_name.lower()
                            self.fields[attr].queryset = self.instance.get_visit().__class__.objects.filter(pk=self.instance.get_visit().pk)
                        except KeyError:
                            pass
                except:
                    pass
        # if in admin edit mode, populate registered_subject's queryset
        if 'registered_subject' in self.fields:
            try:
                if 'registered_subject' in dir(self.instance):
                        if self.instance.registered_subject:
                            self.fields['registered_subject'].queryset = self.instance.registered_subject.__class__.objects.filter(pk=self.instance.registered_subject.pk)
                else:
                    self.fields['registered_subject'].queryset = self.instance.registered_subject.__class__.objects.none()
            except:
                if 'registered_subject' not in self.initial and 'registered_subject' not in self.data:
                    RegisteredSubject = get_model('bhp_registration', 'RegisteredSubject')
                    self.fields['registered_subject'].queryset = RegisteredSubject.objects.none()

    def get_subject_identifier(self, cleaned_data):
        subject_identifier = None
        if 'subject_identifier' in cleaned_data:
            subject_identifier = cleaned_data.get('subject_identifier')
        if not subject_identifier:
            if 'registered_subject' in cleaned_data:
                subject_identifier = cleaned_data.get('registered_subject').subject_identifier
        if not subject_identifier:
            # look for a visit model field
            for field in self._meta.model._meta.fields:
                if isinstance(field, (OneToOneField, ForeignKey)):
                    if isinstance(field.rel.to, BaseVisitTracking):
                        attrname = field.attrname
                        visit = cleaned_data.get(attrname, None)
                        if visit:
                            subject_identifier = visit.get_subject_identifier()
        return subject_identifier

    def clean(self):
        """Calls crypto clean methods, OTHER/Specify and some functionality for bhp_dispatch."""
        cleaned_data = self.cleaned_data
        # check if dispatched
        if 'bhp_dispatch' in settings.INSTALLED_APPS:
            if 'is_dispatched' in dir(self._meta.model()):
                if self._meta.model().is_dispatched:
                    raise forms.ValidationError('Cannot update. Form is currently dispatched')
        # encrypted fields may have their own validation code to run.
        # See the custom field objects in bhp_crypto.
        try:
            from bhp_crypto.fields import BaseEncryptedField
            for field in self._meta.model._meta.fields:
                if isinstance(field, BaseEncryptedField):
                    field.validate_with_cleaned_data(field.attname, cleaned_data)
        except ImportError:
            pass
        # check for OTHER in choices tuples, if selected, should have a value on Other specify.
        other = []
        [other.append(k) for k in cleaned_data.iterkeys() if cleaned_data.get(k, None) in ['other', 'Other', 'OTHER']]
        for k in other:
            if '{0}_other'.format(k) in cleaned_data:
                if not cleaned_data.get('{0}_other'.format(k)):
                    raise forms.ValidationError('If {0} is \'OTHER\', please specify. '
                                                'You wrote \'{1}\''.format(k, cleaned_data['{0}_other'.format(k)]))
        # m2m with OTHER
        self.check_for_other_in_m2m(cleaned_data)
        return super(BaseModelForm, self).clean()

    def check_for_other_in_m2m(self, cleaned_data):
        """Raises ValidtionError for an m2m if it cannot confirm \'Other Specify\' is paired with a value in a following \'other\' field."""
        for field_name, field_value in cleaned_data.iteritems():
            self.check_for_value_in_m2m(cleaned_data, field_name, field_value, '{0}_other'.format(field_name), ['specify', 'explain'], 'other')
#             if isinstance(value, QuerySet):
#                 words = ['specify', 'explain']
#                 answers = [l.name.lower() for l in cleaned_data.get(key, [])]
#                 if answers:
#                     for ans in answers:
#                         if any([word in ans for word in words]) and 'other' in ans.lower():
#                             if not cleaned_data.get('{0}_other'.format(key), None):
#                                 raise forms.ValidationError('You have selected \'{0}\' as an answer for {1}. Please specify.'.format(ans, key))

    def check_for_value_in_m2m(self, cleaned_data, m2m_name, m2m_qs, optional_field_name, optional_words, required_word=None):
        """Raises ValidtionError for an m2m if it cannot confirm \'Other Specify\' is paired with a value in a following \'other\' field."""
        if not required_word:
            required_word = ''
        if isinstance(m2m_qs, QuerySet):
            answers = [l.name.lower() for l in cleaned_data.get(m2m_name, [])]
            if answers:
                for ans in answers:
                    if any([word in ans for word in optional_words]) and required_word in ans.lower():
                        if not cleaned_data.get(optional_field_name, None):
                            raise forms.ValidationError('You have selected \'{0}\' as an answer for {1}. Please specify in {2}.'.format(ans, m2m_name, optional_field_name))

    # TODO: is this method used??
    def validate_m2m(self, **kwargs):
        """Validates at form level a triplet of questions lead by a Yes/No for a many to many with other specify.

            * The first question is a Yes/No question indicating if any items in the many to many will be selected
            * The second question is a many to many (select all that apply)
            * The third is an 'Other Specify' to be completed if an 'Other' item was selected in the many to many question

            Be sure to check cleaned_data for the 'key' of the m2m field first.

            For example, in the ModelForm clean() method call::

                if cleaned_data.has_key('chronic_cond'):
                    self.validate_m2m(
                            label = 'chronic condition',
                            yesno = cleaned_data['has_chronic_cond'],
                            m2m = cleaned_data['chronic_cond'],
                            other = cleaned_data['chronic_cond_other'])
        """
        label = kwargs.get('label', 'items to be selected')
        leading = kwargs.get('leading')
        m2m = kwargs.get('m2m')
        other = kwargs.get('other')

        # if leading question is 'Yes', a m2m item cannot be 'Not applicable'
        if leading.lower() == 'yes' and [True for item in m2m if item.name.lower() == 'not applicable']:
            raise forms.ValidationError("You stated there ARE " + label + "s, yet you selected '{0}'".format(item.name))

        # if leading question is 'No', ensure the m2m item is 'not applicable'
        if leading.lower() == 'no' and not [True for item in m2m if item.name.lower() == 'not applicable']:
            raise forms.ValidationError("You stated there are NO {0}s. Please correct".format(label))

        # if leading question is 'No', ensure only one m2m item is selected.
        if leading.lower() == 'no' and len(m2m) > 1:
            raise forms.ValidationError("You stated there are NO {0}s. Please correct".format(label))

        # if leading question is 'Yes' and an m2m item is 'other, specify', ensure 'other' attribute has a value
        if leading.lower() == 'yes' and not other and [True for item in m2m if 'other' in item.name.lower()]:
            raise forms.ValidationError("You have selected a '{0}' as 'Other', please specify.".format(label))

        # if 'other' has a value but no m2m item is 'Other, specify'
        if other and not [True for item in m2m if 'other' in item.name.lower()]:
            raise forms.ValidationError("You have specified an 'Other' {0} but not selected 'Other, specify'. Please correct.".format(label))

    def options_in_tuple(self, choices, options):
        """Confirms options exist in choices tuple."""
        if not isinstance(choices, tuple):
            raise TypeError('Parameter \'choices\' must be a tuple.')
        if not isinstance(options, list):
            raise TypeError('Parameter \'options\' must be a list.')
        choices = list(choices)
        choices.sort()
        lst = list(set(list(options) + choices))
        lst.sort()
        if not lst == choices:
            raise TypeError('Options {0} are not in choices tuple {1}. Has the choices tuple changed?'.format(options, choices))

    def verify_tuples(self):
        """Override to verify tuple values referenced in the valifation checks.

        For example, validation checks refer to values from these choices::
            options = ['Yes', 'No', 'not sure', 'Don\'t want to answer']
            self.options_in_tuple(YES_NO_UNSURE, options)
            self.options_in_tuple(FIRSTPARTNERHIV_CHOICE, ['negative', 'I am not sure'])
        """
        pass
