from django.shortcuts import render
from .models import payments
from .serializers import paymentsSerializer , paymentsAddSerializer , PaymentsViewSerializer , PaymentsDateWeight , PaymentsDateAmount
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max

# Create your views here.

class paymentsView(APIView):
    def get(self, request, format=None):
        queryset = payments.objects.all()
        serializer = paymentsSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = paymentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        
        try:
            payment = payments.objects.get(pk=pk)
        except payments.DoesNotExist:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = paymentsAddSerializer(payment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetListByPlanterId(APIView):
    def get(self, request, planter_id, format=None):
        queryset = payments.objects.filter(planter_id=planter_id)
        serializer = PaymentsViewSerializer(queryset, many=True)
        return Response(serializer.data)
    
class PaymentsGetAmount(APIView):
    def get(self, request, format=None):
        latest_records_pks = payments.objects.values('gross_weight').annotate(latest_pk=Max('pk')).values_list('latest_pk', flat=True)

        # Get the actual records using the primary keys
        queryset = payments.objects.filter(pk__in=latest_records_pks)

        serializer = PaymentsDateAmount(queryset, many=True)
        return Response(serializer.data)
    
class PaymentsGetWeigth(APIView):
    def get(self, request, format=None):
        latest_records_pks = payments.objects.values('gross_weight').annotate(latest_pk=Max('pk')).values_list('latest_pk', flat=True)

        # Get the actual records using the primary keys
        queryset = payments.objects.filter(pk__in=latest_records_pks)

        serializer = PaymentsDateWeight(queryset, many=True)
        return Response(serializer.data)
    