from rest_framework import serializers
from estate.models import estate
from user.serializers import RegisterSerializer
from .models import planter
from collector.models import collector
from collector.serializers import collectorSerializer
from estate.serializers import estateSerializer


class planterSerializerBasic(serializers.ModelSerializer):
    
    class Meta:
        model = planter
        fields = '__all__'
        
        
class planterSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = planter
        fields = '__all__'
        
class AddPlanterSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password' , write_only=True)
    email = serializers.CharField(source='user.email')
    usertype = serializers.CharField(source='user.usertype')
    
    class Meta:
        model = planter
        fields = ('first_name','last_name','nic','address','telephone','username','password' , 'email' , 'usertype' , 'estate' ,)
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = RegisterSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        planter_prof = planter.objects.create(user=user, **validated_data)
        return planter_prof