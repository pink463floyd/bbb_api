import sys
sys.path.append('/home/slarribeau/src/python/django_bbb/vp27/lib/python2.7/site-packages/google/transit')
#print sys.path

from datetime import datetime as dt
from time import sleep
import gtfs_realtime_pb2 as gtfs
import requests

r = requests.get('http://gtfs.bigbluebus.com/tripupdates.bin')
f = gtfs.FeedMessage()
f.ParseFromString(r.content)
for e in f.entity:
  #print e
  #print e.trip_update
  #print e.trip_update.trip.trip_id
  #print e.trip_update.stop_time_update[0].stop_sequence
  #print e.trip_update.stop_time_update[0].arrival.delay
  print str(e.trip_update.trip.trip_id) + ': ' + str(e.trip_update.stop_time_update[0].arrival.delay)

"""
658094
[<gtfs_realtime_pb2.StopTimeUpdate object at 0x25be8c0>]
"""


"""
id: "3876"
trip_update {
  trip {
    trip_id: "658070"
  }
  stop_time_update {
    stop_sequence: 1
    arrival {
      delay: 0
    }
  }
  vehicle {
    id: "3876"
  }
  timestamp: 1463942630
}
"""
