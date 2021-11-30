from django.test import TestCase, Client
import requests

# Create your tests here.
class HomepageTest(TestCase):
    def url_test(self):
        c = Client()
        resp = c.get('/')
        self.assertEqual(200, resp.status_code)
        self.longMessage("get url tested working fine")