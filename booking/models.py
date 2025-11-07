from django.db import models
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from datetime import time
from django.contrib.auth.models import User

# Create your models here.


class Court (models.Model):
    COURT_TYPE_CHOICES = [
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
    ]
    SURFACE_CHOICES = [
        ('clay', 'Clay'),
        ('hard', 'Hard'),
    ]

    name = models.CharField(max_length=100)
    court_type = models.CharField(max_length=10, choices=COURT_TYPE_CHOICES)
    surface_type = models.CharField(
        max_length=10, choices=SURFACE_CHOICES, default='hard')

    def clean(self):
        """Custom validation to prevent clay courts from being indoor"""
        if self.court_type == 'indoor' and self.surface_type == 'clay':
            raise ValidationError("Indoor courts are hard courts only.")

    def save(self, *args, **kwargs):
        """Ensure validation runs before saving"""
        self.full_clean()  # ensures clean() runs before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.name} ({self.get_court_type_display()}) - "
            f"({self.get_surface_type_display()})"
        )


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    court = models.ForeignKey(
        Court, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """Run all validation checks for a booking"""
        super().clean()
        self._validate_time_on_the_hour()
        self._validate_time_order()
        self._validate_opening_hours()
        self._validate_outdoor_availability()
        self._validate_maximum_duration()
        self._validate_no_overlap()

    def _validate_time_on_the_hour(self):
        """Ensure booking times are on the hour"""
        # Skip validation if times are not provided (handled by form)
        if not self.start_time or not self.end_time:
            return
        if self.start_time.minute != 0 or self.start_time.second != 0:
            raise ValidationError(
                "Start time must be on the hour (e.g., 8:00, 9:00).")
        if self.end_time.minute != 0 or self.end_time.second != 0:
            raise ValidationError(
                "End time must be on the hour (e.g., 9:00, 10:00).")

    def _validate_time_order(self):
        """Ensures end time is after start time"""
        # Skip validation if times are not provided (handled by form)
        if not self.start_time or not self.end_time:
            return
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time.")

    def _validate_opening_hours(self):
        """Opening hours of venue"""
        if not self.start_time or not self.end_time:
            return
        opening_time = time(7, 0)
        closing_time = time(21, 0) if (
            self.user and self.user.is_staff) else time(20, 0)
        if not (opening_time <= self.start_time <
                closing_time):
            raise ValidationError(
                "Bookings can only start between 7:00 and 21:00.")
        if not (opening_time < self.end_time <= closing_time):
            raise ValidationError(
                "Bookings can only end between 7:00 and 21:00.")

    def _validate_outdoor_availability(self):
        """Block courts for bookings in winter"""
        try:
            court = self.court
        except ObjectDoesNotExist:
            return  # Skip if no court assigned

        if not self.date:
            return  # Skip if no date assigned

        if court.court_type == 'outdoor' and self.date.month in [12, 1, 2, 3]:
            raise ValidationError(
                "Outdoor courts are closed from December to March.")

    def _validate_no_overlap(self):
        """Prevent double bookings"""
        try:
            if (
                not self.court
                or not self.date
                or not self.start_time
                or not self.end_time
            ):

                return
            overlapping = Booking.objects.filter(
                court=self.court,
                date=self.date,
                start_time__lt=self.end_time,
                end_time__gt=self.start_time
            )
            # Exclude the current booking when editing an existing one
            if self.pk:
                overlapping = overlapping.exclude(pk=self.pk)

            if overlapping.exists():
                raise ValidationError(
                    "This court is already booked for that time slot.")
        except ObjectDoesNotExist:
            # If any related object is missing, skip this check
            return

    def _validate_maximum_duration(self):
        """No single booking can be more than 3 hours."""
        if not self.start_time or not self.end_time:
            return

        duration_hours = (self.end_time.hour
                          - self.start_time.hour)
        if duration_hours > 3:
            raise ValidationError(
                "You cannot book a court for more than 3 hours "
                "in a single booking."
            )

    def save(self, *args, **kwargs):
        """Ensure validation runs before saving"""
        self.full_clean()  # runs clean() before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.name} - {self.court.name} on {self.date} "
            f"from {self.start_time} to {self.end_time}"
        )
