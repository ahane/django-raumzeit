from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from happenings.models import Artist

class ArtistResource(ModelResource):

	class Meta:
		queryset = Artist.objects.all()
		resource_name = 'artist'
		authorization= Authorization()