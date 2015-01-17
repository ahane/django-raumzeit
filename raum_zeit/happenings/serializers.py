from rest_framework import serializers
from happenings.models import Artist, Location, Happening, ThirdParty, LocationLink, ArtistLink, HappeningLink, Performance
entity_fields = ['id', 'name', 'description', 'links']
link_fields = ['id', 'url', 'third_party', 'category', 'identifier']

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

class HappeningLinkSlimSerializer(serializers.ModelSerializer):
	third_party = serializers.SlugRelatedField(slug_field='name', read_only=True)

	class Meta:
		model = HappeningLink
		fields = ['url', 'third_party']


class LocationLinkSerializer(serializers.ModelSerializer):
	class Meta:
		model = LocationLink
		fields = link_fields + ['location']

class ArtistLinkSerializer(serializers.ModelSerializer):
	class Meta:
		model = ArtistLink
		fields = link_fields + ['artist']

class HappeningLinkSerializer(serializers.ModelSerializer):
	class Meta:
		model = HappeningLink
		fields = link_fields + ['happening']

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

class HappeningSerializer(serializers.ModelSerializer):
	links = HappeningLinkSlimSerializer(many=True, read_only=True)
	class Meta:
		model = Happening
		fields = entity_fields + ['start', 'stop', 'location']


class ThirdPartySerializer(serializers.ModelSerializer):
	class Meta:
		model = ThirdParty
		fields = ['id', 'name', 'url']

class PerformanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Performance
		fields = ['id', 'artist', 'happening', 'kind']



