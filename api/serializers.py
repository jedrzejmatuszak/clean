from rest_framework import serializers
from .models import Flat, Flatmate, Room, Record, CleanUp, User


class FlatSerializer(serializers.ModelSerializer):
    flat_details = serializers.HyperlinkedIdentityField(view_name='flat-detail')

    class Meta:
        model = Flat
        fields = ['id', 'name', 'flat_details']


class FlatDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flat
        fields = ['id', 'name', 'flatmates', 'rooms', 'flat_records']


class FlatmateSerializer(serializers.ModelSerializer):
    flatmate_details = serializers.HyperlinkedIdentityField(view_name='flatmate-detail')

    class Meta:
        model = Flatmate
        fields = ['id', 'user', 'flat', 'flatmate_details']


class FlatmateDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flatmate
        fields = ['id', 'user', 'flat', 'flatmate_records']


class RoomSerializer(serializers.ModelSerializer):
    room_details = serializers.HyperlinkedIdentityField(view_name='room-detail')

    class Meta:
        model = Room
        fields = ['id', 'name', 'flat', 'room_details']


class RoomDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id', 'name', 'flat', 'room_records']


class CleanUpSerializer(serializers.ModelSerializer):
    cleanup_details = serializers.HyperlinkedIdentityField(view_name='cleanup-detail')

    class Meta:
        model = CleanUp
        fields = ['id', 'name', 'points', 'room', 'cleanup_details']


class CleanUpDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CleanUp
        fields = ['id', 'name', 'room', 'points', 'cleanup_records']


class RecordSerializer(serializers.ModelSerializer):
    record_details = serializers.HyperlinkedIdentityField(view_name='record-detail')
    date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Record
        fields = ['id', 'flat', 'date', 'to_date', 'realized', 'record_details']


class RecordDetailSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Record
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    user_detail = serializers.HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'user_detail']


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password', ]
