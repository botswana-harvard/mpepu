from django.db import models


class MaternalArvManager(models.Manager):

    def get_by_natural_key(self, arv_code, modification_date, report_datetime, visit_instance, appt_status, visit_definition_code, subject_identifier_as_pk):
        MaternalVisit = models.get_model('mpepu_maternal', 'MaternalVisit')
        MaternalArvPregHistory = models.get_model('mpepu_maternal', 'MaternalArvPregHistory')
        maternal_visit = MaternalVisit.objects.get_by_natural_key(report_datetime, visit_instance, appt_status, visit_definition_code, subject_identifier_as_pk)
        maternal_arv_preg_history = MaternalArvPregHistory.objects.get(maternal_visit=maternal_visit)
        return self.get(arv_code=arv_code, modification_date=modification_date, maternal_arv_preg_history=maternal_arv_preg_history)
