from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import *

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
        context['lanes'] = Lane.objects.filter(board__number=self.kwargs['number'])
        context['cards'] = Card.objects.filter(lane__board__number=self.kwargs['number'])

        return context

    def get_object(self, **kwargs):
        board = Board.objects.get(number=self.kwargs['number'])
        return board

def board_detail_view(request, number):

    board = Board.objects.get(number=number)
    lanes = Lane.objects.filter(board__number=number)

    context = {
        'board' : board,
        'lanes' : lanes,
    }

    return render(request, 'board-detail.html', context)