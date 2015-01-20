
from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from happenings.util import UTC
from happenings.templatetags.link import *
from happenings.tests.factories import *


class TestFilters(TestCase):

	def make_links(self):
		ThirdPartyFactory.reset_sequence()
		tp1 = ThirdPartyFactory(name='SoundCloud')
		tp2 = ThirdPartyFactory(name='Resident Advisor')
		h = HappeningFactory()
		l1 = HappeningLinkFactory(happening=h, third_party=tp1, category='REPR')
		l2 = HappeningLinkFactory(happening=h, third_party=tp2, category='REPR')
		l3 = HappeningLinkFactory(happening=h, third_party=tp1, category='SMPL')
		l4 = HappeningLinkFactory(happening=h, third_party=tp2, category='SMPL')
		return [l1, l2, l3, l4]


	def test_get_third_party_name(self):
		links = self.make_links()
		filtered = match_third_party(links, 'SoundCloud')
		tp_names = {l.third_party.name for l in filtered}
		self.assertEquals(len(filtered), 2)
		self.assertEquals(tp_names, {'SoundCloud'})

	def test_get_category(self):
		links = self.make_links()
		filtered = match_category(links, 'REPR')
		tp_names = {l.third_party.name for l in filtered}
		self.assertEquals(len(filtered), 2)
		self.assertEquals(tp_names, {'SoundCloud', 'Resident Advisor'})

	def test_get_representations(self):
		links = self.make_links()
		filtered = get_representations(links)
		tp_names = {l.third_party.name for l in filtered}
		categories = {l.category for l in filtered}
		self.assertEquals(len(filtered), 2)
		self.assertEquals(tp_names, {'SoundCloud', 'Resident Advisor'})
		self.assertEquals(categories, {'REPR'})

	def test_get_samples(self):
		links = self.make_links()
		filtered = get_samples(links)
		tp_names = {l.third_party.name for l in filtered}
		categories = {l.category for l in filtered}
		self.assertEquals(len(filtered), 2)
		self.assertEquals(tp_names, {'SoundCloud', 'Resident Advisor'})
		self.assertEquals(categories, {'SMPL'})

	def test_get_soundcloud(self):
		links = self.make_links()
		filtered = get_soundcloud(links)
		tp_names = {l.third_party.name for l in filtered}
		categories = {l.category for l in filtered}
		self.assertEquals(len(filtered), 2)
		self.assertEquals(tp_names, {'SoundCloud'})
		self.assertEquals(categories, {'SMPL', 'REPR'})

	def test_get_residenta(self):
		links = self.make_links()
		filtered = get_residenta(links)
		tp_names = {l.third_party.name for l in filtered}
		categories = {l.category for l in filtered}
		self.assertEquals(len(filtered), 2)
		self.assertEquals(tp_names, {'Resident Advisor'})
		self.assertEquals(categories, {'SMPL', 'REPR'})

	def test_googlemaps(self):
		google_query_url = compile_google_maps(" Schillerpromenade 11, 12049 Berlin")
		self.assertEquals(google_query_url, 'http://maps.google.com/maps?q=+Schillerpromenade+11%2C+12049+Berlin')