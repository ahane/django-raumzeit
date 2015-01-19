import sys
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class TestRunning(StaticLiveServerTestCase):
	
	@classmethod
	def setUpClass(cls):
		for arg in sys.argv:
			if 'liveserver' in arg:
				cls.server_url = 'http://' + arg.split('=')[1]
				return
		super().setUpClass()
		cls.server_url = cls.live_server_url

	@classmethod
	def tearDownClass(cls):
		if cls.server_url == cls.live_server_url:
			super().tearDownClass()

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
		

	def test_title(self):

		self.browser.get(self.server_url)
		self.assertIn('dasgeht', self.browser.title)