from rest_framework import serializers
from .models import updates
from planter.models import planter
from collector.models import collector



        


class UpdatesSerializer(serializers.ModelSerializer):
    planter = "planter.serializers.planterSerializer"
    collector="collector.serializers.collectorSerializer"
    class Meta:
        model = updates
        fields = '__all__'
        
class planterSerializer(serializers.ModelSerializer):
    class Meta:
        model = planter
        fields = '__all__'        
        
class collectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = collector
        fields = '__all__' 
        
class GetupdatesbyPlantIDdSerializer(serializers.ModelSerializer):
    
    planter = serializers.CharField(source='planter.first_name', read_only=True)
    collector = serializers.CharField(source='collector.first_name', read_only=True)
    estate = serializers.CharField(source='estate.name', read_only=True)
    
    class Meta:
        model = updates
        fields = ['id','planter','collector','collected_date' , 'weight' , 'estate']     
        
        