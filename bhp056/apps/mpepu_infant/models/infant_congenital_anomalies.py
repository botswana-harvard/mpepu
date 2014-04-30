from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models

from edc.base.model.fields.custom.custom_fields import OtherCharField
from edc.base.model.validators import datetime_not_before_study_start, datetime_not_future, datetime_is_after_consent
from edc.choices.common import CONFIRMED_SUSPECTED
from edc.subject.consent.models.base_consented_uuid_model import BaseConsentedUuidModel
from edc.entry_meta_data.managers import EntryMetaDataManager

from apps.mpepu.choices import (CNS_ABNORMALITIES, FACIAL_DEFECT, CLEFT_DISORDER, MOUTH_UP_GASTROINT_DISORDER,
                                CARDIOVASCULAR_DISORDER, RESPIRATORY_DEFECT, LOWER_GASTROINTESTINAL_ABNORMALITY,
                                FEM_GENITAL_ANOMALY, MALE_GENITAL_ANOMALY, RENAL_ANOMALY, MUSCULOSKELETAL_ABNORMALITY,
                                SKIN_ABNORMALITY, TRISOME_CHROSOMESOME_ABNORMALITY, OTHER_DEFECT)

from .base_infant_registered_subject_model import BaseInfantRegisteredSubjectModel
from .infant_off_study_mixin import InfantOffStudyMixin
from .infant_visit import InfantVisit


class InfantCongenitalAnomalies(BaseInfantRegisteredSubjectModel):

    infant_visit = models.OneToOneField(InfantVisit)

    entry_meta_data_manager = EntryMetaDataManager(InfantVisit)

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.registered_subject.relative_identifier

    def get_subject_identifier(self):
        return self.registered_subject.subject_identifier

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantcongenitalanomalies__change', args=(self.id,))

    def get_report_datetime(self):
        return self.registered_subject.registration_datetime

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies"


class BaseCnsItem(InfantOffStudyMixin, BaseConsentedUuidModel):
# class BaseCnsItem(InfantBaseUuidModel):
    """Adds in method to get mother's subject_identifier for confirming the consent (see bhp_consent)."""

    report_datetime = models.DateTimeField(
        verbose_name="Visit Date and Time",
        validators=[
            datetime_not_before_study_start,
            datetime_is_after_consent,
            datetime_not_future,
            ],
        default=datetime.today()
        )

    #infant_visit = models.OneToOneField(InfantVisit)

    #entry_meta_data_manager = EntryMetaDataManager(InfantVisit)

#     def get_visit(self):
#         return '2000'

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.congenital_anomalies.registered_subject.relative_identifier

    def get_report_datetime(self):
        return self.report_datetime

    def get_subject_identifier(self):
        """Returns subject identifier."""
        return self.congenital_anomalies.registered_subject.subject_identifier

    class Meta:
        abstract = True


class InfantCnsAbnormalityItems(BaseCnsItem):

    congenital_anomalies = models.ForeignKey(InfantCongenitalAnomalies)

    cns_abnormality = models.CharField(
        max_length=250,
        choices=CNS_ABNORMALITIES,
        verbose_name="Central nervous system abnormality",
        blank=True,
        null=True,
        )
    abnormality_status = models.CharField(
        max_length=35,
        choices=CONFIRMED_SUSPECTED,
        verbose_name="Abnormality status",
        blank=True,
        null=True,
        )
    cns_abnormality_other = OtherCharField(
        max_length=250,
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )

    def get_visit(self):
        return self.congenital_anomalies.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantcnsabnormalityitems__change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies:Cns"


class InfantFacialDefectItems(BaseCnsItem):

    congenital_anomalies = models.ForeignKey(InfantCongenitalAnomalies)

    facial_defect = models.CharField(
        max_length=250,
        choices=FACIAL_DEFECT,
        verbose_name="Facial defects",
        blank=True,
        null=True,
        )
    abnormality_status = models.CharField(
        max_length=35,
        choices=CONFIRMED_SUSPECTED,
        verbose_name="Abnormality status",
        blank=True,
        null=True,
        )
    facial_defects_other = OtherCharField(
        max_length=250,
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )

    def get_visit(self):
        return self.congenital_anomalies.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantfacialdefectitems__change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies:Facial"


class InfantCleftDisorderItems(BaseCnsItem):

    congenital_anomalies = models.ForeignKey(InfantCongenitalAnomalies)

    cleft_disorder = models.CharField(
        max_length=250,
        choices=CLEFT_DISORDER,
        verbose_name="Cleft disorders",
        blank=True,
        null=True,
        )
    abnormality_status = models.CharField(
        max_length=35,
        choices=CONFIRMED_SUSPECTED,
        verbose_name="Abnormality status",
        blank=True,
        null=True,
        )
    cleft_disorders_other = OtherCharField(
        max_length=250,
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )

    def get_visit(self):
        return self.congenital_anomalies.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantcleftdisorderitems__change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies:Cleft"


