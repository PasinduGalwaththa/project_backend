from rest_framework.serializers import ModelSerializer
from planter.models import planter

from .models import collector





        


class collectorSerializer(ModelSerializer):
    #planter=planterSerializer()
    class Meta:
        model = collector
        fields = '__all__'
        
# class planterSerializer(ModelSerializer):
#     class Meta:
#         model = planter
#         fields = '__all__'        