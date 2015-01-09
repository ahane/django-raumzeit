import factory
import datetime
from happenings.util import UTC
from happenings.models import Happening, HappeningLink, Artist, Location, ThirdParty

########################
# Helper Factories
########################

def make_tz():
	return UTC()

def make_dt(day=1, hour=12, tzinfo=make_tz()):
	return datetime.datetime(2015, 1, day, hour, tzinfo=tzinfo)

########################
# Entity Factories
########################

class LocationFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Location

	name = factory.Sequence(lambda n: 'location{}'.format(n))
	address = 'foobar'
	lat = 51.1
	lon = 13.1

class ThirdPartyFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = ThirdParty

	name = factory.Sequence(lambda n: 'thirdparty{}'.format(n))
	url = factory.LazyAttribute(lambda o: 'http://{}.com'.format(o.name))

class HappeningFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Happening

	name = factory.Sequence(lambda n: 'happening{}'.format(n))
	start = make_dt(hour=12)
	stop = factory.LazyAttribute(lambda o: o.start + datetime.timedelta(hours=4))
	location = factory.SubFactory(LocationFactory)

class HappeningLinkFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = HappeningLink

	third_party = factory.SubFactory(ThirdPartyFactory)
	happening = factory.SubFactory(HappeningFactory)
	url = factory.LazyAttribute(lambda o: '{0}/{1}'.format(o.third_party.url, o.happening))
	identifier = factory.LazyAttribute(lambda o: o.happening.id)

class ArtistFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Artist

	name = factory.Sequence(lambda n: 'artist{}'.format(n))
	description = 'desc'


#######################
# Aggregate Factories
########################

class HappeningWithLinksFactory(HappeningFactory):
	third_parties1 = factory.RelatedFactory(HappeningLinkFactory, 'happening')
	third_parties2 = factory.RelatedFactory(HappeningLinkFactory, 'happening')


########################
# Collections Factories
########################



def make_locations_with_happenings():
	# 10:00h, 12:00h, 14:00h, 16:00h
	starts_1 = [make_dt(hour=h) for h in range(10, 18, 2)]
	# 14:00h, 16:00h, 18:00h, 20:00h
	starts_2 = [make_dt(hour=h) for h in range(14, 22, 2)]

	l1 = LocationFactory()
	for s in starts_1:
		HappeningFactory(start=s, location=l1)

	l2 = LocationFactory()
	for s in starts_2:
		HappeningFactory(start=s, location=l2)