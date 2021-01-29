from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

from .models import *
from .utils import *


#Set updated timestamp each time model is saved
@receiver(pre_save, sender=Board)
@receiver(pre_save, sender=Lane)
@receiver(pre_save, sender=Card)
def pre_save_set_updated_timestamp(sender, instance, **kwargs):
    instance.updated = timezone.now()

#Set lane timestamp when card changes lane
@receiver(pre_save, sender=Card)
def pre_save_set_lane_change_timestamp(sender, instance, **kwargs):
    init_obj = Card.objects.get(id=instance.id)
    if instance.lane != init_obj.lane:
        instance.lane_timestamp = timezone.now()

#Set lane is_beginning to True if lane path is first
@receiver(pre_save, sender=Lane)
def pre_save_set_is_beginning(sender, instance, **kwargs):
    first_lane = Lane.objects.filter(board=instance.board).order_by('path').first()
    if first_lane == instance or first_lane == None:
        instance.is_beginning=True

#Set lane is_completed to True if lane path is last
#Set is_completed to False for all other lanes for that board
@receiver(pre_save, sender=Lane)
def pre_save_set_is_completed(sender, instance, **kwargs):
    lanes = Lane.objects.filter(board=instance.board).order_by('path')
    if lanes:
        if instance.path > lanes.last().path:
            instance.is_completed=True
            lanes.exclude(id=instance.id).update(is_completed=False)

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