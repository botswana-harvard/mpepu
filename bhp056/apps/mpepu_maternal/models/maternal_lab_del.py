from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.base.model.fields.custom.custom_fields import OtherCharField
from edc.base.model.validators import datetime_not_future
from edc.choices.common import YES_NO, YES_NO_NA_SPECIFY, YES_NO_UNKNOWN
from edc.core.crypto_fields.utils import mask_encrypted
from edc.core.identifier.classes import InfantIdentifier
from edc.subject.adverse_event.choices import GRADING_SCALE
from edc.subject.code_lists.models import WcsDxAdult

from apps.mpepu.choices import LABOUR_HOURS, LABOUR_MODE_OF_DELIVERY, DELIVERY_HOSPITAL, DX
from apps.mpepu_list.models import HealthCond, DelComp, ObComp, Suppliment

from ..managers import MaternalLabDelDxTManager

from .base_scheduled_visit_model import BaseScheduledVisitModel
from .maternal_base_uuid_model import MaternalBaseUuidModel



class MaternalLabDel(BaseScheduledVisitModel):

    """ Maternal Labor and Delivery which triggers registration of infants.

    .. note:: This model allocates infant identifiers. Check admin.py :func:`save_model` method
              for bhp_identifier class access."""

    delivery_datetime = models.DateTimeField(
        verbose_name="Date and time of delivery :",
        help_text="If TIME unknown, estimate",
        validators=[
            datetime_not_future,],
        )
    del_time_is_est = models.CharField(
        verbose_name="Is the delivery TIME estimated?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )
    labour_hrs = models.CharField(
        verbose_name="How long prior to to delivery, in HRS, did labour begin? ",
        max_length=10,
        choices=LABOUR_HOURS,
        help_text="For multiple births, time of delivery = time first infant born",
        )
    del_mode = models.CharField(
        verbose_name="Mode of delivery  ",
        max_length=25,
        choices=LABOUR_MODE_OF_DELIVERY,
        help_text="",
        )

    has_ga = models.CharField(
        verbose_name='Is the gestational age at delivery known?',
        max_length=10,
        choices=YES_NO,
        help_text="If known, complete below",
        )

    ga = models.IntegerField(
        verbose_name="Gestational Age at Delivery  ",
        validators=[MinValueValidator(20), MaxValueValidator(44), ],
        null=True,
        blank=True,
        help_text="in weeks",
        )

    del_hosp = models.CharField(
        verbose_name="Where did the participant deliver? ",
        max_length=25,
        choices=DELIVERY_HOSPITAL,
        help_text="If 'Other health facility' or 'Other', specify below",
        )
    del_hosp_other = OtherCharField()

    has_urine_tender = models.CharField(
        max_length=10,
        choices=YES_NO_UNKNOWN,
        verbose_name="Was uterine tenderness recorded? ",
        help_text="",
        )
    labr_max_temp = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        verbose_name="Indicate the maximum temperature of mother during labour",
        help_text="In degrees Celcius. -1 = unknown",
        validators=[
            MinValueValidator(-1),
            MaxValueValidator(41),
            ]
        )
    has_chorioamnionitis = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Was chorio-amnionitis suspected? ",
        help_text="",
        )
    has_del_comp = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Were there other complications at delivery? ",
        help_text="( if 'YES' continue. Otherwise go to question 10 )",
        )
    del_comp = models.ManyToManyField(DelComp,
        verbose_name="If so, select the complication ",
        help_text="",

        )
    del_comp_other = models.TextField(
        max_length=250,
        verbose_name="if other, describe the complication",
        blank=True,
        null=True,
        )

    live_infants = models.IntegerField(
        verbose_name="How many live babies did the mother deliver? ",
        help_text="",
        )

    live_infants_to_register = models.IntegerField(
        verbose_name="How many babies are registering to the study? ",
        help_text="",
        )

    still_borns = models.IntegerField(
        verbose_name="How many stillbirths did the mother deliver?  ",
        help_text="( if '>0' continue. Otherwise go to question 13 )",
        )
    
    still_born_has_congen_abn = models.CharField(
        max_length=3,
        choices=YES_NO_NA_SPECIFY,
        verbose_name="If any stillborns, did any have a congenital abnormality noted? ",
        help_text="",
        blank=True,
        null=True,
        default="N/A",
        )
    
    still_born_congen_abn = OtherCharField(
        verbose_name="If yes, specify;",
        blank=True,
        null=True,
        )
    
    del_comment = models.TextField(
        max_length=250,
        verbose_name="List any addtional information about the labour and delivery (mother only) ",
        blank=True,
        null=True,
        )
    
    comment = models.TextField(
        max_length=250,
        verbose_name="Comment if any additional pertinent information ",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    class Meta:
        app_label = 'mpepu_maternal'
        verbose_name = "Maternal Labour & Delivery"

    def save(self, *args, **kwargs):
        # put in to trap during testing
        if self.has_ga == 'Yes':
            if self.ga < 20 or self.ga > 44:
                raise ValidationError('Attribute \'ga\' must be between >=20 and <=44 weeks or None. Got {0}'.format(self.ga))
        super(MaternalLabDel, self).save(*args, **kwargs)

    def post_save_register_infants(self, created):
        """Registers infant(s) using the bhp_identifier class which allocates identifiers and creates registered_subject instances.

        Called on the post_save signal"""
        if created:
            if self.live_infants_to_register > 0:
                for infant_order in range(0, self.live_infants_to_register):
                    infant_identifier = InfantIdentifier(
                        maternal_identifier=self.maternal_visit.appointment.registered_subject.subject_identifier,
                        study_site=self.maternal_visit.appointment.registered_subject.study_site,
                        birth_order=infant_order,
                        live_infants=self.live_infants,
                        live_infants_to_register=self.live_infants_to_register,
                        user=self.user_created)
                    infant_identifier.get_identifier()

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternallabour&delivery_change', args=(self.id,))

    def __unicode__(self):
        return "{0} delivered on {1} ({2})".format(self.maternal_visit.appointment.registered_subject,
                                                   self.delivery_datetime,
                                                   mask_encrypted(self.maternal_visit.appointment.registered_subject.first_name))


class MaternalLabDelMed(BaseScheduledVisitModel):

    """ Medical history collected during labor and delivery. """
    maternal_lab_del = models.OneToOneField(MaternalLabDel)

    has_health_cond = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Has the mother been newly diagnosed (during this pregnancy) with any major chronic health condition(s) that remain ongoing?  ",
        help_text="if yes answer 14a, otherwise go to Question 15",
        )
    health_cond = models.ManyToManyField(HealthCond,
        verbose_name="Select all that apply ",
        help_text="",
        )
    health_cond_other = OtherCharField()
    has_ob_comp = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="During this pregnancy, did the mother have any of the following obstetrical complications? (in 15a)",
        help_text="",
        )
    ob_comp = models.ManyToManyField(ObComp,
        verbose_name="Select all that apply",
        help_text="",
        )
    ob_comp_other = models.TextField(
        max_length=250,
        blank=True,
        null=True,
        )

    comment = models.TextField(
        max_length=250,
        verbose_name="Comment if any additional pertinent information ",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Labour & Delivery: MedHistory"

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternallabour&deliverymedhistory_change', args=(self.id,))


class MaternalLabDelClinic(BaseScheduledVisitModel):

    """ Laboratory and other clinical information collected during labor and delivery"""

    maternal_lab_del = models.OneToOneField(MaternalLabDel)

    has_cd4 = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="During this pregnancy did the mother have at least one CD4 count performed (outside the study)? ",
        help_text="( if 'YES' continue. Otherwise go to question 20 )",
        )
    cd4_date = models.DateField(
        verbose_name="Date of most recent CD4 test? ",
        help_text="",
        blank=True,
        null=True
        )
    cd4_result = models.CharField(
        max_length=35,
        verbose_name="Result of most recent CD4 test",
        blank=True,
        null=True
        )
    has_vl = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="During this pregnancy did the mother have a viral load perfomed (outside the study)? ",
        help_text="(if 'YES' continue. Otherwise go to question 2)",
        )
    vl_date = models.DateField(
        verbose_name="If yes, Date of most recent VL test? ",
        help_text="",
        blank=True,
        null=True
        )
    vl_result = models.CharField(
        max_length=35,
        verbose_name="Result of most recent VL test",
        blank=True,
        null=True
        )

    took_suppliments = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Did the mother take any of the following during this pregnancy?(in 23a)   ",
        help_text="( if 'YES' continue. Otherwise go to question 23 )",
        )

    suppliment = models.ManyToManyField(Suppliment,
        verbose_name="Select all that apply ",
        help_text="",
        )
    comment = models.TextField(
        max_length=250,
        verbose_name="Comment if any additional pertinent information ",
        blank=True,
        null=True,
        )

    history = AuditTrail()

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Labour & Delivery: ClinHist"

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternallabour&deliverymedhistory_change', args=(self.id,))


