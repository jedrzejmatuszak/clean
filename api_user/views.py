from django.http import Http404
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserDetailSerializer, CreateUserSerializer
# Create your views here.


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            CustomUser.objects.create_user(
                    username=serializer.validated_data['username'],
                    email=serializer.validated_data['email'],
                    password=serializer.validated_data['password']
                )
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            queryset = CustomUser.objects.get(pk=pk)
            serializer = CustomUserDetailSerializer(queryset, context={'request': request})
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            raise Http404
