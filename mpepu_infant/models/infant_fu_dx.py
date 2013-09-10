from django.db import models
from django.core.urlresolvers import reverse
from audit_trail.audit import AuditTrail
from mpepu_infant.models import BaseScheduledVisitModel
from infant_fu import InfantFu


class InfantFuDx(BaseScheduledVisitModel):

    infant_fu = models.ForeignKey(InfantFu)

    history = AuditTrail()

    objects = models.Manager()

    def __unicode__(self):
        return unicode(self.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantfudx_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant FollowUp: Dx"
        verbose_name_plural = "Infant FollowUp: Dx"
