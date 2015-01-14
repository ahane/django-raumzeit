#from django.core.urlresolvers import reverse
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from happenings.models import Location, ThirdParty
from happenings.tests.factories import ArtistFactory, LocationFactory, ThirdPartyFactory, LocationLinkFactory, ArtistLinkFactory
from happenings.serializers import ThirdPartySerializer, LocationSerializer

def replace(dct, key, value):
	d = dct.copy()
	d[key] = value
	return d

class ArtistTests(APITestCase):
	list_url = reverse('happenings:api-artists-list')
	data = {'name': 'Artist1', 'description': 'FooBar', 'links': []}
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

class LocationTests(APITestCase):
	list_url = reverse('happenings:api-locations-list')
	data = {'name': 'Location1', 'description': 'FooBar',
			    'lat': 13.1, 'lon': 51.1, 'address': 'somestreet'}
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

class ThirdPartyTests(APITestCase):
	list_url = reverse('happenings:api-thirdparties-list')
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


class LocationLinkTests(APITestCase):
	list_url = reverse('happenings:api-locationlinks-list')

	def test_list_get_locationlink(self):
		LocationLinkFactory()
		LocationLinkFactory()
		response = self.client.get(self.list_url, format='json')
		
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(2, len(response.data))

	def test_create_locationlink(self):
		tp = ThirdPartyFactory()
		l = LocationFactory()
		data = {'third_party': tp.id, 'location': l.id, 'url': 'http://someurl.com'}
		
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
		LocationLinkFactory(location=l)
		LocationLinkFactory(location=l)
		l_url = reverse('happenings:api-location-detail', kwargs={'pk': l.id})
		response = self.client.get(l_url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		links = response.data['links']
		self.assertEqual(2, len(links))
		self.assertEqual([{'third_party': 'thirdparty1', 'url': 'http://thirdparty1.com/location1'},
						  {'third_party': 'thirdparty2', 'url': 'http://thirdparty2.com/location1'}],
						   links)


class ArtistLinkTests(APITestCase):
	list_url = reverse('happenings:api-artistlinks-list')

	def test_list_get_artistlink(self):
		ArtistLinkFactory()
		ArtistLinkFactory()
		response = self.client.get(self.list_url, format='json')
		
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(2, len(response.data))

	def test_create_lartistlink(self):
		tp = ThirdPartyFactory()
		a = ArtistFactory()
		data = {'third_party': tp.id, 'artist': a.id, 'url': 'http://someurl.com'}
		
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
		ArtistLinkFactory(artist=a)
		ArtistLinkFactory(artist=a)
		a_url = reverse('happenings:api-artist-detail', kwargs={'pk': a.id})
		response = self.client.get(a_url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		links = response.data['links']
		self.assertEqual(2, len(links))
		self.assertEqual([{'third_party': 'thirdparty1', 'url': 'http://thirdparty1.com/artist1'},
						  {'third_party': 'thirdparty2', 'url': 'http://thirdparty2.com/artist1'}],
						   links)
		