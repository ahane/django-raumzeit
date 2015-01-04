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

class LocationFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Location

	name = 'location'
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
	start = datetime.datetime.now(UTC())
	stop = start + datetime.timedelta(hours=4)

	location = factory.SubFactory(LocationFactory)


class HappeningLinkFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = HappeningLink

	third_party = factory.SubFactory(ThirdPartyFactory)
	happening = factory.SubFactory(HappeningFactory)
	url = factory.LazyAttribute(lambda o: '{0}/{1}'.format(o.third_party.url, o.happening))

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
