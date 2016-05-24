import sys
sys.path.append('/home/slarribeau/src/python/django_bbb/vp27/lib/python2.7/site-packages/google/transit')
from datetime import datetime as dt
from time import sleep
import gtfs_realtime_pb2 as gtfs
import requests

import psycopg2

conn = psycopg2.connect("dbname='django' user='djangouser' host='127.0.0.1' password='dbpass'")
#cur = conn.cursor()
#cur.execute("""SELECT * from api_trips""")
#rows = cur.fetchall()

#for row in rows:
#   print "   ", row[0], row[1], row[2], row[3], row[4]
#   print row


cur = conn.cursor()
update="UPDATE api_trips SET delay = 32767;"
cur.execute(update)
conn.commit();

cur = conn.cursor()
r = requests.get('http://gtfs.bigbluebus.com/tripupdates.bin')
f = gtfs.FeedMessage()
f.ParseFromString(r.content)
for e in f.entity:
     delay=str(e.trip_update.stop_time_update[0].arrival.delay)
     trip=str(e.trip_update.trip.trip_id);
     print str(e.trip_update.trip.trip_id) + ': ' + str(e.trip_update.stop_time_update[0].arrival.delay)
     update2="UPDATE api_trips SET delay = " + delay + " where id = " + trip + ";"
     print update2;
     cur.execute(update2)
     conn.commit();


#cur = conn.cursor()
#cur.execute("""SELECT * from api_trips""")
#rows = cur.fetchall()

#for row in rows:
#   print "   ", row[0], row[1], row[2], row[3], row[4]
#   print row

