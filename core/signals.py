from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

from .models import *
from .utils import *


@receiver(pre_save, sender=Board)
@receiver(pre_save, sender=Lane)
@receiver(pre_save, sender=Card)
def pre_save_set_updated_timestamp(sender, instance, **kwargs):
    instance.updated = timezone.now()

@receiver(pre_save, sender=Card)
def pre_save_set_lane_change_timestamp(sender, instance, **kwargs):
    init_obj = Card.objects.get(id=instance.id)
    if instance.lane != init_obj.lane:
        instance.lane_timestamp = timezone.now()


'''
@receiver(post_save, sender=Board)
@receiver(post_save, sender=Lane)
@receiver(post_save, sender=Card)
def post_save_create_number(sender, instance, created, **kwargs):
    if created:
        number = create_number(obj=instance)
        print(number)
        print(type(number))
        type(instance).objects.filter(id=instance.id).update(number=number)
'''