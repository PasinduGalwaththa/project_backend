from django.shortcuts import render, get_object_or_404
from .models import planter
from .serializers import planterSerializer, planterSerializerBasic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from estate.models import estate
from estate.serializers import estateSerializer

# ... Your other code ...

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

class EstateNumberView(APIView):
    def get(self, request, estate_number, format=None):
        estate_obj = get_object_or_404(estate, id=estate_number)
        planters = planter.objects.filter(estate=estate_obj)
        serializer = planterSerializerBasic(planters, many=True)
        return Response(serializer.data)

# ... Your other code ...
