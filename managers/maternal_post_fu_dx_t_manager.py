from django.db import models


class MaternalPostFuDxTManager(models.Manager):

    def get_by_natural_key(self, lab_del_dx, report_datetime, visit_instance, appt_status, visit_definition_code, subject_identifier_as_pk):
        MaternalVisit = models.get_model('mpepu_maternal', 'MaternalVisit')
        MaternalPostFuDx = models.get_model('mpepu_maternal', 'MaternalPostFuDx')
        maternal_visit = MaternalVisit.objects.get_by_natural_key(report_datetime, visit_instance, appt_status, visit_definition_code, subject_identifier_as_pk)
        maternal_post_fu_dx = MaternalPostFuDx.objects.get(maternal_visit=maternal_visit)
        return self.get(lab_del_dx=lab_del_dx, maternal_post_fu_dx=maternal_post_fu_dx)
