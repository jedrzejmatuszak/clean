from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import Room, Flat, Flatmate, Record, CleanUp
from .serializers import FlatSerializer, FlatDetailSerializer, RecordSerializer, FlatmateSerializer, \
    FlatmateDetailSerializer, RoomSerializer, RoomDetailSerializer, CleanUpSerializer, CleanUpDetailSerializer, \
    RecordDetailSerializer, UserSerializer, UserDetailSerializer, ChangePasswordSerializer, FlatmateSerializerViewset, \
    RoomSerializerViewset, CleanUpSerializerViewset, FlatSerializerViewset, RecordSerializerViewset, \
    UserSerializerViewset
from rest_framework import generics, permissions, status, viewsets


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
    serializer_class = FlatDetailSerializer


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
    serializer_class = FlatmateDetailSerializer


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
    serializer_class = RoomDetailSerializer


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
    serializer_class = CleanUpDetailSerializer


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
    serializer_class = RecordDetailSerializer


class UserList(generics.ListCreateAPIView):
    """
    List all users or create new user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, delete or update a user instance
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class ChangePasswordView(generics.UpdateAPIView):
    """
    Endpoint for changing password
    """
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password': 'Wrong password'}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlatViewset(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class =FlatSerializerViewset


class FlatmateViewset(viewsets.ModelViewSet):
    queryset = Flatmate.objects.all()
    serializer_class = FlatmateSerializerViewset


class RoomViewset(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializerViewset


class CleanUpViewset(viewsets.ModelViewSet):
    queryset = CleanUp.objects.all()
    serializer_class = CleanUpSerializerViewset


class RecordViewset(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializerViewset


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerViewset
