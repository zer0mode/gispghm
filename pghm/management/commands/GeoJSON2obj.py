import os
import json
import pghm
from django.core import serializers
from djgeojson.serializers import Deserializer as GeoJSONSerializer
from django.core.management.base import BaseCommand, CommandError

#from .models import Webcam

class Command(BaseCommand):
    help = 'Shows geojson'

    #def run(verbose=True):
    def handle(self, *args, **options):

        # locating files
        # the command GeoJSON2obj is in commands folder
        # commands folder is in management - it can be located like this :
        manage_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        gjdata = os.path.join(os.path.dirname(pghm.__file__),'data/webcam2.geojson')
        print (gjdata)
        with open(gjdata, 'r') as handle:
            parsed = json.load(handle)
        print (json.dumps(parsed, indent=4))

        #show object
        # for deserialized_object in serializers.deserialize("geojson", parsed):
        #    if object_should_be_saved(deserialized_object):
        #       print (deserialized_object)
        #GeoJSONSerializer().deserialize('geojson', gjdata)