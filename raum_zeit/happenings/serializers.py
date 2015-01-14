from rest_framework import serializers
from happenings.models import Artist, Location, ThirdParty, LocationLink, ArtistLink
entity_fields = ['id', 'name', 'description', 'links']

class LocationLinkSlimSerializer(serializers.ModelSerializer):
	third_party = serializers.SlugRelatedField(slug_field='name', read_only=True)
	class Meta:
		model = LocationLink
		fields = ['url', 'third_party']

class ArtistLinkSlimSerializer(serializers.ModelSerializer):
	third_party = serializers.SlugRelatedField(slug_field='name', read_only=True)

	class Meta:
		model = ArtistLink
		fields = ['url', 'third_party']


class LocationSerializer(serializers.ModelSerializer):
	links = LocationLinkSlimSerializer(many=True, read_only=True)
	class Meta:
		model = Location
		fields = entity_fields + ['address', 'lat', 'lon']

class ArtistSerializer(serializers.ModelSerializer):
	links = ArtistLinkSlimSerializer(many=True, read_only=True)
	class Meta:
		model = Artist
		fields = entity_fields

class ThirdPartySerializer(serializers.ModelSerializer):
	class Meta:
		model = ThirdParty
		fields = ['id', 'name', 'url']

class ThirdPartySlimSerializer(serializers.ModelSerializer):
	class Meta:
		model = ThirdParty
		fields = ['name']


class LocationLinkSerializer(serializers.ModelSerializer):
	class Meta:
		model = LocationLink
		fields = ['id', 'url', 'third_party', 'location']

class ArtistLinkSerializer(serializers.ModelSerializer):
	class Meta:
		model = ArtistLink
		fields = ['id', 'url', 'third_party', 'artist']





