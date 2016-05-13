from api.models import Stops
x=Stops.objects.all()
from api.serializers import StopsSerializer
s=StopsSerializer(x, many=True)
print s.data
