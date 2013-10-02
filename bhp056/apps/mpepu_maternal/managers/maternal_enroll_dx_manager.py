from django.db import models


class MaternalEnrollDxManager(models.Manager):

    def get_by_natural_key(self, diagnosis, modification_date, report_datetime, visit_instance, appt_status, visit_definition_code, subject_identifier_as_pk):
        MaternalVisit = models.get_model('mpepu_maternal', 'MaternalVisit')
        MaternalEnrollMed = models.get_model('mpepu_maternal', 'MaternalEnrollMed')
        maternal_visit = MaternalVisit.objects.get_by_natural_key(report_datetime, visit_instance, appt_status, visit_definition_code, subject_identifier_as_pk)
        maternal_enroll_med = MaternalEnrollMed(maternal_visit=maternal_visit)
        return self.get(diagnosis=diagnosis, maternal_enroll_med=maternal_enroll_med)
