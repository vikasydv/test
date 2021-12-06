from django.test import TestCase
from ch4.models import Page
from django.urls import reverse
# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        Page.objects.create(text='just a game')
    def test_of_model(self):
        page = Page.objects.get(id=1)
        expected_outcome = f'{page.text}'
        self.assertEqual(expected_outcome,'just a game')
class HomepageTest(TestCase):
    def setUp(self):
        Page.objects.create(text='another test')
    def test_url_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)
    def test_url_byName(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
    def test_url_html(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'ch4/home_list.html')