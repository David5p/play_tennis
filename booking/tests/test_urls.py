from django.test import SimpleTestCase
from django.urls import reverse, resolve
from booking.views import home, create_booking, my_bookings, register
from booking import views

class TestUrls(SimpleTestCase):
    def test_urls_resolve_to_correct_view(self):
        url_view_map = {
            'home': views.home,
            'create_booking': views.create_booking,
            'my_bookings': views.my_bookings,
            'register': views.register,
        }

        for url_name, view_func in url_view_map.items():
            url = reverse(url_name)
            self.assertEqual(resolve(url).func, view_func)