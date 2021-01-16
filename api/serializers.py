from django.contrib.auth.models import User

from rest_framework import serializers

from core.models import *


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    number = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()
    active = serializers.ReadOnlyField()

    class Meta:
        model = Board
        fields = [
            'id', 
            'name', 
            'number', 
            'created', 
            'updated', 
            'active',
            'owner',
        ]


class LaneSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    number = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()
    active = serializers.ReadOnlyField()
    has_children = serializers.ReadOnlyField()
    parent = serializers.ReadOnlyField()

    class Meta:
        model = Lane
        fields = [
            'id', 
            'name', 
            'number',
            'board', 
            'path', 
            'is_worked', 
            'is_beginning',
            'is_completed',
            'queue_max',
            'has_children',
            'parent',
            'created',
            'updated',
            'active',
            'owner',
        ]


class CardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    number = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()
    active = serializers.ReadOnlyField()

    class Meta:
        model = Card
        fields = [
            'id', 
            'name', 
            'number', 
            'lane',
            'description',
            'priority',
            'created', 
            'updated', 
            'active',
            'owner',
        ]


class UserSerializer(serializers.ModelSerializer):
    boards = serializers.PrimaryKeyRelatedField(many=True, queryset=Board.objects.all())
    lanes = serializers.PrimaryKeyRelatedField(many=True, queryset=Lane.objects.all())
    cards = serializers.PrimaryKeyRelatedField(many=True, queryset=Card.objects.all())

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'boards',
            'lanes',
            'cards',
        ]