class InfantMouthUpGastrointestinalItems(BaseCnsItem):

    congenital_anomalies = models.ForeignKey(InfantCongenitalAnomalies)

    mouth_up_gastrointest = models.CharField(
        max_length=250,
        choices=MOUTH_UP_GASTROINT_DISORDER,
        verbose_name="Mouth and upper gastrointestinal disorders",
        blank=True,
        null=True,
        )
    abnormality_status = models.CharField(
        max_length=35,
        choices=CONFIRMED_SUSPECTED,
        verbose_name="Abnormality status",
        blank=True,
        null=True,
        )
    mouth_up_gastrointest_other = OtherCharField(
        max_length=250,
        verbose_name="if other specify...",
        blank=True,
        null=True)

    def get_visit(self):
        return self.congenital_anomalies.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantmouthupgastrointestinalitems__change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies:MouthUpp"


class InfantCardiovascularDisorderItems(BaseCnsItem):

    congenital_anomalies = models.ForeignKey(InfantCongenitalAnomalies)

    cardiovascular_disorder = models.CharField(
        max_length=250,
        choices=CARDIOVASCULAR_DISORDER,
        verbose_name="Cardiovascular disorders",
        blank=True,
        null=True,
        )
    abnormality_status = models.CharField(
        max_length=35,
        choices=CONFIRMED_SUSPECTED,
        verbose_name="Abnormality status",
        blank=True,
        null=True,
        )
    cardiovascular_other = OtherCharField(
        max_length=250,
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )

    def get_visit(self):
        return self.congenital_anomalies.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantcardiovasculardisorderitems__change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies:Cardio"


class InfantRespiratoryDefectItems(BaseCnsItem):

    congenital_anomalies = models.ForeignKey(InfantCongenitalAnomalies)

    respiratory_defect = models.CharField(
        max_length=250,
        choices=RESPIRATORY_DEFECT,
        verbose_name="Respiratory defects",
        blank=True,
        null=True,
        )
    abnormality_status = models.CharField(
        max_length=35,
        choices=CONFIRMED_SUSPECTED,
        verbose_name="Abnormality status",
        blank=True,
        null=True,
        )
    respiratory_defects_other = OtherCharField(
        max_length=250,
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )

    def get_visit(self):
        return self.congenital_anomalies.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantrespiratorydefectitems__change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies:Respitarory"


class InfantLowerGastrointestinalItems(BaseCnsItem):

    congenital_anomalies = models.ForeignKey(InfantCongenitalAnomalies)

    lower_gastrointestinal = models.CharField(
        max_length=250,
        choices=LOWER_GASTROINTESTINAL_ABNORMALITY,
        verbose_name="Lower gastrointestinal abnormalities",
        blank=True,
        null=True,
        )
    abnormality_status = models.CharField(
        max_length=35,
        choices=CONFIRMED_SUSPECTED,
        verbose_name="Abnormality status",
        blank=True,
        null=True,
        )
    lower_gastrointestinal_other = OtherCharField(
        max_length=250,
        verbose_name="if other specify",
        blank=True,
        null=True,
        )

    def get_visit(self):
        return self.congenital_anomalies.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantlowergastrointestinalitems__change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies:LowerGast"


class InfantFemaleGenitalAnomalyItems(BaseCnsItem):

    congenital_anomalies = models.ForeignKey(InfantCongenitalAnomalies)

    female_genital_anomal = models.CharField(
        max_length=250,
        choices=FEM_GENITAL_ANOMALY,
        verbose_name="Female genital anomaly",
        blank=True,
        null=True,
        )
    abnormality_status = models.CharField(
        max_length=35,
        choices=CONFIRMED_SUSPECTED,
        verbose_name="Abnormality status",
        blank=True,
        null=True,
        )
    female_genital_anomal_other = OtherCharField(
        max_length=250,
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )

    def get_visit(self):
        return self.congenital_anomalies.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantfemalegenitalanomalyitems__change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies:FemaleGen"


