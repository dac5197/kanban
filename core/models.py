from django.db import models
from django.db.models import CharField
from django.db.models.functions import Length
from django.utils import timezone


# Create your models here.

#Register 'Length' transfer for Charfield to allow queryset filtering by char length
#https://stackoverflow.com/a/45260608
CharField.register_lookup(Length, 'length')

#Generate and incement numbers for models
#Example: BRD0000001
def format_number(prefix, id):
    number = prefix + str(id).zfill(7)
    return number

def increment_board_number():
    try:
        number = Board.objects.all().order_by('number').last().number
        last_id = int(number[-7:])
        last_id += 1
    except:
        last_id = 1
    return format_number('BRD', last_id)

def increment_lane_number():
    try:
        number = Lane.objects.all().order_by('number').last().number
        last_id = int(number[-7:])
        last_id += 1
    except:
        last_id = 1
    return format_number('LANE', last_id)

def increment_card_number():
    try:
        number = Card.objects.all().order_by('number').last().number
        last_id = int(number[-7:])
        last_id += 1
    except:
        last_id = 1
    return format_number('CRD', last_id)


class Priority(models.Model):
    value = models.IntegerField(unique=True, null=False, blank=False)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    default_value = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    @property
    def priority(self):
        return str(self.value) + " - " + str(self.name)
    
    class Meta:
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.priority


class Board(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    number = models.CharField(max_length=20, unique=True, default=increment_board_number)
    created = models.DateTimeField(default=timezone.now, null=False, blank=False)
    updated = models.DateTimeField(default=timezone.now, null=False, blank=False)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='boards', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.number


class Lane(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    number = models.CharField(max_length=20, unique=True, default=increment_lane_number)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, blank=True)
    path = models.CharField(max_length=25, blank=True, null=True)
    is_worked = models.BooleanField(default=False)
    is_beginning = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    queue_max = models.IntegerField(default=None, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, null=False, blank=False)
    updated = models.DateTimeField(default=timezone.now, null=False, blank=False)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='lanes', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.number

    @property
    def has_children(self):
        children = Lane.objects.filter(path__startswith=self.path, path__length=len(self.path)+1)
        children = children.exclude(path=self.path)

        if children.exists():
            return True
        else:
            return False

    @property
    def parent(self):
        parent = Lane.objects.get(path=self.path[:-1], board__id=self.board.id)
        return parent.name


class Card(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    number = models.CharField(max_length=20, unique=True, default=increment_card_number)
    description = models.TextField(null=True, blank=True)
    lane = models.ForeignKey(Lane, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, default= 4, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, null=False, blank=False)
    updated = models.DateTimeField(default=timezone.now, null=False, blank=False)
    lane_timestamp = models.DateTimeField(default=timezone.now, null=False, blank=False)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='cards', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.number

    @property
    def lane_location(self):
        if self.lane.is_beginning:
            loc = 'start'
        elif self.lane.is_completed:
            loc = 'end'
        else:
            loc = 'middle'

        return loc

    @property
    def lane_is_worked(self):
        return self.lane.is_worked

    @property
    def board(self):
        return self.lane.board