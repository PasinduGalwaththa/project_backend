from rest_framework.serializers import ModelSerializer
from .models import collector
from collector.models import collector
from planter.serializers import planterSerializer
from planter.models import planter


        


class collectorSerializer(ModelSerializer):
    planter=planterSerializer()
    class Meta:
        model = collector
        fields = '__all__'
        
class planterSerializer(ModelSerializer):
    class Meta:
        model = planter
        fields = '__all__'        