class MaternalLabDelDx(BaseScheduledVisitModel):

    """ Diagnosis during pregnancy collected during labor and delivery. """

    maternal_lab_del = models.OneToOneField(MaternalLabDel)

    has_preg_dx = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="During this pregnancy, did the mother have any of the following? ",
        help_text="If yes, Select all that apply in the table, only report grade 3 or 4 diagnoses",
        )
    has_who_dx = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="During this pregnancy, did the mother have any new diagnoses listed in the WHO Adult/Adolescent HIV clinical staging document which is/are NOT reported below in Question 3 ",
        help_text="If yes, answer 17a, otherwise go to Question 18",
        )
    wcs_dx_adult = models.ManyToManyField(WcsDxAdult,
        verbose_name="List any new WHO Stage III/IV diagnoses that are not reported in Question 3 below:  ",
        )

    history = AuditTrail()

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternallabour&deliverypregdx_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Labour & Delivery: Preg Dx"


class MaternalLabDelDxT (MaternalBaseUuidModel):

    """ Diagnosis during pregnancy collected during labor and delivery (transactions). """

    maternal_lab_del_dx = models.ForeignKey(MaternalLabDelDx)

    lab_del_dx = models.CharField(
        max_length=175,
        choices=DX,
        verbose_name="Diagnosis",
        help_text="",
        )
    lab_del_dx_specify = models.CharField(
        max_length=50,
        verbose_name="Diagnosis specification",
        help_text="",
        blank=True,
        null=True,
        )
    grade = models.IntegerField(
        choices=GRADING_SCALE,
        verbose_name="Grade",
        )
    hospitalized = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Hospitalized",
        help_text="",
        )

    history = AuditTrail()

    objects = MaternalLabDelDxTManager()

    def natural_key(self):
        return (self.lab_del_dx, ) + self.maternal_lab_del_dx.natural_key()

    def get_visit(self):
        return self.maternal_lab_del_dx.maternal_visit

    def get_report_datetime(self):
        return self.maternal_lab_del_dx.maternal_visit.report_datetime

    def get_subject_identifier(self):
        return self.maternal_lab_del_dx.maternal_visit.subject_identifier

    def __unicode__(self):
        return unicode(self.get_visit())

    def get_absolute_url(self):
        return reverse('admin:mpepu_maternal_maternallabour&deliverypregdx_change', args=(self.id,))

    class Meta:
        app_label = "mpepu_maternal"
        verbose_name = "Maternal Labour & Delivery: Preg DxT"
