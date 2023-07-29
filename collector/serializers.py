from rest_framework import serializers
from planter.models import planter
from user.serializers import RegisterSerializer
from .models import collector

from .models import collector

class collectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = collector
        fields = '__all__'
        
class AddCustomerSerialier(serializers.ModelSerializer):
    
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password' , write_only=True)
    email = serializers.CharField(source='user.email')
    usertype = serializers.CharField(source='user.usertype')
    
    class Meta:
        model = collector
        fields = ('first_name','last_name','nic','address','telephone','username','password' , 'email' , 'usertype')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = RegisterSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        collector_prof = collector.objects.create(user=user, **validated_data)
        return collector_prof
    
   
       