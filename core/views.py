from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
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


class BoardCreateView(CreateView):
    model = Board
    template_name = 'board-create.html'
    fields = ['name']
    success_url = '/{number}'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


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
        #return Board.objects.get(number=self.kwargs['number'])
        return get_object_or_404(Board, number=self.kwargs['number'])


class LaneCreateView(CreateView):
    model = Lane
    template_name = 'lane-create.html'
    fields = ['name', 'path', 'is_worked', 'queue_max',]
    success_url = '/{number}'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

def card_change_lane_view(request, board_id, action, card_id):
    if request.method == 'POST':
        card = Card.objects.get(id=card_id)

        if card.lane.board.id == board_id:

            card.lane = get_adjacent_lane(lane=card.lane, action=action)
            card.save()
        
    cards_serialized = CardSerializer(Card.objects.filter(lane__board__id=board_id).order_by('lane_timestamp'), many=True).data
    
    return JsonResponse(cards_serialized, safe=False)


def create_defualt_lanes(request, number):
    #Get board
    board = Board.objects.get(number=number)

    #Create First Lane    
    Lane.objects.create(board=board, name='To Do', path='A', owner=request.user)
    #Create Second Lane    
    Lane.objects.create(board=board, name='Working', path='B', owner=request.user, queue_max=3, is_worked=True)
    #Create Third Lane    
    Lane.objects.create(board=board, name='Completed', path='C', owner=request.user)

    return redirect('board-detail', number=number)


def board_detail_view(request, number):
    #Get board
    board = Board.objects.get(number=number)

    #Get lanes and serialized lanes for board
    lanes = Lane.objects.filter(board__number=number)
    lanes_serialized = LaneSerializer(lanes, many=True).data

    #Get cards and serialized cards for board
    cards = Card.objects.filter(lane__board__number=number).order_by('lane_timestamp')
    cards_serialized = CardSerializer(cards, many=True).data

    context = {
        'board' : board,
        'lanes' : lanes,
        'lanes_serialized' : lanes_serialized,
        'cards' : cards,
        'cards_serialized' : cards_serialized,
    }

    return render(request, 'board-detail.html', context)