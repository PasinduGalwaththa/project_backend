from django.shortcuts import render
from .models import SetArrivals
from .serializers import SetArrivalsSerializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import DestroyAPIView

# Create your views here.


@api_view(['GET', 'POST', 'DELETE'])
def SetArrivals_view(request,pk=None):
    if request.method == 'GET':
        queryset = SetArrivals.objects.all()
        serializer = SetArrivalsSerializers(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SetArrivalsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print(request)
        SetArrivals.objects.get(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    

# class SetArrivalsDeleteView(DestroyAPIView):
    # queryset = SetArrivals.objects.all()
    # serializer_class = SetArrivalsSerializers
    
    

    
class DetailByDayView(APIView):
    def get(self, request, day, format=None):
        details = SetArrivals.objects.filter(day=day)
        serializer = SetArrivalsSerializers(details, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SetArrivalsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
     

# Create your views here.
