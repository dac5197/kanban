from .models import *


def get_adjacent_lane(lane, action):
    if action == 'next' and not lane.is_completed:
        adj_path = chr(ord(lane.path)+1)
    elif action == 'prev' and not lane.is_beginning:
        adj_path = chr(ord(lane.path)-1)

    return Lane.objects.get(board=lane.board, path=adj_path)

