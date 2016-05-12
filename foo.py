from django.db.models import Avg, Max, Min
from api.models import Stops, Routes, StopTimes

#{'trip_id__route_id__route_short_name': u'R3', 'trip_id__trip_headsign': u'Downtown SM Rapid', 'trip_id__route_id': 2461, 'departure_time': u'17:45:08'}
result=[]
x=StopTimes.objects.filter(stop_id='4').filter(departure_time__gte='17:18:00').filter(trip_id__service_id='20160221_10').values('trip_id__trip_headsign', 'trip_id__route_id__route_short_name', 'departure_time', 'trip_id__route_id')

min_time=x[0]['departure_time'];
prev_route_id=x[0]['trip_id__route_id__route_short_name'];
prev_route_name=x[0]['trip_id__trip_headsign'];

for y in x:
 #print y
 #print 'current:', y['departure_time'], 'min_time', min_time
 if y['departure_time'] < min_time:
   min_time = y['departure_time']

 if y['trip_id__route_id__route_short_name'] != prev_route_id:
   print('%s %s %s' % (prev_route_id, prev_route_name, min_time));
   result.append([prev_route_id, prev_route_name, min_time])
   min_time = y['departure_time']
   prev_route_id = y['trip_id__route_id__route_short_name']
   prev_route_name = y['trip_id__trip_headsign']

print('%s %s %s' % (prev_route_id, prev_route_name, min_time));
