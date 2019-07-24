from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import Room, Flat, Flatmate, Record, CleanUp
from .serializers import FlatSerializer, FlatDetailSerializer, RecordSerializer, FlatmateSerializer, \
    FlatmateDetailSerializer, RoomSerializer, RoomDetailSerializer, CleanUpSerializer, CleanUpDetailSerializer, \
    RecordDetailSerializer, UserSerializer, UserDetailSerializer
from rest_framework import generics, permissions, status, viewsets


# Create your views here.


class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        serializer = FlatDetailSerializer(self.queryset, pk=pk)
        return Response(serializer.data)


class FlatmateViewSet(viewsets.ModelViewSet):
    queryset = Flatmate.objects.all()
    serializer_class = FlatmateSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        serializer = FlatmateDetailSerializer(self.queryset, pk=pk)
        return Response(serializer.data)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        serializer = RoomDetailSerializer(self.queryset, pk=pk)
        return Response(serializer.data)


class CleanUpViewSet(viewsets.ModelViewSet):
    queryset = CleanUp.objects.all()
    serializer_class = CleanUpSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        serializer = CleanUpDetailSerializer(self.queryset, pk=pk)
        return Response(serializer.data)


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        serializer = RecordDetailSerializer(self.queryset, pk=pk)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        serializer = UserDetailSerializer(self.queryset, pk=pk)
        return Response(serializer.data)
