from django.contrib.gis import admin

# Register your models here.
from django.conf import settings
from leaflet.admin import LeafletGeoAdmin
from pghm.models import Webcam
#from pghm.models import Unite

class MapLeafletGeoAdmin(LeafletGeoAdmin):
# straight hint @https://github.com/makinacorpus/django-leaflet/pull/28#issuecomment-23943492
    settings_overrides = {
    	'TILES': [
			('IGN Maps', settings.SCAN_IGN, settings.IGN_ATTRIB),
			('IGN Ortho', settings.ORTHO_IGN, settings.IGN_ATTRIB),
			('OSM', settings.BASE_OSM, settings.OSM_ATTRIB),
		],    
		#'MINIMAP': True,
	}    

#admin.site.register(Unite, LeafletGeoAdmin)
admin.site.register(Webcam, MapLeafletGeoAdmin)
#admin.site.register(Webcam, admin.OSMGeoAdmin)