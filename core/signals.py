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


#For first lane for lanes belonging to board, set is_beginning to true and set to false for all other lanes
@receiver(post_save, sender=Lane)
def post_save_set_is_beginning(sender, instance, **kwargs):
    lanes = Lane.objects.filter(board=instance.board).order_by('path')
    first_lane = lanes.first()
    lanes.filter(id=first_lane.id).update(is_beginning=True)
    lanes.exclude(id=first_lane.id).update(is_beginning=False)


#For last lane for lanes belonging to board, set is_completed to true and set to false for all other lanes
@receiver(post_save, sender=Lane)
def post_save_set_is_completed(sender, instance, **kwargs):
    lanes = Lane.objects.filter(board=instance.board).order_by('path')
    last_lane = lanes.last()
    lanes.filter(id=last_lane.id).update(is_completed=True)
    lanes.exclude(id=last_lane.id).update(is_completed=False)