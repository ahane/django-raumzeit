from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'raum_zeit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^rz/', include('happenings.urls', namespace='happenings')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

)
