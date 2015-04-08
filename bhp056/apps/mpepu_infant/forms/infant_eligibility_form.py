from django import forms

from edc.subject.registration.models import RegisteredSubject

from apps.mpepu_infant.models import InfantEligibility

from .base_infant_eligibility_form import BaseInfantEligibilityForm


class InfantEligibilityForm (BaseInfantEligibilityForm):

    suppress_eligibility_exception = False

    def clean(self):
        raise forms.ValidationError('Randomization for this study has ceased.')

#         cleaned_data = super(InfantEligibilityForm, self).clean()
        #check that multiple births have the same information
#         infants = RegisteredSubject.objects.filter(relative_identifier=cleaned_data.get('registered_subject').relative_identifier)
#         if infants.count() > 1:
#             for infant in infants:
#                 eligibility = InfantEligibility.objects.filter(registered_subject=infant)
#                 if eligibility:
#                     if infant != cleaned_data.get('registered_subject'):
#                         if eligibility[0].maternal_art_status != cleaned_data.get('maternal_art_status'):
#                             raise forms.ValidationError("The maternal ART status is not identical for multiple birth infants. On '{0}' you indicated '{1}'. Please correct.".format(infant.subject_identifier,eligibility[0].maternal_art_status))
#                         if eligibility[0].maternal_feeding_choice != cleaned_data.get('maternal_feeding_choice'):
#                             raise forms.ValidationError("The maternal feeding choice is not identical for multiple birth infants. On '{0}' you indicated '{1}'. Please correct.".format(infant.subject_identifier,eligibility[0].maternal_feeding_choice))
#                         if eligibility[0].rando_bf_duration != cleaned_data.get('rando_bf_duration'):
#                             raise forms.ValidationError("The breast feeding randomization choice is not identical for mutliple birth infants. On '{0}' you indicated '{1}'. Please correct.".format(infant.subject_identifier,eligibility[0].rando_bf_duration))
#                         if eligibility[0].randomization_site != cleaned_data.get('randomization_site'):
#                             raise forms.ValidationError("The rando site is not identical for multiple birth infants. On '{0}' you indicated '{1}'.Please correct.".format(infant.subject_identifier,eligibility[0].randomization_site))
# 
#         if 'maternal_feeding_choice' in cleaned_data:
#             if not cleaned_data.get('rando_bf_duration'):
#                 raise forms.ValidationError('Breast Feeding duration cannot be None')
#             if cleaned_data.get('maternal_feeding_choice') == 'FF':
#                 if cleaned_data.get('rando_bf_duration') != 'N/A':
#                     raise forms.ValidationError("Feeding Choice is Formula Feeding. Breast Feeding duration should be 'Not Applicable'. Please correct.")
#             if cleaned_data.get('maternal_feeding_choice') == 'BF' and cleaned_data.get('rando_bf_duration') == 'N/A':
#                 raise forms.ValidationError("Breast Feeding duration cannot be 'Not Applicable' as you indicated Feeding Choice to be Breast Feeding.")

#         return cleaned_data

    class Meta:
        model = InfantEligibility
