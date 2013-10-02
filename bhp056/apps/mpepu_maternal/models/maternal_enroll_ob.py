from django.db import models
from django.core.urlresolvers import reverse
from edc.audit.audit_trail import AuditTrail
from mpepu_maternal.models import BaseScheduledVisitModel
from maternal_enroll import MaternalEnroll


class MaternalEnrollOb(BaseScheduledVisitModel):

    """Model for Maternal Enrollment: Ob History"""

    maternal_enroll = models.OneToOneField(MaternalEnroll)

    pregs_24wks_or_more = models.IntegerField(
        verbose_name="1a. Number of pregnancies at least 24 weeks.?",
        help_text="",
        )
    lost_before_24wks = models.IntegerField(
        verbose_name="1b. Number of pregnancies lost before 24 weeks gestation",
        help_text="",
        )
    lost_after_24wks = models.IntegerField(
        verbose_name="1c. Number of pregnancies lost at or after 24 weeks gestation ",
        help_text="",
        )
    live_children = models.IntegerField(
        verbose_name="2. How many other living children does the participant currently have (excluding baby to be enrolled in the study)",
        help_text="",
        )
    children_died_b4_5yrs = models.IntegerField(
        verbose_name="3. How many of the participant's children died after birth before 5 years of age? ",
        help_text="",
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % (self.maternal_enroll)

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalenrollob_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Enrollment: Ob History"
