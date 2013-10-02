from django.db.models.signals import post_save
from django.dispatch import receiver
from mpepu_maternal.models import MaternalLabDel


@receiver(post_save, weak=False, dispatch_uid='post_save_register_infants')
def post_save_register_infants(sender, instance, raw, created, using, **kwarg):
    if isinstance(instance, MaternalLabDel):
        instance.post_save_register_infants(created)
