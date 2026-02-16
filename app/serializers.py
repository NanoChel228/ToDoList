from rest_framework import serializers
from .models import Task
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class AdminUserSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):

    user = UserSerizalizer(read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'user', 'completed']
        read_only_fields = ['user']
        

    def create(self, validated_data):
        return Task.objects.create(
            user=self.context['request'].user,
            **validated_data
        )