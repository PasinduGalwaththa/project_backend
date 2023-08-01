from django.shortcuts import render
from .models import estate
from .serializers import estateSerializer , addEstateSerializer , EstateIdOnlyserializer
from rest_framework.decorators import APIView
from rest_framework.response import Response



# Create your views here.
class estateView(APIView):
    def get(self, request, estate_number, format=None):
        details = estate.objects.get(estate_number=estate_number)
        serializer = estateSerializer(details)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = estateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class AddStateView(APIView):
    def post(self, request, format=None):
        serializer = addEstateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self, request, format=None):
        details = estate.objects.all()
        serializer = addEstateSerializer(details, many=True)
        return Response(serializer.data)
    
class EstateIdOnlyView(APIView):
    def get(self, request, format=None):
        details = estate.objects.all()
        serializer = EstateIdOnlyserializer(details, many=True)
        return Response(serializer.data)
