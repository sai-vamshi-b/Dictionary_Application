from django.test import SimpleTestCase
from django.urls import reverse, resolve
from dictionary.views import home_view, search_view

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home_view)

    def test_search_url_resolves(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search_view)
    
    