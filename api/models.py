from __future__ import unicode_literals
from django.db import models

"""
from api.models import Stops
from api.models import StopTimes

s=Stops(stop_id='66666', stop_code='99999', stop_desc='desc desc', stop_name='name name', latitude=1.1, longitude=2.2)

s.save()

Stops.objects.all()

s=Stops.objects.get(stop_id='66666')

s

from api.serializers import StopsSerializer
"""
class Stops(models.Model):
    stop_id = models.CharField(max_length=8)
    stop_code = models.CharField(max_length=16)
    stop_name = models.CharField(max_length=80)
    stop_desc = models.CharField(max_length=80)
    latitude = models.FloatField();
    longitude = models.FloatField();
    stop_zone = models.CharField(max_length=8, null=True)
    stop_url = models.CharField(max_length=8, null=True)
    stop_location_type = models.CharField(max_length=8, null=True)
    parent_station = models.CharField(max_length=8, null=True)
    timezone = models.CharField(max_length=8, null=True)
    wheelchair = models.CharField(max_length=8, null=True)

    def __unicode__(self):
        return '%s: %s %f %f' % (self.stop_code, self.stop_name, self.latitude, self.longitude)

class StopTimes(models.Model):
   trip_id = models.CharField(max_length=8)
   arrival_time = models.CharField(max_length=8)
   departure_time = models.CharField(max_length=8)
   stop_id = models.CharField(max_length=8)
   stop_sequence = models.CharField(max_length=8)
   stop_headsign = models.CharField(max_length=80, null=True)
   pickup_type = models.CharField(max_length=8, null=True)
   drop_off_type = models.CharField(max_length=8, null=True)
   shape_dist_traveled = models.CharField(max_length=8, null=True)
   timepoint = models.CharField(max_length=8, null=True)
   def __unicode__(self):
      return '%s: %s %s' % (self.trip_id, self.stop_id, self.stop_sequence)


class Routes(models.Model):
   route_id = models.CharField(max_length=8)
   agency_id = models.CharField(max_length=8)
   route_short_name = models.CharField(max_length=8)
   route_long_name = models.CharField(max_length=80)
   route_desc = models.CharField(max_length=8, null=True)
   route_type = models.CharField(max_length=8, null=True)
   route_url = models.CharField(max_length=120, null=True)
   route_color = models.CharField(max_length=8, null=True)
   route_text_color = models.CharField(max_length=8, null=True)
   def __unicode__(self):
      return '%s: %s %s' % (self.route_id, self.route_short_name, self.route_long_name)

class Trips(models.Model):
   route_id=models.CharField(max_length=8)
   service_id=models.CharField(max_length=24)
   trip_id=models.CharField(max_length=8)
   trip_headsign=models.CharField(max_length=80)
   trip_short_name=models.CharField(max_length=8, null=True)
   direction_id=models.CharField(max_length=8)
   block_id=models.CharField(max_length=8, null=True)
   shape_id=models.CharField(max_length=8)
   wheelchair_accessible=models.CharField(max_length=8)
   bikes_allowed=models.CharField(max_length=8)
