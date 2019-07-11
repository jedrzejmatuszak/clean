from .models import Room, Flat, Flatmate, Record, CleanUp
from .serializers import FlatSerializer, RecordSerializer, FlatmateSerializer, RoomSerializer, CleanUpSerializer
from rest_framework import generics
# Create your views here.


class FlatList(generics.ListCreateAPIView):
    """
    List all flats or create new flat
    """
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, delete or update a flat instance
    """
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatmateList(generics.ListCreateAPIView):
    """
    List all flatmates or create new flatmate
    """
    queryset = Flatmate.objects.all()
    serializer_class = FlatmateSerializer


class FlatmateDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, delete or update a flatmate instance
    """
    queryset = Flatmate.objects.all()
    serializer_class = FlatmateSerializer


class RoomList(generics.ListCreateAPIView):
    """
    List all rooms or create new room
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, delete or update a room instance
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CleanUpList(generics.ListCreateAPIView):
    """
    List all cleanups or create new cleanup
    """
    queryset = CleanUp.objects.all()
    serializer_class = CleanUpSerializer


class CleanUpDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, delete or update a cleanup instance
    """
    queryset = CleanUp.objects.all()
    serializer_class = CleanUpSerializer


class RecordList(generics.ListCreateAPIView):
    """
    List all records or create new record
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, delete or update a record instance
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
