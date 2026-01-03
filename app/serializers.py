from rest_framework import serializers
from .models import User, Task
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)


    def create(self, validated_data):
        return User.objects.create(**validated_data)
    