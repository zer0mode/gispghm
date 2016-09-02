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
from django.conf.urls import url, include
from django.contrib.gis import admin
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from pghm.models import Webcam
from pghm import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^webcams/', TemplateView.as_view(template_name='pghm/wcams.html'), name='webcams'),
    
    url(r'^webcams.geojson/', GeoJSONLayerView.as_view(model=Webcam, properties=()), name='wcamsdata'),
    # map geojson file

    url(r'^cams.data/', views.cam_view, name='camser'),

    # http://stackoverflow.com/questions/2867213/is-there-a-built-in-login-template-in-django
    url('^', include('django.contrib.auth.urls')),
    url(r'^logout/', views.logout_view, name='logout'),
    #url(r'^accounts/login/$', auth_views.login),
    
    # custom login with custom location
    #url('^login/', auth_views.login, {'template_name': 'pghm/login2.html'}, name='user_login'),
]