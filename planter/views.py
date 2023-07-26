from django.shortcuts import render, get_object_or_404
from .models import planter
from .serializers import planterSerializer, planterSerializerBasic , AddPlanterSerializer
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
        serializer = planterSerializerBasic(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = planterSerializerBasic(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstateNumberView(APIView):
    def get(self, request, estate_id, format=None):
        estate_obj = get_object_or_404(estate, id=estate_id)
        planters = planter.objects.filter(estate=estate_obj)
        serializer = planterSerializerBasic(planters, many=True)
        return Response(serializer.data)

# ... Your other code ...
class PlanterView(APIView):
    
    def get(self, request):
        queryset = planter.objects.all()
        serializer = AddPlanterSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AddPlanterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)