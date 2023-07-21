from rest_framework.serializers import ModelSerializer
from .models import vehicles
from collector.models import collector
from collector.serializers import collectorSerializer

class vehilcesSerializer(ModelSerializer):
    collector = collectorSerializer()
    class Meta:
        model = vehicles
        fields = '__all__'
        
class collectorSerializer(ModelSerializer):
    class Meta:
        model = collector
        fields = '__all__'        