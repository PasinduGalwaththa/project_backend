from rest_framework import serializers
from .models import Teatype

class TeatypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teatype
        fields = ['id', 'teatype']