class InfantMaleGenitalAnomalyItems(BaseCnsItem):

    congenital_anomalies = models.ForeignKey(InfantCongenitalAnomalies)

    male_genital_anomal = models.CharField(
        max_length=250,
        choices=MALE_GENITAL_ANOMALY,
        verbose_name="Male genital anomaly",
        blank=True,
        null=True,
        )
    abnormality_status = models.CharField(
        max_length=35,
        choices=CONFIRMED_SUSPECTED,
        verbose_name="Abnormality status",
        blank=True,
        null=True,
        )
    male_genital_anomal_other = OtherCharField(
        max_length=250,
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )

    def get_visit(self):
        return self.congenital_anomalies.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantmalegenitalanomalyitems__change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies:MaleGen"


class InfantRenalAnomalyItems(BaseCnsItem):

    congenital_anomalies = models.ForeignKey(InfantCongenitalAnomalies)

    renal_amomalies = models.CharField(
        max_length=250,
        choices=RENAL_ANOMALY,
        verbose_name="Renal anomalies",
        blank=True,
        null=True,
        )
    abnormality_status = models.CharField(
        max_length=35,
        choices=CONFIRMED_SUSPECTED,
        verbose_name="Abnormality status",
        blank=True,
        null=True,
        )
    renal_amomalies_other = OtherCharField(
        max_length=250,
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )

    def get_visit(self):
        return self.congenital_anomalies.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantcongenitalanomaliesrenal__change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies:Renal"


class InfantMusculoskeletalAbnormalItems(BaseCnsItem):

    congenital_anomalies = models.ForeignKey(InfantCongenitalAnomalies)

    musculo_skeletal = models.CharField(
        max_length=250,
        choices=MUSCULOSKELETAL_ABNORMALITY,
        verbose_name="Musculo-skeletal abnomalities",
        blank=True,
        null=True,
        )
    abnormality_status = models.CharField(
        max_length=35,
        choices=CONFIRMED_SUSPECTED,
        verbose_name="Abnormality status",
        blank=True,
        null=True,
        )
    musculo_skeletal_other = OtherCharField(
        max_length=250,
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )

    def get_visit(self):
        return self.congenital_anomalies.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantcongenitalanomaliesmusculosk__change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies:Musculosk"


class InfantSkinAbnormalItems(BaseCnsItem):

    congenital_anomalies = models.ForeignKey(InfantCongenitalAnomalies)

    skin_abnormality = models.CharField(
        max_length=250,
        choices=SKIN_ABNORMALITY,
        verbose_name="Skin abnormalities",
        help_text="Excludes cafe au lait spots, Mongolian spots, port wine stains, nevus, hemangloma <4 cm in diameter. If hemangloma is >4 cm, specify",
        blank=True,
        null=True,
        )
    abnormality_status = models.CharField(
        max_length=35,
        choices=CONFIRMED_SUSPECTED,
        verbose_name="Abnormality status",
        blank=True,
        null=True,
        )
    skin_abnormality_other = OtherCharField(
        max_length=250,
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )

    def get_visit(self):
        return self.congenital_anomalies.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantcongenitalanomaliesskin__change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies:Skin"


class InfantTrisomiesChromosomeItems(BaseCnsItem):

    congenital_anomalies = models.ForeignKey(InfantCongenitalAnomalies)

    triso_chromo_abnormal = models.CharField(
        max_length=250,
        choices=TRISOME_CHROSOMESOME_ABNORMALITY,
        verbose_name="Trisomies / chromosomes abnormalities",
        blank=True,
        null=True,
        )
    abnormality_status = models.CharField(
        max_length=35,
        choices=CONFIRMED_SUSPECTED,
        verbose_name="Abnormality status",
        blank=True,
        null=True,
        )
    triso_chromo_abnormal_other = OtherCharField(
        max_length=250,
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )

    def get_visit(self):
        return self.congenital_anomalies.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantcongenitalanomaliestrisomes__change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies:Trisomes"


class InfantOtherAbnormalityItems(BaseCnsItem):

    congenital_anomalies = models.ForeignKey(InfantCongenitalAnomalies)

    other_abnormalities = models.CharField(
        max_length=250,
        choices=OTHER_DEFECT,
        verbose_name="Other",
        blank=True,
        null=True,
        )
    abnormality_status = models.CharField(
        max_length=35,
        choices=CONFIRMED_SUSPECTED,
        verbose_name="Abnormality status",
        blank=True,
        null=True,
        )
    other_abnormalities_other = OtherCharField(
        max_length=250,
        verbose_name="if other specify...",
        blank=True,
        null=True,
        )

    def get_visit(self):
        return self.congenital_anomalies.infant_visit

    def get_absolute_url(self):
        return reverse('admin:mpepu_infant_infantcongenitalanomaliesother__change', args=(self.id,))

    class Meta:
        app_label = "mpepu_infant"
        verbose_name = "Infant Congenital Anomalies:Other"
