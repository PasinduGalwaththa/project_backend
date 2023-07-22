from rest_framework.serializers import ModelSerializer
from estate.models import estate
from .models import planter


from estate.serializers import estateSerializer




class planterSerializerBasic(ModelSerializer):
    estate = estateSerializer()
    # collector=collectorSerializer()
    class Meta:
        model = planter
        fields = '__all__'

class estateSerializer(ModelSerializer):
    class Meta:
        model = estate
        fields = '__all__'
        
class planterSerializer(ModelSerializer):
    class Meta:
        model = planter
        fields = '__all__'
        
# class collectorSerializer(ModelSerializer):
#     class Meta:
#         model = collector
#         fields = '__all__'                