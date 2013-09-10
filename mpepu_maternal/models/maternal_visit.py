from django.core.urlresolvers import reverse
from audit_trail.audit import AuditTrail
from bhp_visit_tracking.models import BaseVisitTracking
from maternal_off_study_mixin import MaternalOffStudyMixin
from mpepu_maternal.choices import VISIT_REASON


class MaternalVisit(MaternalOffStudyMixin, BaseVisitTracking):

    """ Maternal visit form that links all follow-up forms """

    history = AuditTrail()

    def __unicode__(self):
        return unicode(self.appointment)

    def get_visit_reason_choices(self):
        return VISIT_REASON

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalvisit_change', args=(self.id,))

    class Meta:
        db_table = 'mpepu_maternal_maternalvisit'
        verbose_name = "Maternal Visit"
        app_label = "mpepu_maternal"
