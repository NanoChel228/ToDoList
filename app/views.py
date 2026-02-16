from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer, UserSerizalizer, AdminUserSerizalizer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from django.contrib.auth.models import User




# Create your views here.


# Регистрация пользователя

class ListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        task = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(task, many=True)


        return Response(serializer.data)


class CompletedAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        serializer = TaskSerializer(task, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class deleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task_id = task.title
        task.delete()

        return Response({
            'message': f'{task_id} delete'
        })

class createAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class patchGetUserID(APIView):
    # permission_classes = [IsAdminUser]

    def get(self, request, pk):
        users = get_object_or_404(User, pk=pk)
        serializer = AdminUserSerizalizer(users)

        return Response(serializer.data)

    def patch(self, request, pk):
        users = get_object_or_404(User, pk=pk)
        serializer = AdminUserSerizalizer(users, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


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