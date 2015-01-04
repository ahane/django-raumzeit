import datetime

from django.db import models
from django.utils import timezone
from django_extras.db.models import LatitudeField, LongitudeField

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
	class Meta:
		abstract = True

	def __str__(self):
		return self.url
	url = models.URLField(unique=True)
	identifier = models.CharField(max_length=200, blank=True, null=True)
	is_source = models.BooleanField(default=False)
	third_party = models.ForeignKey(ThirdParty)



class Location(models.Model):

	def __str__(self):
		return self.name

	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	lat = LatitudeField()
	lon = LongitudeField()
	
class Artist(models.Model):
	
	name = models.CharField(max_length=200)	
	


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

class Happening(models.Model):

	def __str__(self):
		return self.name

	name = models.CharField(max_length=200)
	start = models.DateTimeField()
	stop = models.DateTimeField()

	location = models.ForeignKey(Location)
	artists = models.ManyToManyField(Artist, db_table='performance', blank=True)
	third_parties = models.ManyToManyField(ThirdParty, 
									through='HappeningLink', through_fields=('happening', 'third_party'))

	objects = HappeningQuerySet.as_manager()

	def duration(self):
		return self.stop - self.start






