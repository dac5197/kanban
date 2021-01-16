from django.shortcuts import render
from django.views.generic.list import ListView

from .models import *

# Create your views here.


class BoardListView(ListView):
    models = Board
    template_name = 'index.html'
    context_object_name = 'boards'

    def get_queryset(self):
        queryset = Board.objects.filter(owner=self.request.user)
        return queryset