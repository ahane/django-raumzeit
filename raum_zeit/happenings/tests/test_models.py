import datetime
import pytz
from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from happenings.models import Happening, Location, Artist, ThirdParty, HappeningLink
from happenings.util import UTC

from happenings.tests.factories import *

	

class HappeningMethodsTest(TestCase):

	def test_start_stop_validation(self):
		""" Validate that start is before stop"""
		with self.assertRaises(ValidationError):
			h = HappeningFactory(start=make_dt(hour=10), stop=make_dt(hour=9))
			h.full_clean()

	def test_duration(self):
		h = HappeningFactory()
		self.assertEqual(h.duration(), datetime.timedelta(hours=4))

	def test_creation_with_links(self):
		ThirdPartyFactory.reset_sequence()
		HappeningFactory.reset_sequence()
		
		h = HappeningWithLinksFactory()
		
		links = h.links.all()
		(self.assertIsInstance(link, HappeningLink) for link in links)
		link_urls = {link.url for link in links}
		self.assertEqual(link_urls, {'http://thirdparty1.com/happening1', 'http://thirdparty2.com/happening1'})

		tps = h.third_parties.all()
		(self.assertIsInstance(link, HappeningLink) for tp in tps)
		tp_names = {tp.name for tp in tps}
		self.assertEquals(tp_names, {'thirdparty1', 'thirdparty2'})

	def test_ordering(self):
		HappeningFactory.reset_sequence()
		HappeningFactory(start=make_dt(hour=11), stop=make_dt(hour=12))
		HappeningFactory(start=make_dt(hour=9), stop=make_dt(hour=10))
		HappeningFactory(start=make_dt(hour=13), stop=make_dt(hour=14))
		HappeningFactory(start=make_dt(hour=9), stop=make_dt(hour=9, minute=30))

		creation_numbers = [int(h.name[-1]) for h in Happening.objects.all()]
		self.assertEquals(creation_numbers, [4, 2, 1, 3])


class HappeningQueryTest(TestCase):

	def make_happenings(self):
		# 10:00h, 12:00h, 14:00h, 16:00h
		starts = [make_dt(hour=h) for h in range(10, 18, 2)]
		# Standard duration of 4 hours
		for start in starts:
			HappeningFactory(start=start)


	def test_query_timespan(self):
		self.make_happenings()
		 
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

	def test_with_artists(self):
		HappeningFactory()
		PerformanceFactory()

		happenings = Happening.objects.with_artists()
		self.assertEqual(len(happenings), 2)


	def test_with_location(self):
		HappeningFactory()
		PerformanceFactory()

		happenings = Happening.objects.with_location()
		self.assertEqual(len(happenings), 2)

	def test_with_links(self):
		HappeningFactory()
		PerformanceFactory()

		happenings = Happening.objects.with_links()
		self.assertEqual(len(happenings), 2)

	def test_query_timespan_chainability(self):
		self.make_happenings()
		all_count = Happening.objects.in_timespan(make_dt(hour=10), make_dt(hour=20)).count()
		self.assertEqual(all_count, 4)

	def test_query_url(self):
		ThirdPartyFactory.reset_sequence()
		HappeningFactory.reset_sequence()
		HappeningWithLinksFactory()
		HappeningWithLinksFactory()

		happenings = Happening.objects.has_link('http://thirdparty1.com/happening1')
		h = happenings[0]
		self.assertIsInstance(h, Happening)
		self.assertEqual(h.name, 'happening1')

	def make_timespans(self):
		now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
		delta = datetime.timedelta
		present_begin = now + delta(hours=-2)
		present_end = now + delta(hours=2)
		present = HappeningFactory(start=present_begin, stop=present_end)

		past_begin = make_dt(hour=0)
		past_end = make_dt(hour=2)
		past = HappeningFactory(start=past_begin, stop=past_end)

		future_begin = now + delta(hours=2)
		future_end = now + delta(hours=4)
		future = HappeningFactory(start=future_begin, stop=future_end)

		return past, present, future

	def test_is_past(self):
		past, present, future = self.make_timespans()
		self.assertTrue(past.is_past())
		self.assertFalse(present.is_past())
		self.assertFalse(future.is_past())

	def test_is_active(self):
		past, present, future = self.make_timespans()
		self.assertFalse(past.is_active())
		self.assertTrue(present.is_active())
		self.assertFalse(future.is_active())

	def test_is_future(self):
		past, present, future = self.make_timespans()
		self.assertFalse(past.is_future())
		self.assertFalse(present.is_future())
		self.assertTrue(future.is_future())

