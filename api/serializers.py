from rest_framework import serializers
from .models import Flat, Flatmate, Room, Record, CleanUp


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = '__all__'


class FlatmateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flatmate
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class CleanUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleanUp
        fields = '__all__'
