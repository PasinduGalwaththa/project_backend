from django.shortcuts import render
from rest_framework.decorators import api_view
from collector.models import collector
from .serializers import collectorSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def collector_view(request):
    if request.method == 'GET':
        queryset = collector.objects.all()
        serializer = collectorSerializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = collectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET']) 
