from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    user_detail = serializers.HyperlinkedIdentityField(view_name='customuser-detail')
    password = serializers.ReadOnlyField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'first_name', 'is_parent', 'is_active', 'user_detail']


class CustomUserDetailSerializer(serializers.ModelSerializer):
    flatmate = serializers.HyperlinkedIdentityField(view_name='flatmate-detail')

    class Meta:
        model = CustomUser
        exclude = ['password', 'groups', 'user_permissions']


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
