from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


# Create your views here.


# Регистрация пользователя

class createListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class createAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class test(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):

        users = request.user.id
        username = request.user.username

        return Response({
            'message': 'hello World',
            'users': users,
            'username': username,
        })