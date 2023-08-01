from django.shortcuts import render, get_object_or_404
from .models import planter
from .serializers import planterSerializer, planterSerializerBasic , AddPlanterSerializer , PlanterSerializerAdd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from estate.models import estate
from estate.serializers import estateSerializer
from user.models import Customuser
from teatype.models import Teatype
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

# ... Your other code ...

@csrf_exempt
@api_view(['GET', 'POST'])
def planter_view(request):
    if request.method == 'GET':
        queryset = planter.objects.all()
        serializer = AddPlanterSerializer(queryset, many=True)
        return Response(serializer.data)

def planter_view(request):
    if request.method == 'GET':
        queryset = planter.objects.all()
        serializer = AddPlanterSerializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AddPlanterSerializer(data=request.data)
        if serializer.is_valid():
            # Ensure the provided usertype is 'planter'
            if serializer.validated_data['user']['usertype'] != 'planter':
                return Response({'error': 'Invalid user type'}, status=status.HTTP_400_BAD_REQUEST)

            # Create or get the Customuser object based on the provided username
            user_data = serializer.validated_data.pop('user')
            user, _ = Customuser.objects.get_or_create(username=user_data['username'])
            user.email = user_data['email']
            user.set_password(user_data['password'])
            user.usertype = 'planter'
            user.save()

            # Get or create the Estate object based on the provided estatename
            estatename = serializer.validated_data['estate']['estatename']
            estate_obj, _ = estate.objects.get_or_create(estatename=estatename)

            # Save the planter object with the correct estate and user
            serializer.save(user=user, estate=estate_obj)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class EstateNumberView(APIView):
    def get(self, request, estate_id, format=None):
        estate_obj = get_object_or_404(estate, id=estate_id)
        planters = planter.objects.get(estate=estate_obj)
        serializer = planterSerializerBasic(planters)
        return Response(serializer.data)

# ... Your other code ...

class PlanterIDview(APIView):
    def get(self, request, id, format=None):
        queryset = planter.objects.get(user_id=id)
        serializer = planterSerializerBasic(queryset)
        return Response(serializer.data)
    
    
class AddPlanterView(generics.CreateAPIView):
    queryset = planter.objects.all()
    serializer_class = AddPlanterSerializer
    
class AddPlanter(APIView):
    def post(self, request, format=None):
        serializer = AddPlanterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        details = planter.objects.all()
        serializer = AddPlanterSerializer(details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class PlanterDetail(APIView):
    def post(self, request, format=None):
        serializer = PlanterSerializerAdd(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        details = planter.objects.all()
        serializer = PlanterSerializerAdd(details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)