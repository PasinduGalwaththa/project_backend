from rest_framework.serializers import ModelSerializer
from .models import planter

class planterSerializer(ModelSerializer):
    class Meta:
        model = planter
        fields = '__all__'