from rest_framework import serializers
from .models import payments

class paymentsSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = payments
        fields = [ 'date', 'calculated_amount' , 'id', 'gross_weight' , 'planter']
        
    
        
class paymentsAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = payments
        fields = '__all__'
        
        
class PaymentsViewSerializer(serializers.ModelSerializer):
    
    planter = serializers.CharField(source='planter.first_name')
    class Meta:
        model = payments
        fields = '__all__'
        
class PaymentsGotPaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = payments
        fields = ['got_paid']

class PaymentsTransferredSerializer(serializers.ModelSerializer):
    class Meta:
        model = payments
        fields = ['transferred']
        
        
class PaymentsDateAmount(serializers.ModelSerializer):
    
    class Meta:
        model = payments
        fields = ['date' , 'calculated_amount']
        
class PaymentsDateWeight(serializers.ModelSerializer):
    
    class Meta:
        model = payments
        fields = ['date' , 'gross_weight']