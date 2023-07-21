from rest_framework.serializers import ModelSerializer
from .models import estate

class estateSerializer(ModelSerializer):
    class Meta:
        model = estate
        fields = '__all__'