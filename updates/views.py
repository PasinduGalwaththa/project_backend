from django.shortcuts import render
from .models import updates
from .serializers import UpdatesSerializer , GetupdatesbyPlantIDdSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from planter.models import planter
# Create your views here.

@api_view(['GET', 'POST'])
def updates_view(request):
    if request.method == 'GET':
        queryset = updates.objects.all()
        serializer = UpdatesSerializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UpdatesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Getupdatesbyd(APIView):
    def get(self, request, planter_id, format=None):
        queryset = updates.objects.filter(planter_id=planter_id)
        serializer = GetupdatesbyPlantIDdSerializer(queryset, many=True)
        return Response(serializer.data)
    

        