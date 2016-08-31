"""djmapping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from pghm import views
from pghm.models import Webcam
from pghm.models import Unite
from pghm.views import MapLayer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
#rom django.views.generic import TemplateView
#from djgeojson.views import GeoJSONLayerView
#from pghm.views import cam_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^camera.geojson$', MapLayer.as_view(model=Webcam, properties=('nom','img','site',)), name='camera'),
    #url(r'^webcams/', TemplateView.as_view(template_name='pghm/wcams.html'), name='wcams'),
    #url(r'^webcams.geojson/', GeoJSONLayerView.as_view(model=Webcam), name='wcamsdata'),
    #url(r'^webcamdata$', views.wcamdata, name='webcams'),
    #url(r'^cams.data/', cam_view, name='camser'),
    #url(r'^ski.data/', ski_view, name='skiser'),
    #url(r'^zone.data/', zone_view, name='zoneser'),
    #url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    #url(r'^accounts/login/$', auth_views.login),
    url('^', include('django.contrib.auth.urls')),
    #url(r'^accounts/profile/$', auth_views.login),
]

