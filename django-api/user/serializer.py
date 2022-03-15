from rest_framework import serializers
from .models import *
from .views import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['created_at', 'modified_at', 'password', 'last_login',
                   'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions', ]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
    