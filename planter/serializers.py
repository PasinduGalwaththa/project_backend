from rest_framework.serializers import ModelSerializer
from estate.models import estate
from .models import planter
from collector.models import collector
from collector.serializers import collectorSerializer

from estate.serializers import estateSerializer




class planterSerializerBasic(ModelSerializer):
    
    
    class Meta:
        model = planter
        fields = '__all__'


        
class planterSerializer(ModelSerializer):
 
   
    class Meta:
        model = planter
        fields = '__all__'
        
                