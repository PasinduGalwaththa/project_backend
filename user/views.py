from django.shortcuts import render
from rest_framework import generics, permissions
from user.models import Customuser
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
class UserView(generics.ListAPIView):
    serializer_class = RegisterSerializer
    
    def get_queryset(self):
        
        return Customuser.objects.all()
    
    def post(self,request):
        serializer = RegisterSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        
        