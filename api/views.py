from django.contrib.auth.models import User
from django.http import Http404
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
        try:
            queryset = Flat.objects.get(pk=pk)
            serializer = FlatDetailSerializer(queryset)
            return Response(serializer.data)
        except Flat.DoesNotExist:
            raise Http404


class FlatmateViewSet(viewsets.ModelViewSet):
    queryset = Flatmate.objects.all()
    serializer_class = FlatmateSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            queryset = Flatmate.objects.get(pk=pk)
            serializer = FlatmateDetailSerializer(queryset)
            return Response(serializer.data)
        except Flatmate.DoesNotExist:
            raise Http404


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            queryset = Room.objects.get(pk=pk)
            serializer = RoomDetailSerializer(queryset)
            return Response(serializer.data)
        except Room.DoesNotExist:
            raise Http404


class CleanUpViewSet(viewsets.ModelViewSet):
    queryset = CleanUp.objects.all()
    serializer_class = CleanUpSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            queryset = CleanUp.objects.get(pk=pk)
            serializer = CleanUpDetailSerializer(queryset)
            return Response(serializer.data)
        except CleanUp.DoesNotExist:
            raise Http404


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            queryset = Record.objects.get(pk=pk)
            serializer = RecordDetailSerializer(queryset)
            return Response(serializer.data)
        except Record.DoesNotExist:
            raise Http404


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            queryset = User.objects.get(pk=pk)
            serializer = UserDetailSerializer(self.queryset, pk=pk)
            return Response(serializer.data)
        except User.DoesNotExist:
            raise Http404
