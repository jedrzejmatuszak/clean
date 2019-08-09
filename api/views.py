from django.http import Http404
from rest_framework.response import Response
from .models import Room, Flat, Flatmate, Record, CleanUp
from .serializers import FlatSerializer, FlatDetailSerializer, RecordSerializer, FlatmateSerializer, \
    FlatmateDetailSerializer, RoomSerializer, RoomDetailSerializer, CleanUpSerializer, CleanUpDetailSerializer, \
    RecordDetailSerializer, CreateRecordSerializer
from rest_framework import generics, permissions, status, viewsets


# Create your views here.


class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
    permission_classes = (permissions.IsAuthenticated,)

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
    permission_classes = (permissions.IsAuthenticated,)

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
    permission_classes = (permissions.IsAuthenticated,)

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
    permission_classes = (permissions.IsAuthenticated,)

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
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = CreateRecordSerializer(data=request.data)
        if serializer.is_valid():
            new_record = Record.objects.create(
                flat=serializer.validated_data['flat'],
                room=serializer.validated_data['room'],
                cleanup=serializer.validated_data['cleanup'],
                flatmate=serializer.validated_data['flatmate'],
                to_date=serializer.validated_data['to_date'],
                author=serializer.validated_data['author'],
            )
            return Response(RecordDetailSerializer(new_record).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            queryset = Record.objects.get(pk=pk)
            serializer = RecordDetailSerializer(queryset)
            return Response(serializer.data)
        except Record.DoesNotExist:
            raise Http404
