from django import forms

from edc.base.form.forms import BaseModelForm

from apps.mpepu_infant.models import (InfantCongenitalAnomalies, InfantCnsAbnormalityItems, InfantFacialDefectItems, InfantCleftDisorderItems,
                                      InfantMouthUpGastrointestinalItems, InfantCardiovascularDisorderItems, InfantRespiratoryDefectItems, InfantLowerGastrointestinalItems,
                                      InfantFemaleGenitalAnomalyItems, InfantMaleGenitalAnomalyItems, InfantRenalAnomalyItems, InfantMusculoskeletalAbnormalItems,
                                      InfantSkinAbnormalItems, InfantTrisomiesChromosomeItems, InfantOtherAbnormalityItems)


class InfantCongenitalAnomaliesForm (BaseModelForm):

    class Meta:
        model = InfantCongenitalAnomalies


class InfantCnsAbnormalityItemsForm (BaseModelForm):
    def clean(self):
        cleaned_data = super(InfantCnsAbnormalityItemsForm, self).clean()
        if cleaned_data.get('cns_abnormality') and not cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You indicated that participant has CNS Abnormality and yet did not indicate the abnormality status. Please correct.')
        if not cleaned_data.get('cns_abnormality') and cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You did NOT indicate the CNS Abnormality and yet provided the abnormality status. Please correct.')

        return cleaned_data

    class Meta:
        model = InfantCnsAbnormalityItems


class InfantFacialDefectItemsForm (BaseModelForm):
    def clean(self):
        cleaned_data = super(InfantFacialDefectItemsForm, self).clean()
        if cleaned_data.get('facial_defect') and not cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You indicated that participant has facial defect and yet did not indicate the abnormality status. Please correct.')
        if not cleaned_data.get('facial_defect') and cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You did NOT indicate the facial defect and yet provided the abnormality status. Please correct.')

        return cleaned_data

    class Meta:
        model = InfantFacialDefectItems


class InfantCleftDisorderItemsForm (BaseModelForm):
    def clean(self):
        cleaned_data = super(InfantCleftDisorderItemsForm, self).clean()
        if cleaned_data.get('cleft_disorder') and not cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You indicated that participant has cleft disorder and yet did not indicate the abnormality status. Please correct.')
        if not cleaned_data.get('cleft_disorder') and cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You did NOT indicate the cleft disorder and yet provided the abnormality status. Please correct.')

        return cleaned_data

    class Meta:
        model = InfantCleftDisorderItems


class InfantMouthUpGastrointestinalItemsForm (BaseModelForm):
    def clean(self):
        cleaned_data = super(InfantMouthUpGastrointestinalItemsForm, self).clean()
        if cleaned_data.get('mouth_up_gastrointest') and not cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You indicated that participant has mouth up gastrointest and yet did not indicate the abnormality status. Please correct.')
        if not cleaned_data.get('mouth_up_gastrointest') and cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You did NOT indicate the mouth up gastrointest and yet provided the abnormality status. Please correct.')

        return cleaned_data

    class Meta:
        model = InfantMouthUpGastrointestinalItems


class InfantCardiovascularDisorderItemsForm (BaseModelForm):
    def clean(self):
        cleaned_data = super(InfantCardiovascularDisorderItemsForm, self).clean()
        if cleaned_data.get('cardiovascular_disorder') and not cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You indicated that participant has cardiovascular disorder and yet did not indicate the abnormality status. Please correct.')
        if not cleaned_data.get('cardiovascular_disorder') and cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You did NOT indicate the cardiovascular disorder and yet provided the abnormality status. Please correct.')

        return cleaned_data

    class Meta:
        model = InfantCardiovascularDisorderItems


class InfantRespiratoryDefectItemsForm (BaseModelForm):
    def clean(self):
        cleaned_data = super(InfantRespiratoryDefectItemsForm, self).clean()
        if cleaned_data.get('respiratory_defect') and not cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You indicated that participant has respiratory defect and yet did not indicate the abnormality status. Please correct.')
        if not cleaned_data.get('respiratory_defect') and cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You did NOT indicate the respiratory defect and yet provided the abnormality status. Please correct.')

        return cleaned_data

    class Meta:
        model = InfantRespiratoryDefectItems


