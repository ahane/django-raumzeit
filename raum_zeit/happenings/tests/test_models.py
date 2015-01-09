import datetime
from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
#import factory
from happenings.models import Happening, Location, ThirdParty, HappeningLink
from happenings.util import UTC

from happenings.tests.factories import *

class HappeningMethodsTest(TestCase):

	def test_start_stop_validation(self):
		""" Validate that start is before stop"""
		with self.assertRaises(ValidationError):
			h = HappeningFactory(start=make_dt(10), stop=make_dt(9))
			h.full_clean()


	def test_duration(self):
		h = HappeningFactory()
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





