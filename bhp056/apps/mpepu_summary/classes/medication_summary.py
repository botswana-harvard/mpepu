from edc.subject.registration.models import RegisteredSubject

from apps.mpepu_infant.models import InfantBirthFeed, InfantStudyDrugInit, InfantBirthArv, InfantStudyDrugItems, InfantFuMed, InfantFuNewMed, InfantArvProphMod


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

            # CTX / Placebo
            if InfantStudyDrugInit.objects.filter(infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier):
                infant_study_drug_init = InfantStudyDrugInit.objects.get(infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier)
                self.context['initiated'] = infant_study_drug_init.initiated
                self.context['first_dose_date'] = infant_study_drug_init.first_dose_date                
            if InfantStudyDrugItems.objects.filter(inf_study_drug__infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier):
                self.context['study_medications'] = InfantStudyDrugItems.objects.filter(inf_study_drug__infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier)
            else:
                self.context['study_medications']= None

            # AZT / NVP
            # supplied at dischare?
            if InfantBirthArv.objects.filter(infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier):
                infant_birth_arv = InfantBirthArv.objects.get(infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier)            
                self.context['azt_discharge_supply'] = infant_birth_arv.azt_discharge_supply                
                self.context['nvp_discharge_supply'] = infant_birth_arv.nvp_discharge_supply                                
            # record
            if InfantArvProphMod.objects.filter(infant_arv_proph__infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier):
                self.context['prophylaxis'] = InfantArvProphMod.objects.filter(infant_arv_proph__infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier)
            else:
                self.context['prophylaxis']= None

            # vaccinations
            # at birth
            if InfantBirthFeed.objects.filter(infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier):
                self.context['birth_vaccines'] = InfantBirthFeed.objects.filter(infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier).order_by('infant_visit__report_datetime')
            else:
                self.context['birth_vaccines']= None
            # during follow up    
            if InfantFuMed.objects.filter(infant_fu__infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier):
                self.context['vaccines'] = InfantFuMed.objects.filter(infant_fu__infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier).order_by('infant_fu__infant_visit__report_datetime')
            else:
                self.context['vaccines']= None


            if InfantFuNewMed.objects.filter(infant_fu__infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier):
                self.context['concomitant'] = InfantFuNewMed.objects.filter(infant_fu__infant_visit__appointment__registered_subject__subject_identifier__exact=self.subject_identifier).order_by('infant_fu__infant_visit__report_datetime')
            else:
                self.context['concomitant'] = None

