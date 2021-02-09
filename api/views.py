from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import generics

from .serializers import *

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
    #permission_classes = (IsAuthenticated,)
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def create(self, request, *args, **kwargs):
        serializer = CardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        board_id=Lane.objects.get(id=request.data['lane']).board.id
        cards_serialized = CardSerializer(Card.objects.filter(lane__board__id=board_id).order_by('lane_timestamp'), many=True).data
        return JsonResponse(cards_serialized, safe=False)

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Card.objects.all()
    serializer_class = CardSerializer


