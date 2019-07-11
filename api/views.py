from django.shortcuts import render
from .models import Room, Flat, Flatmate, Record, CleanUp
from .serializers import FlatSerializer, RecordSerializer, FlatmateSerializer, RoomSerializer, CleanUpSerializer
from rest_framework import generics
from rest_framework import mixins
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


def load_clean(request):
    room_pk = request.GET.get('room_pk')
    # flat_pk = request.GET.get('flat_pk')
    # flat = Flat.objects.get(pk=flat_pk)
    room = Room.objects.get(pk=room_pk)
    cleans = CleanUp.objects.filter(room=room)
    return render(request, '../templates/admin/api/record/cleanup.html', {'cleans': cleans})


def load_points(request):
    clean_pk = request.GET.get('clean_pk')
    room_pk = request.GET.get('room_pk')
    room = Room.objects.get(pk=room_pk)
    clean = CleanUp.objects.filter(room=room).get(pk=clean_pk)
    return render(request, '../templates/admin/api/record/points.html', {'clean': clean})


def load_rooms(request):
    pk = request.GET.get('flat_pk')
    flat = Flat.objects.get(pk=pk)
    rooms = Room.objects.filter(flat=flat)
    return render(request, '../templates/admin/api/record/flat.html', {'rooms': rooms})


def load_flatmate(request):
    pk = request.GET.get('flat_pk')
    flat = Flat.objects.get(pk=pk)
    flatmates = Flatmate.objects.filter(flat=flat)
    return render(request, '../templates/admin/api/record/flatmate.html', {'flatmates': flatmates})
