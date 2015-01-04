import datetime

from django.db import models
from django.utils import timezone

class ThirdParty(models.Model):

	def __str__(self):
		return self.name
	
	name = models.CharField(max_length=200)
	url = models.URLField()
	is_source = models.BooleanField(default=False)


class Location(models.Model):

	name = models.CharField(max_length=200)

	address = models.CharField(max_length=200)
	lat = models.FloatField()
	lon = models.FloatField()
	

class Artist(models.Model):
	
	name = models.CharField(max_length=200)	
	

class Link(models.Model):
	class Meta:
		abstract = True
	url = models.URLField()
	third_party = models.ForeignKey(ThirdParty)


class HappeningLink(Link):

	happening = models.ForeignKey('Happening', related_name='links')
	

class Happening(models.Model):

	def __str__(self):
		return self.name

	name = models.CharField(max_length=200)
	start = models.DateTimeField()
	stop = models.DateTimeField()

	location = models.ForeignKey(Location)
	artists = models.ManyToManyField(Artist, db_table='performance')
	third_parties = models.ManyToManyField(ThirdParty, 
									through='HappeningLink', through_fields=('happening', 'third_party'))


	def duration(self):
		return self.stop - self.start






