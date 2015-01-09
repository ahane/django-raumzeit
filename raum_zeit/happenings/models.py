from django.db import models
from django_extras.db.models import LatitudeField, LongitudeField
from django.core.exceptions import ValidationError

class ThirdParty(models.Model):
	""" A third party that may provide links to an entity.
		Ex: Facebook, SoundCloud, Resident Advisor
	"""
	def __str__(self):
		return self.name
	
	name = models.CharField(max_length=200)
	url = models.URLField(unique=True)

class Link(models.Model):
	""" A hyperlink relating an entity to a resource a third party
	"""
	REPR = 'REPR' 
	# link to a resource representing an entity
	# Ex.: Profil Pages, Event Pages
	SAMPLE = 'SMPL'
	# link to a resource representing an sample work of an entity
	# Ex.: SoundCloud Track link
	SEARCH = 'SRCH'
	# link to the search result of a third party for a given entity
	# Ex. Google Maps location pin

	CATEGORIES = (
		(REPR, 'Page'),
		(SAMPLE, 'Sample'),
		(SEARCH, 'Search')
		)

	class Meta:
		abstract = True

	def __str__(self):
		return self.url

	url = models.URLField(unique=True)
	identifier = models.CharField(max_length=200, blank=True, null=True, help_text='The id used at the third party')
	is_source = models.BooleanField(default=False)
	category = models.CharField(max_length=4, choices=CATEGORIES, default=REPR)
	third_party = models.ForeignKey(ThirdParty)

class LocationLink(Link):

	location = models.ForeignKey('Location', related_name='links')

class Location(models.Model):

	def __str__(self):
		return self.name

	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	lat = LatitudeField()
	lon = LongitudeField()
	description = models.CharField(max_length=200, default='')
	third_parties = models.ManyToManyField(ThirdParty, 
									through='LocationLink', through_fields=('location', 'third_party'))


class ArtistLink(Link):

	artist = models.ForeignKey('Artist', related_name='links')

class Artist(models.Model):
	
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200, default='')
	third_parties = models.ManyToManyField(ThirdParty, 
									through='ArtistLink', through_fields=('artist', 'third_party'))
	
class HappeningLink(Link):

	happening = models.ForeignKey('Happening', related_name='links')
	
class HappeningQuerySet(models.QuerySet):

	def in_timespan(self, span_begin, span_end):
		""" Query happenings that overlap with the given timespan. 
		start < span_end
		stop > span_begin """
    
		return self.filter(start__lt=span_end, stop__gt=span_begin)

	def link_get(self, url):
		""" Get a Happening through a saved third_party link. """

		return self.select_related('links').filter(links__url=url).get()

class Performance(models.Model):

	LIVE_MUSIC = 'LIVE' # Live music such as a band
	LIVE_DJING = 'LIDJ' # A DJ actually performing a live set
	DJING = 'DJ' 		# A DJ playing tracks, a 'non-live' set

	KINDS = ( #add gettext
		(LIVE_MUSIC, 'Live Music'),
		(LIVE_DJING, 'Live Set'),
		(DJING, 'Set')) 

	happening = models.ForeignKey('Happening', related_name='performances')
	artist = models.ForeignKey('Artist', related_name='performances')
	kind = models.CharField(max_length=4, choices=KINDS, default=DJING)

class Happening(models.Model):

	def __str__(self):
		return self.name

	name = models.CharField(max_length=200)
	start = models.DateTimeField()
	stop = models.DateTimeField()
	description = models.CharField(max_length=200, default='')

	location = models.ForeignKey(Location)
	artists = models.ManyToManyField(Artist, through=Performance, blank=True)
	third_parties = models.ManyToManyField(ThirdParty, 
									through='HappeningLink', through_fields=('happening', 'third_party'))
	objects = HappeningQuerySet.as_manager()

	def clean(self):
		if self.start > self.stop:
			raise ValidationError('Happening can not stop before it starts', code='date') # add gettext


	def duration(self):
		return self.stop - self.start






