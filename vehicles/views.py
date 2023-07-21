from django.shortcuts import render
from .models import vehicles
from .serializers import vehiclesSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class paymentsView(APIView):
    def get(self, request, format=None):
        queryset = vehicles.objects.all()
        serializer = vehiclesSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = vehiclesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)