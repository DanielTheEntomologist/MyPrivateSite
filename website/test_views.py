
from django.test import TestCase
from django.urls import reverse


class viewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.sluggless_urls = [
    'home',
    'aboutme'
    ]


    def test_url_responses(self):
        
        for url in self.sluggless_urls:
            response = self.client.get(reverse(url))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, f'{url}.html')