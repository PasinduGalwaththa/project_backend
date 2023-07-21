from rest_framework.serializers import ModelSerializer
from .models import updates
from planter.models import planter
from collector.models import collector



        


class UpdatesSerializer(ModelSerializer):
    planter = "planter.serializers.planterSerializer"
    collector="collector.serializers.collectorSerializer"
    class Meta:
        model = updates
        fields = '__all__'
        
class planterSerializer(ModelSerializer):
    class Meta:
        model = planter
        fields = '__all__'        
        
class collectorSerializer(ModelSerializer):
    class Meta:
        model = collector
        fields = '__all__'        