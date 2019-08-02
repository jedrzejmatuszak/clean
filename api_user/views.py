import requests
from django.http import Http404
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
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
        if str(request.user.pk) == pk:
            try:
                queryset = CustomUser.objects.get(pk=pk)
                serializer = CustomUserDetailSerializer(queryset, context={'request': request})
                return Response(serializer.data)
            except CustomUser.DoesNotExist:
                raise Http404
        elif request.user.is_staff:
            try:
                queryset = CustomUser.objects.get(pk=pk)
                serializer = CustomUserDetailSerializer(queryset, context={'request': request})
                return Response(serializer.data)
            except CustomUser.DoesNotExist:
                raise Http404
        else:
            return Response({'details': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdminUser, ]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated, ]
        elif self.action == 'list':
            permission_classes = [AllowAny, ]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]


class UserActivationView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, uid, token):
        payload = {'uid': uid, 'token': token}
        protocol = "https://" if request.is_secure() else "http://"
        url = protocol + request.get_host() + reverse('customuser-activation')
        response = requests.post(url, data=payload)
        if response.status_code == 204:
            return Response({'is_active': True})
        else:
            return Response({'is_active': False}, status=status.HTTP_400_BAD_REQUEST)
