from django.contrib.gis import admin

# Register your models here.
from leaflet.admin import LeafletGeoAdmin
from pghm.models import Webcam
from pghm.models import Unite

#admin.site.register(Webcam, admin.OSMGeoAdmin)
admin.site.register(Webcam, LeafletGeoAdmin)
admin.site.register(Unite, LeafletGeoAdmin)

