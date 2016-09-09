from django.shortcuts import render
from djgeojson.views import GeoJSONLayerView
from django.http import HttpResponse, HttpResponseBadRequest
# from .models import Webcam
# from .models import Unite
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'index.html')

class MapLayer(GeoJSONLayerView):
    # Options
    precision = 4   # float
    simplify = 0.5  # generalization

# def wcamdata(request):
#     #return HttpResponse("This is hopefully the index of colorado rocks view.")
#     return render(request, 'pghm/data/webcam2.geojson')

# def cam_view(request):
#    cams_as_geojson = serialize('geojson', Webcam.objects.all())
#    return HttpResponse(cams_as_geojson, content_type='json')