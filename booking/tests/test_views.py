from django.test import TestCase, Client
from django.urls import reverse
from booking.models import Court, Booking
from django.contrib.auth.models import User
from datetime import date, time


class TestViews(TestCase):

    def setUp(self):
        """
        Set up test environment with a test client.
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.court = Court.objects.create(
            name='Court 1', court_type='outdoor', surface_type='clay')

        # URL names
        self.urls = {
            'home': reverse('home'),
            'create_booking': reverse('create_booking'),
            'my_bookings': reverse('my_bookings'),
            'register': reverse('register'),
        }

    def test_urls_load_correctly(self):
        """Test return status 200 or redirect to other page"""
        for name, url in self.urls.items():
            if name == 'my_bookings' or name == 'create_booking':
                # login required
                response = self.client.get(url)
                self.assertNotEqual(response.status_code, 200)
            else:
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_create_booking_view_logged_in_user(self):
        """Ensure a user logged in can make a booking"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('create_booking'), {
            'court': self.court.id,
            'date': date.today().isoformat(),
            'start_time': time(16, 0),
            'end_time': time(18, 0),
            'name': 'Test User',
            'email': 'test@example.com',
        })
        self.assertIn(response.status_code, [200, 302])
        self.assertTrue(Booking.objects.exists())

    def test_my_bookings_view_requires_login(self):
        """Redirects if user not logged in"""
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 302)

        # User logs in
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 200)
