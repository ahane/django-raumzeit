from django.shortcuts import render
from django.http import HttpResponse, Http404
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
	template_name = 'happenings/happening_list.html'

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

class LocationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.


    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ArtistList(generics.ListCreateAPIView):
	"""
	List all artist or create a new one.
	"""
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer


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
	queryset = Happening.objects.all()
	serializer_class = HappeningSerializer


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


class ArtistLinkViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.


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