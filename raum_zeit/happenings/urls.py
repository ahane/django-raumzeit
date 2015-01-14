from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from happenings import views

location_list = views.LocationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
location_detail = views.LocationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

locationlink_list = views.LocationLinkViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

artistlink_list = views.ArtistLinkViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


happeninglink_list = views.HappeningLinkViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

performance_list = views.PerformanceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})




urlpatterns = patterns('',
	url(r'^$', views.HappeningListView.as_view(), name='happenings_list'),
	url(r'^happenings/$', views.HappeningListView.as_view(), name='happenings_list'),
	url(r'^(?P<pk>\d+)/$', views.HappeningDetailView.as_view(), name='happening_detail'),
	
	
	url(r'^api/locations/(?P<pk>\d+)/$', location_detail, name='api-location-detail'),
	url(r'^api/locations/$', location_list, name='api-locations-list'),
	url(r'^api/locations/links/$', locationlink_list, name='api-locationlinks-list'),

	url(r'^api/artists/(?P<pk>\d+)/$', views.ArtistDetail.as_view(), name='api-artist-detail'),
	url(r'^api/artists/$', views.ArtistList.as_view(), name='api-artists-list'),
	url(r'^api/artists/links/$', artistlink_list, name='api-artistlinks-list'),

	url(r'^api/happenings/(?P<pk>\d+)/$', views.HappeningDetail.as_view(), name='api-happening-detail'),
	url(r'^api/happenings/$', views.HappeningList.as_view(), name='api-happenings-list'),
	url(r'^api/happenings/links/$', happeninglink_list, name='api-happeninglinks-list'),

	url(r'^api/thirdparties/(?P<pk>\d+)/$', views.ThirdPartyDetail.as_view(), name='api-thirdparty-detail'),
	url(r'^api/thirdparties/$', views.ThirdPartyList.as_view(), name='api-thirdparties-list'),

	#url(r'^api/performances/(?P<pk>\d+)/$', location_detail, name='api-location-detail'),
	url(r'^api/performances/$', performance_list, name='api-performances-list'),

	url(r'^api/', views.api_root) # with a $ this breaks, without is hast to be the last item!
)

urlpatterns = format_suffix_patterns(urlpatterns)