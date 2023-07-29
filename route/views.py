from django.shortcuts import render
from .models import Route

# Create your views here.
# views.py
from rest_framework import generics
from .models import Route
from .serializers import RouteSerializer

class RouteListCreateView(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class RouteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
