from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    # Check that resolve, when called with '/', find a function called home_page
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # create an HttpRequest object, which is what Django will see when a user’s browser asks for a page
        request = HttpRequest()
        # We pass it to our home_page view, which gives us a response
        response = home_page(request)
        # we extract the .content of the response and convert it to utf8
        html = response.content.decode('utf8')
        # We want it to start with an <html> tag which gets closed at the end
        self.assertTrue(html.startswith('<html>'))
        self.assertTrue(html.endswith('</html>'))
        # we want a <title> tag somewhere in the middle, with the words “To-Do lists” in it
        self.assertIn('<title>To-Do lists</title>', html)
