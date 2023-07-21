from rest_framework.serializers import ModelSerializer
from .models import payments

class paymentsSerializer(ModelSerializer):
    class Meta:
        model = payments
        fields = '__all__'
        
        