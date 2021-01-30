from .models import *


def get_adjacent_lane(lane, action):
    if action == 'next' and not lane.is_completed:
        adj_path = chr(ord(lane.path)+1)
    elif action == 'prev' and not lane.is_beginning:
        adj_path = chr(ord(lane.path)-1)

    return Lane.objects.get(board=lane.board, path=adj_path)


#Return last path +1 of lanes belonging to a board
def get_last_path(lane):
    lanes = Lane.objects.filter(board=lane.board).order_by('path')

    if lanes:
        last_path = chr(ord(lanes.last().path)+1)
    else:
        last_path = 'A'

    return last_path


#Increment lane paths to accomodate new inserted lane
def insert_path(lane):
    lanes = Lane.objects.filter(path__gte=lane.path).exclude(id=lane.id)
    for lane in lanes:
        lane.path = chr(ord(lane.path)+1)
        lane.save()