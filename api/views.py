from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import generics

from .serializers import *
from .utils import *

# Create your views here.


class UserList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BoardList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class LaneList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Lane.objects.all()
    serializer_class = LaneSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LaneDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Lane.objects.all()
    serializer_class = LaneSerializer


class CardList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    #Override create to return json response of all Card objects for a board
    def create(self, request, *args, **kwargs):
        save_card_serialized_request_data(request=request)
        cards_serialized = get_card_serialized_response(request=request)
        return JsonResponse(cards_serialized, safe=False)

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def update(self, request, *args, **kwargs):
        save_card_serialized_request_data(request=request, instance=self.get_object())
        cards_serialized = get_card_serialized_response(request=request)
        return JsonResponse(cards_serialized, safe=False)