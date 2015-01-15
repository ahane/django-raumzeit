import datetime

from django.views import generic

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

from happenings.serializers import LocationSerializer, ArtistSerializer, HappeningSerializer, \
	ThirdPartySerializer, LocationLinkSerializer, ArtistLinkSerializer, HappeningLinkSerializer, PerformanceSerializer
from happenings.models import Happening, HappeningLink, Location, LocationLink, Artist, ArtistLink, ThirdParty, Performance


###########################
# HTML Views
###########################

class HappeningListView(generic.ListView):
	model = Happening
	template_name = 'happenings/baseline/happening_list.html'

class CurrentHappeningListView(generic.ListView):
	model = Happening
	template_name = 'happenings/baseline/happening_list.html'
	def get_queryset(self):
		#after = self.requests.after
		#before = self.request.before
		after = datetime.datetime.now()
		before = after + datetime.timedelta(hours=12)
		return Happening.objects.in_timespan(after=after, before=before)


class HappeningDetailView(generic.DetailView):
	model = Happening
	template_name = 'happenings/happening_detail.html'

###########################
# API Views
###########################

@api_view(('GET',))
def api_root(request, format=None):
	return Response({
		'locations': reverse('happenings:api-locations-list', request=request, format=format),
		'artists': reverse('happenings:api-artists-list', request=request, format=format),
		})

class LocationList(generics.ListCreateAPIView):
	"""
	List all artist or create a new one.
	"""
	serializer_class = LocationSerializer

	def get_queryset(self):
		queryset = Location.objects.all()
		url = self.request.query_params.get('url', None)
		if url:
			queryset = queryset.has_link(url)
		return queryset

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a artist instance.
	"""
	queryset = Location.objects.all()
	serializer_class = LocationSerializer

class ArtistList(generics.ListCreateAPIView):
	"""
	List all artist or create a new one.
	"""
	serializer_class = ArtistSerializer

	def get_queryset(self):
		queryset = Artist.objects.all()
		url = self.request.query_params.get('url', None)
		if url:
			queryset = queryset.has_link(url)
		return queryset

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a artist instance.
	"""
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer

class HappeningList(generics.ListCreateAPIView):
	"""
	List all artist or create a new one.
	"""
	#queryset = Happening.objects.all()
	serializer_class = HappeningSerializer
	def get_queryset(self):
		queryset = Happening.objects.all()
		url = self.request.query_params.get('url', None)
		if url:
			queryset = queryset.has_link(url)
		return queryset


class HappeningDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a artist instance.
	"""
	queryset = Happening.objects.all()
	serializer_class = HappeningSerializer

class ThirdPartyList(generics.ListCreateAPIView):
	"""
	List all thirdparties or create a new one.
	"""
	queryset = ThirdParty.objects.all()
	serializer_class = ThirdPartySerializer


class ThirdPartyDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a thirdparty instance.
	"""
	queryset = ThirdParty.objects.all()
	serializer_class = ThirdPartySerializer

class LocationLinkViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.


    """
    queryset = LocationLink.objects.all()
    serializer_class = LocationLinkSerializer

class ArtistLinkList(generics.ListCreateAPIView):
	"""
	List all artist or create a new one.
	"""
	#queryset = Happening.objects.all()
	serializer_class = ArtistLinkSerializer
	def get_queryset(self):
		queryset = ArtistLink.objects.all()
		url = self.request.query_params.get('url', None)
		if url:
			queryset = queryset.has_link(url)
		return queryset


class ArtistLinkDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a artist instance.
	"""
	queryset = ArtistLink.objects.all()
	serializer_class = ArtistLinkSerializer

class HappeningLinkViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.


    """
    queryset = HappeningLink.objects.all()
    serializer_class = HappeningLinkSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.


    """
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer