# booking/tests/test_forms.py
from django.test import TestCase
from datetime import date, time
from booking.forms import BookingForm
from booking.models import Court

class BookingFormTests(TestCase):

    def setUp(self):
        self.court = Court.objects.create(
            name="Court 1",
            court_type="indoor",
            surface_type="hard"
        )

    def test_booking_form_valid_data(self):
        """Form should be valid when given correct data"""
        form = BookingForm(data={
            'name': 'Roger Jones',
            'email': 'jones@example.com',
            'court': self.court.id,
            'date': date.today(),
            'start_time': time(11, 0),
            'end_time': time(13, 0),
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_booking_form_missing_field(self):
        """Form should be invalid when required fields are blank"""
        form = BookingForm(data={
            'name': '',
            'email': '',
            'court': '',
            'date': '',
            'start_time': '',
            'end_time': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)

    def test_booking_form_invalid_time(self):
        """Form should be invalid when end_time is before start_time"""
        form = BookingForm(data={
            'name': 'Francis Dacourt',
            'email': 'dacourt@example.com',
            'court': self.court.id,
            'date': date.today(),
            'start_time': time(14, 0),
            'end_time': time(12, 0),
        })
        self.assertFalse(form.is_valid())
