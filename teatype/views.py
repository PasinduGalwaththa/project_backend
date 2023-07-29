from rest_framework.decorators import APIView
from .models import Teatype
from .serializers import TeatypeSerializer
from rest_framework.response import Response

class ListTeaTypes(APIView):
    def get(self, request, format=None):
        queryset = Teatype.objects.all()
        serializer = TeatypeSerializer(queryset, many=True)
        return Response(serializer.data)
