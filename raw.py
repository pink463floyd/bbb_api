from api.serializers import StopsSerializer
from api.models import Stops

bar=Stops.objects.raw('select id, stop_id from api_stops;')
s=StopsSerializer(bar,many=True)
print s.data
