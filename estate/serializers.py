from rest_framework.serializers import ModelSerializer
from .models import estate


class estateSerializer(ModelSerializer):
    #collector=collectorSerializer()
    class Meta:
        model = estate
        fields = '__all__'
        
# class collectorSerializer(ModelSerializer):
#     class Meta:
#         model = collector
#         fields = '__all__'        