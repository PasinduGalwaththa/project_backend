from django.shortcuts import render
from .models import Route , RouteDetails
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
# views.py
from rest_framework import generics
from .models import Route
from .serializers import RouteSerializer , RouteDetailsSerializer

class RouteListCreateView(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class RouteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    
class RouteDetailsListCreateView(generics.ListCreateAPIView):
    serializer_class = RouteDetailsSerializer
    
    def get_queryset(self):
        return RouteDetails.objects.all()
    
    def post(self, request, format=None):
        serializer = RouteDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
