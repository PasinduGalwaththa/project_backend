from rest_framework.serializers import ModelSerializer
from .models import updates
from planter.models import planter



        


class UpdatesSerializer(ModelSerializer):
    planter = "planter.serializers.planterSerializer"
    class Meta:
        model = updates
        fields = '__all__'
        
class planterSerializer(ModelSerializer):
    class Meta:
        model = planter
        fields = '__all__'        