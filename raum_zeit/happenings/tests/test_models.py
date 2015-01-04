import datetime
from django.test import TestCase
from django.utils import timezone

import factory
from happenings.models import Happening, Location, ThirdParty, HappeningLink


class UTC(datetime.tzinfo):
	    """UTC"""

	    def utcoffset(self, dt):
	        return datetime.timedelta(0)

	    def tzname(self, dt):
	        return "UTC"

	    def dst(self, dt):
	        return datetime.timedelta(0)

def make_dt(day=1, hour=12, tzinfo=UTC()):

	return datetime.datetime(2015, 1, day, hour, tzinfo=UTC())

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

def make_happenings():
	# 10:00h, 12:00h, 14:00h, 16:00h
	starts = [make_dt(hour=h) for h in range(10, 18, 2)]
	# Standard duration of 4 hours
	for start in starts:
		HappeningFactory(start=start)

class HappeningLinkFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = HappeningLink

	third_party = factory.SubFactory(ThirdPartyFactory)
	happening = factory.SubFactory(HappeningFactory)
	url = factory.LazyAttribute(lambda o: '{0}/{1}'.format(o.third_party.url, o.happening))
	identifier = factory.LazyAttribute(lambda o: o.happening.id)

class HappeningWithLinkFactory(HappeningFactory):
	third_parties = factory.RelatedFactory(HappeningLinkFactory, 'happening')

class HappeningWithLinksFactory(HappeningFactory):
	third_parties1 = factory.RelatedFactory(HappeningLinkFactory, 'happening')
	third_parties2 = factory.RelatedFactory(HappeningLinkFactory, 'happening')


class HappeningMethodsTest(TestCase):
	def test_duration(self):
		now = timezone.now()
		stop = now + datetime.timedelta(hours=4)
		h = HappeningFactory(start=now, stop=stop)
		self.assertEqual(h.duration(), datetime.timedelta(hours=4))

	def test_creation_with_link(self):

		h = HappeningWithLinkFactory()
		tps = h.third_parties.all()
		third_party_name = tps[0].name
		self.assertEqual(third_party_name, 'thirdparty1')

	def test_creation_with_third_parties(self):
		ThirdPartyFactory.reset_sequence()
		h = HappeningWithLinksFactory()
		tps = h.third_parties.all()
		tp_names = {tp.name for tp in tps}
		self.assertEquals(tp_names, {'thirdparty1', 'thirdparty2'})

	def test_creation_with_links(self):
		ThirdPartyFactory.reset_sequence()
		HappeningFactory.reset_sequence()
		
		h = HappeningWithLinksFactory()
		
		links = h.links.all()

		for link in links:
			self.assertIsInstance(link, HappeningLink)

		urls = {link.url for link in links}
		self.assertEqual(urls, {'http://thirdparty1.com/happening1', 'http://thirdparty2.com/happening1'})

class HappeningQueryTest(TestCase):


	def test_query_timespan(self):
		make_happenings()
		 
		first_query = Happening.objects.in_timespan(make_dt(hour=8), make_dt(hour=11))
		self.assertEqual(len(first_query), 1)
		first_happ = first_query[0]
		self.assertEqual(first_happ.start, make_dt(hour=10))
		self.assertEqual(first_happ.stop, make_dt(hour=14))
		

		all_query = Happening.objects.in_timespan(make_dt(hour=10), make_dt(hour=20))
		self.assertEqual(len(all_query), 4)

		last_query = Happening.objects.in_timespan(make_dt(hour=19), make_dt(hour=21))
		self.assertEqual(len(last_query), 1)
		last_happ = last_query[0]
		self.assertEqual(last_happ.start, make_dt(hour=16))
		self.assertEqual(last_happ.stop, make_dt(hour=20))

	def test_query_timespan_chainability(self):
		make_happenings()
		all_count = Happening.objects.in_timespan(make_dt(hour=10), make_dt(hour=20)).count()
		self.assertEqual(all_count, 4)


	def test_query_url(self):
		ThirdPartyFactory.reset_sequence()
		HappeningFactory.reset_sequence()
		HappeningWithLinksFactory()
		HappeningWithLinksFactory()

		h = Happening.objects.link_get('http://thirdparty1.com/happening1')
		self.assertEqual(h.name, 'happening1')