class InfantLowerGastrointestinalItemsForm (forms.ModelForm):
    def clean(self):
        cleaned_data = super(InfantLowerGastrointestinalItemsForm, self).clean()
        if cleaned_data.get('lower_gastrointestinal') and not cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You indicated that participant has lower gastrointestinal and yet did not indicate the abnormality status. Please correct.')
        if not cleaned_data.get('lower_gastrointestinal') and cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You did NOT indicate the lower gastrointestinal and yet provided the abnormality status. Please correct.')

        return cleaned_data

    class Meta:
        model = InfantLowerGastrointestinalItems


class InfantFemaleGenitalAnomalyItemsForm (BaseModelForm):
    def clean(self):
        cleaned_data = super(InfantFemaleGenitalAnomalyItemsForm, self).clean()
        if cleaned_data.get('female_genital_anomal') and not cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You indicated that participant has female genital anomaly and yet did not indicate the abnormality status. Please correct.')
        if not cleaned_data.get('female_genital_anomal') and cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You did NOT indicate the female genital anomaly and yet provided the abnormality status. Please correct.')

        return cleaned_data

    class Meta:
        model = InfantFemaleGenitalAnomalyItems


class InfantMaleGenitalAnomalyItemsForm (BaseModelForm):
    def clean(self):
        cleaned_data = super(InfantMaleGenitalAnomalyItemsForm, self).clean()
        if cleaned_data.get('male_genital_anomal') and not cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You indicated that participant has male genital anomaly and yet did not indicate the abnormality status. Please correct.')
        if not cleaned_data.get('male_genital_anomal') and cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You did NOT indicate the male genital anomaly and yet provided the abnormality status. Please correct.')

        return cleaned_data

    class Meta:
        model = InfantMaleGenitalAnomalyItems


class InfantRenalAnomalyItemsForm (BaseModelForm):
    def clean(self):
        cleaned_data = super(InfantRenalAnomalyItemsForm, self).clean()
        if cleaned_data.get('renal_amomalies') and not cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You indicated that participant has renal anomalies and yet did not indicate the abnormality status. Please correct.')
        if not cleaned_data.get('renal_amomalies') and cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You did NOT indicate the renal anomalies and yet provided the abnormality status. Please correct.')

        return cleaned_data

    class Meta:
        model = InfantRenalAnomalyItems


class InfantMusculoskeletalAbnormalItemsForm (BaseModelForm):
    def clean(self):
        cleaned_data = super(InfantMusculoskeletalAbnormalItemsForm, self).clean()
        if cleaned_data.get('musculo_skeletal') and not cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You indicated that participant has musculo skeletal anomaly and yet did not indicate the abnormality status. Please correct.')
        if not cleaned_data.get('musculo_skeletal') and cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You did NOT indicate the musculo skeletal anomaly and yet provided the abnormality status. Please correct.')

        return cleaned_data

    class Meta:
        model = InfantMusculoskeletalAbnormalItems


class InfantSkinAbnormalItemsForm (BaseModelForm):
    def clean(self):
        cleaned_data = super(InfantSkinAbnormalItemsForm, self).clean()
        if cleaned_data.get('skin_abnormality') and not cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You indicated that participant has skin anomaly and yet did not indicate the abnormality status. Please correct.')
        if not cleaned_data.get('skin_abnormality') and cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You did NOT indicate the skin anomaly and yet provided the abnormality status. Please correct.')

        return cleaned_data

    class Meta:
        model = InfantSkinAbnormalItems


class InfantTrisomiesChromosomeItemsForm (BaseModelForm):
    def clean(self):
        cleaned_data = super(InfantTrisomiesChromosomeItemsForm, self).clean()
        if cleaned_data.get('triso_chromo_abnormal') and not cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You indicated that participant has tri chromo anomaly and yet did not indicate the abnormality status. Please correct.')
        if not cleaned_data.get('triso_chromo_abnormal') and cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You did NOT indicate the tri chromo anomaly and yet provided the abnormality status. Please correct.')

        return cleaned_data

    class Meta:
        model = InfantTrisomiesChromosomeItems


class InfantOtherAbnormalityItemsForm (BaseModelForm):
    def clean(self):
        cleaned_data = super(InfantOtherAbnormalityItemsForm, self).clean()
        if cleaned_data.get('other_abnormalities') and not cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You indicated that participant has other abnormalities and yet did not indicate the abnormality status. Please correct.')
        if not cleaned_data.get('other_abnormalities') and cleaned_data.get('abnormality_status'):
            raise forms.ValidationError('You did NOT indicate the other abnormalities and yet provided the abnormality status. Please correct.')

        return cleaned_data

    class Meta:
        model = InfantOtherAbnormalityItems
