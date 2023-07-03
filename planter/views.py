from django.shortcuts import render
from .models import planter
from .serializers import planterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def planter_view(request):
    if request.method == 'GET':
        queryset = planter.objects.all()
        serializer = planterSerializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = planterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class planter_view(APIView):
#     def get(self , request):
#         output = [{'first_name', 'last_name', 'address' , 'telephone', 'nic'}
#                   for output in planter.objects.raw('SELECT * FROM planter_planter')]
#         return Response(output)
        
#     def post(self , request):
#         serializer = planterSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)   