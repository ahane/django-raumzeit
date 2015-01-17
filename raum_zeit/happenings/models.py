import datetime
import pytz
from django.db import models
from django_extras.db.models import LatitudeField, LongitudeField
from django.core.exceptions import ValidationError
from happenings.util import now_utc

class LinksQueryMixin(object):
	""" Functionality for querysets of models that have a 'links' attribute """

	def has_link(self, url):
		""" Get an entity through a saved third_party link. """

		return self.select_related('links').filter(links__url=url).all()

	def with_links(self):
		return self.prefetch_related('links').prefetch_related('links__third_party')

#class ThirdPartyQuerySet(models.QuerySet, LinksQueryMixin):
class ThirdPartyQuerySet(models.QuerySet):
	pass

class ThirdParty(models.Model):
	""" A third party that may provide links to an entity.
		Ex: Facebook, SoundCloud, Resident Advisor
	"""
	def __str__(self):
		return self.name
	
	name = models.CharField(max_length=200, unique=True)
	url = models.URLField(unique=True)
	objects = ThirdPartyQuerySet.as_manager()

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

class LocationQuerySet(models.QuerySet, LinksQueryMixin):
	pass

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

	objects = LocationQuerySet.as_manager()

class ArtistLinkQuerySet(models.QuerySet):
	def has_link(self, url):
		return self.filter(url=url)

	def no_samples(self, third_party):
		""" Finds all links of given third party that have REPR but no SMPL links for same artist.
			
			Ex. Find all SoundCloud pages that haven't had tracks scraped from.
		"""

		repr_links = self.filter(third_party=third_party, category='REPR')
		no_smpl = repr_links.exclude(artist__links__third_party=third_party,
									 artist__links__category='SMPL')
		return no_smpl


class ArtistLink(Link):

	artist = models.ForeignKey('Artist', related_name='links')
	objects = ArtistLinkQuerySet.as_manager()

class ArtistQuerySet(models.QuerySet, LinksQueryMixin):
	
	def no_samples(self, third_party):
		""" Finds all links of given third party that have REPR but no SMPL links for same artist.
			
			Ex. Find all SoundCloud pages that haven't had tracks scraped from.
		"""
		with_repr = self.filter(links__third_party=third_party, links__category='REPR')
		without_smpl = with_repr.exclude(links__category='SMPL')
		return without_smpl


class Artist(models.Model):
	
	def __str__(self):
		return self.name

	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200, default='')
	third_parties = models.ManyToManyField(ThirdParty, 
									through='ArtistLink', through_fields=('artist', 'third_party'))

	objects = ArtistQuerySet.as_manager()
	
class HappeningLink(Link):

	happening = models.ForeignKey('Happening', related_name='links')
	

class HappeningQuerySet(models.QuerySet, LinksQueryMixin):

	def in_timespan(self, after, before):
		""" Query happenings that overlap with the given timespan. 
		start < span_end = before
		stop > span_begin = after"""
    
		filtered = self.filter(start__lt=before, stop__gt=after)
		return filtered

	def with_artists(self):
		return self.prefetch_related('artists')

	def with_location(self):
		return self.prefetch_related('location')


class Performance(models.Model):

	class Meta:
		unique_together = ('happening', 'artist')

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

	class Meta:
		ordering = ('start', 'stop')

	def __str__(self):
		return self.name

	name = models.CharField(max_length=200)
	start = models.DateTimeField()
	stop = models.DateTimeField()
	description = models.CharField(max_length=200, default='')

	location = models.ForeignKey(Location)
	artists = models.ManyToManyField(Artist, through=Performance)
	third_parties = models.ManyToManyField(ThirdParty, 
									through='HappeningLink', through_fields=('happening', 'third_party'))
	
	objects = HappeningQuerySet.as_manager()

	def is_active(self):
		return self.start <= now_utc() < self.stop

	def is_past(self):
		return self.stop <= now_utc()

	def is_future(self):
		return now_utc() < self.start

	def clean(self):
		if self.start > self.stop:
			raise ValidationError('Happening can not stop before it starts', code='date') # add gettext

	def duration(self):
		return self.stop - self.start






