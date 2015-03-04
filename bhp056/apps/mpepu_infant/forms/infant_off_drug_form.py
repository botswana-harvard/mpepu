from datetime import datetime
from django import forms
from django.db.models import Min, Max
from apps.mpepu_infant.models import InfantVisit, InfantOffDrug, InfantStudyDrugItems
from .base_infant_model_form import BaseInfantModelForm


class InfantOffDrugForm (BaseInfantModelForm):

    def clean(self):
        cleaned_data = super(InfantOffDrugForm, self).clean()
        # confirm last_dose_date falls between visit date going off drug and the previous visit date
        last_dose_date = cleaned_data.get('last_dose_date')
        #validating unkeyed dose data
        if not last_dose_date:
            raise forms.ValidationError('Please key in the last_dose_date')

        subject_identifier = cleaned_data.get('registered_subject').subject_identifier
#         last_dose_datetime = datetime(last_dose_date.year, last_dose_date.month, last_dose_date.day)

        # is infant onstuy offdrug
        off_drug_visit_datetime = InfantVisit.objects.filter(
            appointment__registered_subject__subject_identifier=subject_identifier,
            study_status='onstudy rando offdrug').aggregate(Min('report_datetime'))
        missed_2150_visit = InfantVisit.objects.filter(
            appointment__registered_subject__subject_identifier=subject_identifier, 
            reason='missed', appointment__visit_definition__code='2150')
        if not off_drug_visit_datetime['report_datetime__min']:
            off_drug_visit_datetime = InfantVisit.objects.filter(
                appointment__registered_subject__subject_identifier=subject_identifier,
                study_status='offstudy').aggregate(Min('report_datetime'))
#         if not off_drug_visit_datetime['report_datetime__min']:
#             raise forms.ValidationError('Cannot take off-drug. No visit found for reason \'off study\' or \' on study , off drug\'')
        previous_visit_datetime = InfantVisit.objects.filter(
            report_datetime__lt=off_drug_visit_datetime['report_datetime__min'],
            appointment__registered_subject__subject_identifier=subject_identifier).aggregate(Max('report_datetime'))
#         if last_dose_datetime < previous_visit_datetime['report_datetime__max'] and not missed_2150_visit:
#             raise forms.ValidationError('Last dose date must be greater than or equal to report date of last visit before going off drug ({0}). '
#                                         'Got {1}'.format(previous_visit_datetime['report_datetime__max'].strftime('%Y-%m-%d'), last_dose_datetime.strftime('%Y-%m-%d')))
#         if last_dose_datetime > off_drug_visit_datetime['report_datetime__min']:
#             raise forms.ValidationError('Last dose date must be less than or equal to report date of visit where subject is going off drug ({0}). '
#                                         'Got {1}'.format(off_drug_visit_datetime['report_datetime__min'].strftime('%Y-%m-%d'), last_dose_datetime.strftime('%Y-%m-%d')))
        # Ensure study drug dicontinuation indicated on StudyDrugRecord
        drug_record = (InfantStudyDrugItems.objects.filter
                            (inf_study_drug__infant_visit__appointment__registered_subject=
                             cleaned_data.get('registered_subject'), dose_status='Permanently discontinued'))
        if not drug_record:
            raise forms.ValidationError('Discontinuation of study drug has not been indicated on the Study Drug Record.'
                                        ' Please enter it either at this visit or the previuos visit.')

        return cleaned_data

    class Meta:
        model = InfantOffDrug
