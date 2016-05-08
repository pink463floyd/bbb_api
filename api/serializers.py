from rest_framework import serializers
from api.models import Stops


"""
from api.models import Stops
from api.serializers import StopsSerializer
s=Stops.objects.get(stop_id='66666')
serializer=StopsSerializer(s)
serializer.data
"""

class StopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stops
        fields = ('stop_id', 'stop_code', 'stop_desc', 'stop_name', 'latitude')



