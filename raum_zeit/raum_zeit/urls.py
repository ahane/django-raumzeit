from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from happenings.api import ArtistResource

v1_api  = Api(api_name='v1')
v1_api.register(ArtistResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'raum_zeit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^rz/', include('happenings.urls', namespace='happenings')),
   	url(r'^api/', include(v1_api.urls)), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

)
