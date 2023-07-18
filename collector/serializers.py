from rest_framework.serializers import ModelSerializer
from .models import collector
from collector.models import collector


        


class collectorSerializer(ModelSerializer):
    class Meta:
        model = collector
        fields = '__all__'