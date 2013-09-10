from audit_trail.audit import AuditTrail
from datetime import datetime, time
from django.core.urlresolvers import reverse
from bhp_adverse.models import BaseDeathReport
from maternal_off_study_mixin import MaternalOffStudyMixin


class MaternalDeath (MaternalOffStudyMixin, BaseDeathReport):

    #registered_subject = models.OneToOneField(RegisteredSubject)

    history = AuditTrail()

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternaldeath_change', args=(self.id,))

    def get_report_datetime(self):
        return datetime.combine(self.death_date, time(0, 0))

    class Meta:
        verbose_name = "Maternal Death"
        app_label = "mpepu_maternal"


"""
class MaternalDeathAssessment(BaseDeathReportAssess):

    maternal_death = models.OneToOneField(MaternalDeath)

    class Meta:
        app_label="mpepu_maternal"
"""
