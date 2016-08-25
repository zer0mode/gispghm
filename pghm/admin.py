from django.contrib.gis import admin

# Register your models here.
from leaflet.admin import LeafletGeoAdmin
from pghm.models import Webcam

#admin.site.register(Webcam, admin.OSMGeoAdmin)
admin.site.register(Webcam, LeafletGeoAdmin)