from api.serializers import FooSerializer
from api.models import Routes
from api.models import Stops
from api.models import StopTimes

time="'17:18:00'"
stop = "'4'"

bar=Routes.objects.raw("select api_routes.id, route_short_name, api_trips.trip_headsign, MIN(departure_time) from api_stoptimes inner join api_trips on api_stoptimes.trip_id = api_trips.id inner join api_routes on api_trips.route_id=api_routes.id inner join api_stops on api_stoptimes.stop_id = api_stops.id where departure_time > " + time + " AND api_trips.service_id = '20160221_10' and api_stops.stop_id = " + stop + " GROUP BY api_routes.id, route_short_name, api_trips.trip_headsign;")

s=FooSerializer(bar,many=True)
#print s.data