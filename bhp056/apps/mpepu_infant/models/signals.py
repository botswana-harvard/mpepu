from django.db.models.signals import post_save
from django.dispatch import receiver
from infant_birth import InfantBirth
from infant_eligibility import InfantEligibility
from infant_pre_eligibility import InfantPreEligibility


@receiver(post_save, weak=False, dispatch_uid='infant_birth_data_on_post_save')
def infant_birth_data_on_post_save(sender, instance, **kwargs):
    if isinstance(instance, (InfantBirth, InfantPreEligibility)):
        instance.post_save_recalculate_appt_date()


@receiver(post_save, weak=False, dispatch_uid='infant_eligibility_post_save_delete_appointment')
def infant_eligibility_post_save_delete_appointment(sender, instance, **kwargs):
    if isinstance(instance, (InfantEligibility)):
        instance.post_save_delete_appointment()
