from django.test import SimpleTestCase
from django.urls import reverse, resolve
from booking.views import home, create_booking, my_bookings, register

class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_create_booking_url_resolves(self):
        url = reverse('create_booking')
        self.assertEqual(resolve(url).func, create_booking)

    def test_my_bookings_url_resolves(self):
        url = reverse('my_bookings')
        self.assertEqual(resolve(url).func, my_bookings)
    
    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)
