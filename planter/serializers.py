from rest_framework.serializers import ModelSerializer
from .models import planter

class planterSerializerBasic(ModelSerializer):
    class Meta:
        model = planter
        fields = ['first_name','last_name','estate_number','id']

class planterSerializer(ModelSerializer):
    class Meta:
        model = planter
        fields = '__all__'