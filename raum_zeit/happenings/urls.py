from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
	#url(r'^$', views.index, name='index')
	url(r'^$', views.HappeningListView.as_view(), name='happenings_list'),
	url(r'^happenings/$', views.HappeningListView.as_view(), name='happenings_list'),
	url(r'^(?P<pk>\d+)/$', views.HappeningDetailView.as_view(), name='happening_detail'),
)