from rest_framework.serializers import ModelSerializer
from .models import updates
from planter.models import planter


        


class UpdatesSerializer(ModelSerializer):
    class Meta:
        model = updates
        fields = '__all__'