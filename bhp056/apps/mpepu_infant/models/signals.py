from django.db.models.signals import post_save
from django.dispatch import receiver

from .infant_birth import InfantBirth
from .infant_eligibility import InfantEligibility
from .infant_pre_eligibility import InfantPreEligibility
from .infant_visit import InfantVisit


@receiver(post_save, weak=False, dispatch_uid='infant_birth_data_on_post_save')
def infant_birth_data_on_post_save(sender, instance, **kwargs):
    if isinstance(instance, (InfantBirth, InfantPreEligibility)):
        instance.post_save_recalculate_appt_date()

# @receiver(post_save, weak=False, dispatch_uid='infant_eligibility_post_save_delete_appointment')
# def infant_eligibility_post_save_delete_appointment(sender, instance, **kwargs):
#     if isinstance(instance, (InfantEligibility)):
#         instance.post_save_delete_appointment()


# @receiver(post_save, weak=False, dispatch_uid="infant_eligibility_on_post_save")
# def infant_eligibility_on_post_save(sender, instance, raw, created, using, **kwargs):
#     """"""
#     if isinstance(instance, (InfantEligibility)):
#         instance.prepare_appointments(using)


@receiver(post_save, weak=False, dispatch_uid='post_save_recalculate_appts')
def post_save_recalculate_appts(sender, instance, **kwargs):
    if isinstance(instance, (InfantEligibility)):
        instance.post_save_recalculate_maternal_appts()
        
@receiver(post_save, weak=False, dispatch_uid='mpepu_cessation_post_save')
def mpepu_cessation_post_save(sender, instance, **kwargs):
    if isinstance(instance, (InfantVisit)):
        instance.mpepu_cessation_post_save()
    