from rest_framework import serializers
from happenings.models import Artist, Location, ThirdParty, LocationLink
entity_fields = ['id', 'name', 'description']

class LocationSerializer(serializers.ModelSerializer):
	links = serializers.SlugRelatedField( 
		many=True,
        read_only=True,
        slug_field='url'
	)
	class Meta:
		model = Location
		fields = entity_fields + ['address', 'lat', 'lon', 'links']

class ArtistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artist
		fields = entity_fields

class ThirdPartySerializer(serializers.ModelSerializer):
	class Meta:
		model = ThirdParty
		fields = ['id', 'name', 'url']

class LocationLinkSerializer(serializers.ModelSerializer):
	# third_party = serializers.PrimaryKeyRelatedField(queryset=ThirdParty.objects.all())
	# location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
	class Meta:
		model = LocationLink
		fields = ['id', 'url', 'third_party', 'location']



