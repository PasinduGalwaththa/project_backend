from .models import Customuser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['usertype'] = user.usertype
        # ...

        return token
    
    
class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customuser
        fields = ['username', 'password', 'usertype', 'email']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = Customuser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],  # Save the email field correctly
            password=validated_data['password'],
            usertype=validated_data['usertype'],
        )
        return user
    
    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customuser
        fields = ['username', 'email', 'usertype' , 'password']

