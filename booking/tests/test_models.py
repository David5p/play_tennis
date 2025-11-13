from django.test import TestCase
from booking.models import Court, Booking
from django.contrib.auth.models import User
from datetime import date, time


class BookingModelTests(TestCase):
    def setUp(self):
        """
        Create a test user and a sample Court object for use in tests.
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.court = Court.objects.create(
            name='Court 1', court_type='indoor', surface_type='hard')

    def test_time_on_the_hour_validation(self):
        """
        Test that Booking objects raise a ValidationError if start_time
        or end_time are not on the hour.
        """
        from django.core.exceptions import ValidationError
        booking = Booking(
            user=self.user,
            court=self.court,
            name='Test',
            email='test@example.com',
            date=date.today(),
            start_time=time(16, 30),  # invalid time booking
            end_time=time(17, 30)
        )
        with self.assertRaises(ValidationError):
            booking.full_clean()

    def test_valid_booking_saves(self):
        """
        Test that a Booking with valid on-the-hour times
        is saved successfully.
        """
        booking = Booking(
            user=self.user,
            court=self.court,
            name='Test',
            email='test@example.com',
            date=date.today(),
            start_time=time(16, 0),
            end_time=time(17, 0)
        )
        booking.full_clean()
        booking.save()
        self.assertTrue(Booking.objects.exists())
