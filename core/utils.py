from .models import *


def get_adjacent_lane(lane, action):
    if action == 'next' and not lane.is_completed:
        adj_path = chr(ord(lane.path)+1)
    elif action == 'prev' and not lane.is_beginning:
        adj_path = chr(ord(lane.path)-1)

    return Lane.objects.get(board=lane.board, path=adj_path)


#Return last path +1 of lanes belonging to a board
def get_last_path_plus_one(lane):
    lanes = Lane.objects.filter(board=lane.board).order_by('path')

    if lanes:
        last_path = chr(ord(lanes.last().path)+1)
    else:
        last_path = 'A'

    return last_path


#Increment or decrement path fields of queryset
def insert_path(qs, action):
    for obj in qs:
        if action == 'increment' or action == 'plus' or action == 'add' or action == 'right':
            obj.path = chr(ord(obj.path)+1)
        elif action == 'decrement' or action == 'minus' or action == 'subtract' or action == 'left':
            obj.path = chr(ord(obj.path)-1)
        obj.save()


def get_card_form_lane_choices(card):
    lanes = Lane.objects.filter(board=card.lane.board).order_by('path')
    choices = [(lane.id, lane.number) for lane in lanes]
    return choices