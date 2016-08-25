#from django.db import models

# Create your models here.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class Webcam(models.Model):
	geom = models.PointField(blank=True, null=True)
	station = models.CharField(max_length=255, blank=True, null=True)
	site = models.CharField(max_length=255, blank=True, null=True)
	img = models.CharField(max_length=255, blank=True, null=True)
	nom = models.CharField(max_length=255, blank=True, null=True)
	lat = models.FloatField(blank=True, null=True)
	lon = models.FloatField(blank=True, null=True)
	yaw = models.IntegerField(blank=True, null=True)

	def __str__(self):              # __unicode__ on Python 2
		return self.station + ': ' + self.nom

	class Meta:
		managed = False
		db_table = 'webcam'