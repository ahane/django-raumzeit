import datetime

from django.views import generic
from django.http import Http404
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.exceptions import APIException, ParseError


from happenings.serializers import LocationSerializer, ArtistSerializer, HappeningSerializer, \
	ThirdPartySerializer, LocationLinkSerializer, ArtistLinkSerializer, HappeningLinkSerializer, PerformanceSerializer
from happenings.models import Happening, HappeningLink, Location, LocationLink, Artist, ArtistLink, ThirdParty, Performance



def make_timespan(hours=12):
	now = datetime.datetime.now()
	after = datetime.datetime(now.year, now.month, now.day, now.hour)
	before = after + datetime.timedelta(hours=hours)
	return after, before

###########################
# HTML Views
###########################

def homepage_view(request):
	return redirect('happenings:current_happenings_list')

class HappeningListView(generic.ListView):
	model = Happening
	template_name = 'happenings/baseline/happening_list.html'

	def get_queryset(self):
		return Happening.objects.with_artists().with_location()


class CurrentHappeningCardView(generic.ListView):
	model = Happening
	template_name = 'happenings/baseline/happening_list.html'
	def get_queryset(self):
		after, before =  make_timespan()
		timespan_happenings = Happening.objects.in_timespan(after=after, before=before)
		return timespan_happenings.with_artists().with_location()

class SignUpMockView(generic.TemplateView):
	template_name = 'happenings/baseline/signup_mock.html'


class HappeningDetailView(generic.DetailView):
	model = Happening
	template_name = 'happenings/baseline/happening_detail.html'

###########################
# API Exceptions
###########################
# put custom exceptions here 


###########################
# API Views
###########################

@api_view(('GET',))
def api_root(request, format=None):
	return Response({
		'locations': reverse('happenings:api-locations-list', request=request, format=format),
		'artists': { 
			'list': reverse('happenings:api-artists-list', request=request, format=format),
			'queries': {
				'no-sample': reverse('happenings:api-artistlinks-no-samples', request=request, format=format),
			}
		}
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
			if not queryset.exists():
				raise Http404
		return queryset.with_links()

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
			if not queryset.exists():
				raise Http404
		return queryset.with_links()

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
			if not queryset.exists():
				raise Http404
		return queryset.with_links()


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

	serializer_class = ThirdPartySerializer

	def get_queryset(self):
		queryset = ThirdParty.objects.all()
		url = self.request.query_params.get('url', None)
		if url:
			queryset = queryset.filter(url=url)
			if not queryset.exists():
				raise Http404
		return queryset


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
	queryset = ArtistLink.objects.all()
	serializer_class = ArtistLinkSerializer
	
class ArtistLinkNoSamplesList(generics.ListCreateAPIView):
	"""
	List all artist or create a new one.
	"""
	serializer_class = ArtistLinkSerializer
	def get_queryset(self):
		queryset = ArtistLink.objects.all()
		third_party = self.request.query_params.get('third_party', None)
		if third_party:
			queryset =  queryset.no_samples(third_party)
			if not queryset.exists():
				raise Http404
		else:
			raise ParseError
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