from api.models import Routes
x=Routes.objects.all()
from api.serializers import RoutesSerializer
s=RoutesSerializer(x[0], many=False)
print s.data
