from datetime import datetime, time
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.subject.registration.models import RegisteredSubject

from .maternal_base_registered_subject_model import MaternalBaseRegisteredSubjectModel


class MaternalPostReg(MaternalBaseRegisteredSubjectModel):

    """ Post-partum registration """

    reg_datetime = models.DateTimeField()

    history = AuditTrail()

    def get_registration_datetime(self):

        # base the date on the infant dob which implies the infant must exist
        if RegisteredSubject.objects.filter(relative_identifier=self.registered_subject.subject_identifier):
            rs = RegisteredSubject.objects.filter(relative_identifier=self.registered_subject.subject_identifier).order_by('dob')
            if rs[0].dob:
                infant_dob = rs[0].dob
            else:
                raise AttributeError('{0} model method \'get_registration_datetime\' cannot determine the dob of the first infant for this {0}'.format(self, self.registered_subject))
        else:
            raise AttributeError('{0} model method \'get_registration_datetime\' cannot find an infant for this {0}'.format(self, self.registered_subject))
        return datetime.combine(infant_dob, time(0, 0))

    def __unicode__(self):
        return "{0} {1}".format(self.registered_subject, self.reg_datetime)

    def get_report_datetime(self):
        return self.reg_datetime

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternalpostreg_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Post Partum Registration"
