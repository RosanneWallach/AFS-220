from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.test import Client

class PageViewTestAbout(TestCase):
    c = Client()

    def test_page_status_code(self):
        resp = self.c.get('/agency/about')
        self.assertEqual(resp.status_code, 200)

class PageViewTestPlans(TestCase):
    c = Client()

    def test_page_status_code(self):
        resp = self.c.get('/agency/plans')
        self.assertEqual(resp.status_code, 200)
