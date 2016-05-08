from __future__ import unicode_literals
from django.db import models


class Stops(models.Model):
    stop_id = models.CharField(max_length=8)
    stop_code = models.CharField(max_length=8)
    stop_desc = models.CharField(max_length=40)
    stop_name = models.CharField(max_length=40)
    latitude = models.FloatField();
    longitude = models.FloatField();

    def __unicode__(self):
        return '%s: %s %f %f' % (self.stop_code, self.stop_name, self.latitude, self.longitude)

