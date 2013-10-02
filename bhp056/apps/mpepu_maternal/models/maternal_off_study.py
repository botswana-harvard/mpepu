from django.core.urlresolvers import reverse
from audit_trail.audit import AuditTrail
from bhp_off_study.models import BaseOffStudy


class MaternalOffStudy(BaseOffStudy):

    """ Maternal Off-Study.

    * Complete this form to record permanent discontinuation from all follow-up for each participant (Mother).
    * Header date equals "Off-Study Date", unless there is a death.In the event of death "Off-study Date"="Date of Death". """

    history = AuditTrail()

    def __unicode__(self):
        return '%s ' % (self.registered_subject)

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternaloffstudy_change', args=(self.id,))

    class Meta:
        verbose_name = "Maternal Off-Study"
        verbose_name_plural = "Maternal Off-Study"
        app_label = "mpepu_maternal"
