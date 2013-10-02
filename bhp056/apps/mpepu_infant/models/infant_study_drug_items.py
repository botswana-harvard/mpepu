from django.db import models
from django.core.urlresolvers import reverse
from infant_base_uuid_model import InfantBaseUuidModel
from audit_trail.audit import AuditTrail
from bhp_haart.choices import DOSE_STATUS, ARV_MODIFICATION_REASON
from infant_study_drug import InfantStudyDrug
from bhp_entry.models import AdditionalEntryBucket
from django.db.models import Q, get_model


class InfantStudyDrugItems(InfantBaseUuidModel):

    """ CTX / Placebo """

    inf_study_drug = models.ForeignKey(InfantStudyDrug)

    dose_status = models.CharField(
        verbose_name="Dose Status",
        choices=DOSE_STATUS,
        max_length=25,
        )
    ingestion_date = models.DateField(
        verbose_name="Date of study drug ingestion",
        )
    modification_reason = models.CharField(
        verbose_name="Reason for modification",
        choices=ARV_MODIFICATION_REASON,
        max_length=75,
        )

    history = AuditTrail()

    def save(self, *args, **kwargs):
        super(InfantStudyDrugItems, self).save(*args, **kwargs)
        if self.dose_status.lower() == 'permanently discontinued':
            model = get_model('mpepu_infant', 'infantoffdrug')
            AdditionalEntryBucket.objects.add_for(
                registered_subject=self.inf_study_drug.infant_visit.appointment.registered_subject,
                model=model,
                qset=Q(registered_subject=self.inf_study_drug.infant_visit.appointment.registered_subject))

    def get_visit(self):
        return  self.inf_study_drug.infant_visit

    def __unicode__(self):
        return  unicode(self.inf_study_drug.infant_visit)

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantstudydrug_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Study Drug Record Items"
        ordering = ['ingestion_date', ]
