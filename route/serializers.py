# serializers.py
from rest_framework import serializers
from .models import Route ,  RouteDetails

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'
        
        
class RouteDetailsSerializer(serializers.ModelSerializer):
    
    route = serializers.CharField(source='route.routename', read_only=True)
    collector = serializers.CharField(source='collector.name', read_only=True)
    
    class Meta:
        model = RouteDetails
        fields = ['id','route','collector','starting_time','ending_time','day']
