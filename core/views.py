from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from api.serializers import *

from .models import *
from .utils import *

# Create your views here.


class BoardListView(ListView):
    models = Board
    template_name = 'index.html'
    context_object_name = 'boards'

    def get_queryset(self):
        queryset = Board.objects.filter(owner=self.request.user).order_by('number')
        return queryset


class BoardDetailView(DetailView):
    models = Board
    template_name = 'board-detail.html'
    context_object_name = 'board'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lanes = Lane.objects.filter(board__number=self.kwargs['number'])
        context['lanes'] = lanes
        context['lanes_serialized'] = LaneSerializer(lanes, many=True).data
        cards = Card.objects.filter(lane__board__number=self.kwargs['number']).order_by('lane_timestamp')
        context['cards'] = cards
        context['cards_serialized'] = CardSerializer(cards, many=True).data

        return context

    def get_object(self, **kwargs):
        board = Board.objects.get(number=self.kwargs['number'])
        return board


def card_change_lane_view(request, board_id, action, card_id):
    if request.method == 'POST':
        card = Card.objects.get(id=card_id)

        if card.lane.board.id == board_id:

            card.lane = get_adjacent_lane(lane=card.lane, action=action)
            card.save()
        
    cards_serialized = CardSerializer(Card.objects.filter(lane__board__id=board_id).order_by('lane_timestamp'), many=True).data
    
    return JsonResponse(cards_serialized, safe=False)




def board_detail_view(request, number):

    board = Board.objects.get(number=number)
    lanes = Lane.objects.filter(board__number=number)

    context = {
        'board' : board,
        'lanes' : lanes,
    }

    return render(request, 'board-detail.html', context)