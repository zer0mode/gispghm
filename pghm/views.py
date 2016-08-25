from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Webcam
from django.core.serializers import serialize

@login_required(login_url='/login/')
# login_required decorator requires authentification for all views
# looks for login.html located in 'appname/templates/registration'
def home(request):
    #return HttpResponse("This will be the index.")
    return render(request, 'pghm/index.html')

def cam_view(request):
    cams_as_geojson = serialize('geojson', Webcam.objects.all())
    return HttpResponse(cams_as_geojson, content_type='json')

def logout_view(request):
    logout(request)
    # Redirect to a success page.