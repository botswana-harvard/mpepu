from django.db import models
from django.core.urlresolvers import reverse
from audit_trail.audit import AuditTrail
from bhp_haart.models import BaseHaartModification
from infant_arv_proph import InfantArvProph
from infant_off_study_mixin import InfantOffStudyMixin


class InfantArvProphMod(InfantOffStudyMixin, BaseHaartModification):

    infant_arv_proph = models.ForeignKey(InfantArvProph)

    history = AuditTrail()

    def get_report_datetime(self):
        return self.infant_arv_proph.get_report_datetime()

    def get_subject_identifier(self):
        return self.infant_arv_proph.get_subject_identifier()

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.infant_arv_proph.infant_visit.appointment.registered_subject.relative_identifier

    def __unicode__(self):
        return unicode(self.infant_arv_proph.infant_visit)

    def get_visit(self):
        return self.infant_arv_proph.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantarvprophmod_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = 'Infant NVP or AZT Proph: Mods'
