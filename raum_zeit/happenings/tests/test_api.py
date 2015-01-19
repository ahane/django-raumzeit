#from django.core.urlresolvers import reverse
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from happenings.tests.factories import *
from django.contrib.auth.models import User
import pytz

USER = User.objects.get(username='scraper')

def replace(dct, key, value):
	d = dct.copy()
	d[key] = value
	return d

class HappeningTests(APITestCase):
	list_url = reverse('happenings:api-happenings-list')
	
	data = {'name': 'Happening1', 
			
			'description': 'foobar', 'links': []}

	def setUp(self):
		self.client.force_authenticate(USER)

	def test_create_happening(self):
		""" If an happening is created with a timezone naive
			datetimes, it is assumed to be UTC.
		"""
		l = LocationFactory()
		data = self.data.copy()
		data['location'] = l.id

		start = make_dt(hour=8, tzinfo=None).isoformat()
		stop = make_dt(hour=9, tzinfo=None).isoformat()
		data['start'], data['stop'] = start, stop
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		# Z = zulu = UTC
		self.assertEqual(response.data['start'], start + 'Z')
		self.assertEqual(response.data['stop'], stop + 'Z')

	def test_create_happening_UTC(self):
		l = LocationFactory()
		data = self.data.copy()
		data['location'] = l.id

		naive_start = datetime.datetime.utcnow()
		naive_stop = naive_start + datetime.timedelta(hours=4)

		start = pytz.utc.localize(naive_start)
		stop = pytz.utc.localize(naive_stop)

		data['start'], data['stop'] = start.isoformat(), stop.isoformat()
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		zulu_start = naive_start.isoformat() + 'Z'
		stop_start = naive_stop.isoformat() + 'Z'
		self.assertEqual(response.data['start'], zulu_start)
		self.assertEqual(response.data['stop'], stop_start)


	def test_create_happening_CET(self):
		l = LocationFactory()
		data = self.data.copy()
		data['location'] = l.id


		naive_start = datetime.datetime.utcnow()
		naive_stop = naive_start + datetime.timedelta(hours=4)

		cet = pytz.timezone('CET')		
		start = cet.localize(naive_start).isoformat()
		stop = cet.localize(naive_stop).isoformat()

		data['start'], data['stop'] = start, stop
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		self.assertEqual(response.data['start'], start)
		self.assertEqual(response.data['stop'], stop)


	def test_create_happening_EST(self):
		l = LocationFactory()
		data = self.data.copy()
		data['location'] = l.id


		naive_start = datetime.datetime.utcnow()
		naive_stop = naive_start + datetime.timedelta(hours=4)

		est = pytz.timezone('EST')		
		start = est.localize(naive_start).isoformat()
		stop = est.localize(naive_stop).isoformat()

		data['start'], data['stop'] = start, stop
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		self.assertEqual(response.data['start'], start)
		self.assertEqual(response.data['stop'], stop)

	def test_list_get_happening(self):
		HappeningFactory()
		HappeningFactory()
		
		response = self.client.get(self.list_url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(2, len(response.data))

	def test_bad_create_happening(self):
		data = {'foo': 'happening1', 'description': 'FooBar'}

		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_get_happening(self):
		HappeningFactory.reset_sequence()
		h = HappeningFactory()
		url = reverse('happenings:api-happening-detail', kwargs={'pk': h.id})
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['name'], 'happening1')

	def test_link_get_happening(self):
		h = HappeningFactory()
		HappeningFactory()
		hl = HappeningLinkFactory(happening=h)
		query = {'url': hl.url}
		response = self.client.get(self.list_url, query, format='json')
		found_h = response.data[0]
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)
		self.assertEqual(found_h['name'], h.name)

	def test_bad_link_get_happening(self):
		hl = HappeningLinkFactory()
		query = {'url': 'httpL//somebull.com'}
		response = self.client.get(self.list_url, query, format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ArtistTests(APITestCase):
	list_url = reverse('happenings:api-artists-list')
	data = {'name': 'Artist1', 'description': 'FooBar', 'links': []}

	def setUp(self):
		self.client.force_authenticate(USER)

	def test_create_artist(self):
		
		
		response = self.client.post(self.list_url, self.data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		
		data = self.data.copy()
		data['id'] = response.data['id']
		self.assertEqual(response.data, data)

	def test_sparse_create_artist(self):
		
		data = self.data.copy()
		del data['description']
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		
		data['id'] = response.data['id']
		data['description'] = ''
		self.assertEqual(response.data, data)
	
	def test_bad_create_artist(self):
		data = {'foo': 'Artist1', 'description': 'FooBar'}

		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_list_get_artist(self):
		ArtistFactory()
		ArtistFactory()
		
		response = self.client.get(self.list_url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(2, len(response.data))

	def test_get_artist(self):
		ArtistFactory.reset_sequence()
		a = ArtistFactory()
		url = reverse('happenings:api-artist-detail', kwargs={'pk': a.id})
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['name'], 'artist1')

	def test_link_get_artist(self):
		a = ArtistFactory()
		ArtistFactory()
		link = ArtistLinkFactory(artist=a)
		query = {'url': link.url}
		response = self.client.get(self.list_url, query, format='json')
		found_a = response.data[0]
		self.assertEqual(len(response.data), 1)
		self.assertEqual(found_a['name'], a.name)

	def test_bad_link_get_happening(self):
		hl = ArtistLinkFactory()
		query = {'url': 'httpL//somebull.com'}
		response = self.client.get(self.list_url, query, format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class LocationTests(APITestCase):
	list_url = reverse('happenings:api-locations-list')
	data = {'name': 'Location1', 'description': 'FooBar',
			    'lat': 13.1, 'lon': 51.1, 'address': 'somestreet'}

	def setUp(self):
		self.client.force_authenticate(USER)

	def test_create_location(self):
	
		response = self.client.post(self.list_url, self.data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		
		data = self.data.copy()
		data['id'] = response.data['id']
		data['links'] = []
		self.assertEqual(response.data, data)

	def test_sparse_create_location(self):
		
		data = self.data.copy()
		del data['description']
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		
		data['id'] = response.data['id']
		data['description'] = ''
		data['links'] = []
		self.assertEqual(response.data, data)
	
	def test_bad_create_location(self):
		data = {'foo': 'Location1'}

		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_lat_lon_validation_location(self):
		data = replace(self.data, 'lat', 3000)

		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_list_get_location(self):
		LocationFactory()
		LocationFactory()
		
		response = self.client.get(self.list_url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(2, len(response.data))

	def test_get_location(self):
		LocationFactory.reset_sequence()
		l = LocationFactory()
		url = reverse('happenings:api-location-detail', kwargs={'pk': l.id})
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['name'], 'location1')

	def test_link_get_location(self):
		l = LocationFactory()
		LocationFactory()
		link = LocationLinkFactory(location=l)
		query = {'url': link.url}
		response = self.client.get(self.list_url, query, format='json')
		found_l = response.data[0]
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)
		self.assertEqual(found_l['name'], l.name)

	def test_bad_link_get_location(self):
		LocationLinkFactory()
		query = {'url': 'http://someurl.com'}
		response = self.client.get(self.list_url, query, format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
		

class ThirdPartyTests(APITestCase):
	list_url = reverse('happenings:api-thirdparties-list')

	def setUp(self):
		self.client.force_authenticate(USER)

	def test_create_thirdparty(self):
		
		data = {'name': 'TP1', 'url': 'http://someurl.com'}
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		
		data['id'] = response.data['id']
		self.assertEqual(response.data, data)

	
	def test_bad_create_thirdparty(self):
		data = {'foo': 'TP1',
			    'url': 'http://someurl.com'}

		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_url_validation_location(self):
		data = {'name': 'TP1',
			    'url': 'not a url'}

		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_url_unique_thirdparty(self):
		data = {'name': 'TP1',
			    'url': 'http://someurl.com'}

		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		data_same_name = data.copy()
		data_same_name['url'] = 'http://otherurl.com'
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

		data_same_url= data.copy()
		data_same_url['name'] = 'TP2'
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


	def test_list_get_thirdparty(self):
		ThirdPartyFactory()
		ThirdPartyFactory()
		
		response = self.client.get(self.list_url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(2, len(response.data))

	def test_get_thirdparty(self):
		ThirdPartyFactory.reset_sequence()
		ThirdPartyFactory()
		url = reverse('happenings:api-thirdparty-detail', kwargs={'pk': 1})
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['name'], 'thirdparty1')

	def test_url_get_thirdparty(self):
		tp = ThirdPartyFactory()
		ThirdPartyFactory()
		query = {'url': tp.url}
		response = self.client.get(self.list_url, query, format='json')
		found_tp = response.data[0]
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)
		self.assertEqual(found_tp['name'], tp.name)

	def test_bad_url_get_thirdparty(self):
		tp = ThirdPartyFactory()
		ThirdPartyFactory()
		query = {'url': 'http://someotherstuff.com'}
		response = self.client.get(self.list_url, query, format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
		
class PerformanceTests(APITestCase):
	list_url = reverse('happenings:api-performances-list')

	def setUp(self):
		self.client.force_authenticate(USER)

	def test_list_get_performances(self):
		PerformanceFactory()
		PerformanceFactory()
		
		response = self.client.get(self.list_url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(2, len(response.data))

	def test_create_performances(self):
		h = HappeningFactory()
		a = ArtistFactory()
		data = {'happening': h.id, 'artist': a.id, 'kind': 'DJ'}
		
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		
		data['id'] = response.data['id']
		self.assertEqual(response.data, data)


	def test_create_bad_kindperformances(self):
		h = HappeningFactory()
		a = ArtistFactory()
		data = {'happening': h.id, 'artist': a.id, 'kind': 'foo'}
		
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		

	def test_create_performances_bad_foreign_key(self):
		HappeningFactory()
		a = ArtistFactory()
		data = {'happening': 100, 'artist': a.id}
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class LocationLinkTests(APITestCase):
	list_url = reverse('happenings:api-locationlinks-list')

	def setUp(self):
		self.client.force_authenticate(USER)

	def test_list_get_locationlink(self):
		LocationLinkFactory()
		LocationLinkFactory()
		response = self.client.get(self.list_url, format='json')
		
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(2, len(response.data))


	def test_create_locationlink(self):
		tp = ThirdPartyFactory()
		l = LocationFactory()
		data = {'third_party': tp.id, 'location': l.id, 'url': 'http://someurl.com',
				'category': 'REPR', 'identifier': 'foo'}
		
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		
		data['id'] = response.data['id']
		self.assertEqual(response.data, data)

	def test_create_locationlink_bad_foreign_key(self):
		ThirdPartyFactory()
		l = LocationFactory()
		data = {'third_party': 100, 'location': l.id, 'url': 'http://someurl.com'}
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		

	def test_embed_in_location(self):
		LocationFactory.reset_sequence()
		ThirdPartyFactory.reset_sequence()
		l = LocationFactory()
		ll1 = LocationLinkFactory(location=l)
		ll2 = LocationLinkFactory(location=l)
		l_url = reverse('happenings:api-location-detail', kwargs={'pk': l.id})
		response = self.client.get(l_url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		links = response.data['links']
		self.assertEqual(2, len(links))
		self.assertEqual([{'third_party': 'thirdparty1', 'url': 'http://thirdparty1.com/location1/REPR'},
						  {'third_party': 'thirdparty2', 'url': 'http://thirdparty2.com/location1/REPR'}],
						   links)



class ArtistLinkTests(APITestCase):
	list_url = reverse('happenings:api-artistlinks-list')

	def setUp(self):
		self.client.force_authenticate(USER)

	def test_list_get_artistlink(self):
		ArtistLinkFactory()
		ArtistLinkFactory()
		response = self.client.get(self.list_url, format='json')
		
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(2, len(response.data))

	def test_create_lartistlink(self):
		tp = ThirdPartyFactory()
		a = ArtistFactory()
		data = {'third_party': tp.id, 'artist': a.id, 'url': 'http://someurl.com',
				'category': 'REPR', 'identifier': 'foo'}
		
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		
		data['id'] = response.data['id']
		self.assertEqual(response.data, data)

	def test_create_locationlink_bad_foreign_key(self):
		ThirdPartyFactory()
		a = ArtistFactory()
		data = {'third_party': 100, 'location': a.id, 'url': 'http://someurl.com'}
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		

	def test_embed_in_artist(self):
		ArtistFactory.reset_sequence()
		ThirdPartyFactory.reset_sequence()
		a = ArtistFactory()
		al1 = ArtistLinkFactory(artist=a)
		al2 = ArtistLinkFactory(artist=a)
		a_url = reverse('happenings:api-artist-detail', kwargs={'pk': a.id})
		response = self.client.get(a_url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		links = response.data['links']
		self.assertEqual(2, len(links))
		self.assertEqual([{'third_party': 'thirdparty1', 'url': al1.url},
						  {'third_party': 'thirdparty2', 'url': al2.url}],
						   links)

	def test_no_sample_lookup_repr_links(self):
		url = reverse('happenings:api-artistlinks-no-samples')
		tp = ThirdPartyFactory()
		links = make_no_sample_artist_links(tp, retrn='links')
		link_urls = {l.url for l in links}
		query = {'third_party': tp.id}
		response = self.client.get(url, query, format='json')
		found_links = {l['url'] for l in response.data}
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(found_links), 2)
		self.assertEqual(found_links, link_urls)

		response = self.client.get(url, {}, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

		


class HappeningLinksTests(APITestCase):
	list_url = reverse('happenings:api-happeninglinks-list')

	def setUp(self):
		self.client.force_authenticate(USER)

	def test_list_get_happeninglink(self):
		HappeningLinkFactory()
		HappeningLinkFactory()
		response = self.client.get(self.list_url, format='json')
		
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(2, len(response.data))

	def test_create_happeninglink(self):
		tp = ThirdPartyFactory()
		h = HappeningFactory()
		data = {'third_party': tp.id, 'happening': h.id, 'url': 'http://someurl.com',
				'category': 'REPR', 'identifier': 'foo'}
		
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		
		data['id'] = response.data['id']
		self.assertEqual(response.data, data)

	def test_create_happeninglink_bad_foreign_key(self):
		ThirdPartyFactory()
		h = HappeningFactory()
		data = {'third_party': 100, 'location': h.id, 'url': 'http://someurl.com'}
		response = self.client.post(self.list_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		

	def test_embed_in_happening(self):
		HappeningFactory.reset_sequence()
		ThirdPartyFactory.reset_sequence()
		h = HappeningFactory()
		hl1 = HappeningLinkFactory(happening=h)
		hl2 = HappeningLinkFactory(happening=h)
		h_url = reverse('happenings:api-happening-detail', kwargs={'pk': h.id})
		response = self.client.get(h_url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		links = response.data['links']
		self.assertEqual(2, len(links))
		self.assertEqual([{'third_party': 'thirdparty1', 'url': hl1.url},
						  {'third_party': 'thirdparty2', 'url': hl2.url}],
						   links)
		
