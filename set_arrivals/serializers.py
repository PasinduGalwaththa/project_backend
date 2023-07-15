from rest_framework.serializers import ModelSerializer
from .models import SetArrivals

class SetArrivalsSerializers(ModelSerializer):
    class Meta:
        model=SetArrivals
        fields='__all__'