from rest_framework import serializers
from estate.models import estate
from user.serializers import RegisterSerializer
from .models import planter
from estate.serializers import addEstateSerializer
from teatype.models import Teatype 
from user.models import Customuser

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
    password = serializers.CharField(source='user.password', write_only=True)
    email = serializers.CharField(source='user.email')
    usertype = serializers.CharField(source='user.usertype')
    estate = serializers.CharField(read_only=True )
    teatype = serializers.CharField(read_only=True)
    

    class Meta:
        model = planter
        fields = (
            'first_name', 'last_name', 'nic', 'address', 'telephone', 'username',
            'password', 'email', 'usertype', 'estate', 'teatype'
        )
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user_data = validated_data.pop('user')
            user_serializer = RegisterSerializer(data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()

            estatename = validated_data.pop('estate')
            teatype_name = validated_data.pop('teatype')

            # Get or create the Estate object based on the estatename
            estate_obj, _ = estate.objects.get_or_create(estatename=estatename)

            # Get or create the Teatype object based on the teatype_name
            teatype_obj, _ = Teatype.objects.get_or_create(teatype=teatype_name)

            planter_prof = planter.objects.create(user=user, estate=estate_obj, teatype=teatype_obj, **validated_data)
            return planter_prof
        
        

class PlannterIDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = planter
        fields = ['id']
        

class AddPlanterSerializer(serializers.ModelSerializer):
    estate = addEstateSerializer()
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password', write_only=True)
    email = serializers.CharField(source='user.email')
    usertype = serializers.CharField(source='user.usertype')
    
    class Meta:
        model = planter
        fields = [
            'first_name', 'last_name', 'nic', 'address', 'telephone', 'username',
            'password', 'email', 'usertype', 'estate'
        ]

    def create(self, validated_data):
        # Extract data for the nested estate serializer
        estate_data = validated_data.pop('estate', None)
        
        # Create the planter instance without the nested estate field
        user_data = validated_data.pop('user')
        user = Customuser.objects.create(**user_data)
        planter_instance = planter.objects.create(user=user, **validated_data)
        
        # Handle the nested estate creation
        if estate_data:
            estate_serializer = addEstateSerializer(data=estate_data)
            estate_serializer.is_valid(raise_exception=True)
            estate_serializer.save()
        
        return planter_instance
    
    
class PlanterSerializerAdd(serializers.ModelSerializer):
    
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    password = serializers.CharField(source='user.password', write_only=True)
    usertype = serializers.CharField(source='user.usertype')
    
    class Meta:
        model = planter
        fields = ['id','first_name','last_name','nic','address','telephone','estate', 'username', 'email', 'password', 'usertype']
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = RegisterSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        planter_profile = planter.objects.create(user=user, **validated_data)
        return planter_profile
        