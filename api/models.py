from __future__ import unicode_literals
from django.db import models

"""
from api.models import Stops

s=Stops(stop_id='66666', stop_code='99999', stop_desc='desc desc', stop_name='name name', latitude=1.1, longitude=2.2)

s.save()

Stops.objects.all()

s=Stops.objects.get(stop_id='66666')

s

from api.serializers import StopsSerializer
"""



class Stops(models.Model):
    stop_id = models.CharField(max_length=8)
    stop_code = models.CharField(max_length=8)
    stop_desc = models.CharField(max_length=40)
    stop_name = models.CharField(max_length=40)
    latitude = models.FloatField();
    longitude = models.FloatField();

    def __unicode__(self):
        return '%s: %s %f %f' % (self.stop_code, self.stop_name, self.latitude, self.longitude)

