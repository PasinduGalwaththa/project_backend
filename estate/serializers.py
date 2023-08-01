from rest_framework import serializers
from .models import estate
from teatype.serializers import TeaIdOnlyserializer


class estateSerializer(serializers.ModelSerializer):
    class Meta:
        model = estate
        fields = '__all__'
        
# class collectorSerializer(ModelSerializer):
#     class Meta:
#         model = collector
#         fields = '__all__' 

class addEstateSerializer(serializers.ModelSerializer):
    
    teatype =  serializers.CharField(source='teatype.teatype')
    
    class Meta:
        model = estate
        fields = ['estatename', 'teatype']
        
    def create(self, validated_data):
        teatype_data = validated_data.pop('teatype')
        teatype_serializer = TeaIdOnlyserializer(data=teatype_data)
        teatype_serializer.is_valid(raise_exception=True)
        teatype = teatype_serializer.save()
        estate_prof = estate.objects.create(teatype=teatype, **validated_data)
        return estate_prof
    

class EstateIdOnlyserializer(serializers.ModelSerializer):
    class Meta:
        model = estate
        fields = ['id' , 'estatename']