class ArtistMethodsTest(TestCase):

	def test_filter_links(self):
		tp1 = ThirdPartyFactory()
		tp2 = ThirdPartyFactory()
		a = ArtistFactory()
		l1 = ArtistLinkFactory(artist=a, third_party=tp1, category='REPR')
		l2 = ArtistLinkFactory(artist=a,third_party=tp2, category='REPR')
		s1 = ArtistLinkFactory(artist=a,third_party=tp1, category='SMPL')
		s2 = ArtistLinkFactory(artist=a, third_party=tp2, category='SMPL')

		links_smpl = set(a.links_with(category='SMPL'))
		self.assertEquals({s1, s2}, links_smpl)

		links_repr = set(a.links_with(category='REPR'))
		self.assertEquals({l1, l2}, links_repr)

		links_smpl_tp1 = set(a.links_with(category='SMPL', third_party_name=tp1.name))
		self.assertEquals({s1}, links_smpl_tp1)



class ArtistQueryTest(TestCase):

	def test_with_links(self):
		ArtistFactory()
		ArtistLinkFactory()

		artists = Artist.objects.with_links()
		self.assertEqual(len(artists), 2)

	def test_query_url(self):
		ThirdPartyFactory.reset_sequence()
		a = ArtistFactory()
		ArtistFactory()
		link = ArtistLinkFactory(artist=a)
		ArtistLinkFactory()

		artists = Artist.objects.has_link(link.url)
		found_a = artists[0]
		self.assertIsInstance(found_a, Artist)
		self.assertEqual(a, found_a)	

	def test_query_no_samples(self):
		""" Finds all links of given third party that have
			have kind REPR but no SMPL links for same artist.
			Ex. Find all SoundCloud pages that haven't had tracks scraped from.
		"""
		tp = ThirdPartyFactory()
		a1, a2 = make_no_sample_artist_links(tp)

		artists_missing_samples = set(Artist.objects.no_samples(third_party=tp))
		self.assertEquals(len(artists_missing_samples), 2)

		self.assertEquals({a1, a2}, artists_missing_samples)

class ArtistLinkQueryTest(TestCase):
	def test_query_url(self):
		ThirdPartyFactory.reset_sequence()
		a = ArtistFactory()
		ArtistFactory()
		link = ArtistLinkFactory(artist=a)
		ArtistLinkFactory()

		found_links = ArtistLink.objects.has_link(link.url)
		
		found_link = found_links[0]
		self.assertIsInstance(found_link, ArtistLink)
		self.assertEqual(link, found_link)

	def test_query_no_samples(self):
		""" Finds all links of given third party that have
			have kind REPR but no SMPL links for same artist.
			Ex. Find all SoundCloud pages that haven't had tracks scraped from.
		"""
		tp = ThirdPartyFactory()
		l1, l2 = make_no_sample_artist_links(tp, retrn='links')

		artistslinks_missing_samples = set(ArtistLink.objects.no_samples(third_party=tp))
		self.assertEquals(len(artistslinks_missing_samples), 2)

		self.assertEquals({l1, l2}, artistslinks_missing_samples)


class LocationQueryTest(TestCase):

	def test_with_links(self):
		LocationFactory()
		LocationLinkFactory()

		locs = Location.objects.with_links()
		self.assertEqual(len(locs), 2)

	def test_query_url(self):
		ThirdPartyFactory.reset_sequence()
		l = LocationFactory()
		LocationFactory()
		link = LocationLinkFactory(location=l)
		LocationLinkFactory()

		locs = Location.objects.has_link(link.url)
		found_l = locs[0]
		self.assertIsInstance(found_l, Location)
		self.assertEqual(l, found_l)





