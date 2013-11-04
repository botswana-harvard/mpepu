from edc.subject.registration.models import RegisteredSubject

from apps.mpepu_infant.models import InfantStudyDrugItems, InfantFuMed, InfantFuNewMed

class MedicationSummary(object):

    def __init__(self, **kwargs):
        self.context = {}
        self.subject_identifier = kwargs.get('subject_identifier')

        self.context['section_name'] = kwargs.get('section_name')
        self.context['search_name'] = kwargs.get('search_name')        
        self.context['template']  = 'medication_summary.html'
        self.context['subject_identifier'] = self.subject_identifier
        
        if self.subject_identifier:
            self.context['registered_subject'] = RegisteredSubject.objects.get(subject_identifier=self.subject_identifier)        
            if InfantStudyDrugItems.objects.filter(inf_study_drug__infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier):
                self.context['study_medications'] = InfantStudyDrugItems.objects.filter(inf_study_drug__infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier)
            else:
                self.context['study_medications']= None

            if InfantFuMed.objects.filter(infant_fu__infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier):
                self.context['vaccines'] = InfantFuMed.objects.filter(infant_fu__infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier).order_by('infant_fu__infant_visit__report_datetime')
            else:
                self.context['vaccines']= None

            if InfantFuNewMed.objects.filter(infant_fu__infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier):
                self.context['concomitant'] = InfantFuNewMed.objects.filter(infant_fu__infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier).order_by('infant_fu__infant_visit__report_datetime')
            else:
                self.context['concomitant'] = None

