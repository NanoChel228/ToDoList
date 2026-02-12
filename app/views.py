from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated


# Create your views here.


# Регистрация пользователя
class registration(APIView):
    
    def post(self, request):

        username = User.objects.filter(username=request.data.get("username"))

        if username:
            return Response({"message": "This user already exists"}, status=200)
            # return redirect("authorization")
        else:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()


        return Response({"message": "User created successfully"}, status=201)
    

    def get(self, request):
        users = User.objects.all()
        return Response({"users": UserSerializer(users, many=True).data})
    
    

# Авторизация пользователя
class authorization(APIView):

    def post(self, request):

        data = User.objects.filter(username=request.data.get("username"), password=request.data.get("password"))

        if data:
            return Response({
                "message": "Authorization successfull",

            }, status=200)
        
        else:
            return Response({
                "message": "Invalid username or password"
                
            }, status=401)


class test(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):

        return Response({
            'message': 'hello World'
        })