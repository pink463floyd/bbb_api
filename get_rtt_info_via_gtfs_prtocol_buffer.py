import sys
sys.path.append('/home/slarribeau/src/python/django_bbb/vp27/lib/python2.7/site-packages/google/transit')
print sys.path

from datetime import datetime as dt
from time import sleep
import gtfs_realtime_pb2 as gtfs
import requests

r = requests.get('http://gtfs.bigbluebus.com/tripupdates.bin')
f = gtfs.FeedMessage()
f.ParseFromString(r.content)
for e in f.entity:
        print "Id: " + str(e.vehicle.vehicle.id)
        print "Latitude: " + str(e.vehicle.position.latitude)
        print "Longitude: " + str(e.vehicle.position.longitude)
	etime = dt.fromtimestamp(e.vehicle.timestamp)
	etime = etime.strftime('%H:%M:%S')
	curr_time = dt.now()
	curr_time = curr_time.strftime('%H:%M:%S')
	print "Time: " + etime
	print "Script-Time: " + curr_time

