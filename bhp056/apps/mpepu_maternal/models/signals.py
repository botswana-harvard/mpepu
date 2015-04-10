from django.db.models.signals import post_save
from django.dispatch import receiver

from .maternal_lab_del import MaternalLabDel
from .maternal_visit import MaternalVisit


@receiver(post_save, weak=False, dispatch_uid='post_save_register_infants')
def post_save_register_infants(sender, instance, raw, created, using, **kwarg):
    if isinstance(instance, MaternalLabDel):
        instance.post_save_register_infants(created)

@receiver(post_save, weak=False, dispatch_uid='maternal_mpepu_cessation_post_save')
def maternal_mpepu_cessation_post_save(sender, instance, **kwargs):
    if isinstance(instance, (MaternalVisit)):
        instance.maternal_mpepu_cessation_post_save()