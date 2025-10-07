from django.db import models
from django.core.exceptions import ValidationError

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
    surface_type = models.CharField(max_length=10, choices=SURFACE_CHOICES, default = 'hard')

    def clean(self):
        "Custom validation to prevent clay courts from being indoor"
        if self.court_type == 'indoor' and self.surface_type == 'clay':
            raise ValidationError("Indoor courts are hard courts only.")
    
    def save(self, *args, **kwargs):
        "Ensure validation runs before saving"
        self.full_clean()  # ensures clean() runs before saving
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name} ({self.get_court_type_display()}) - ({self.get_surface_type_display()})"

class Booking(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        """Validation for time order and overlap prevention"""
        #Ensures end time is after start time
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time.")
        
        # Prevent overlapping bookings
        overlapping = Booking.objects.filter(
            court=self.court,
            date=self.date,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        ).exclude(id=self.id)

        if overlapping.exists():
            raise ValidationError("This court is already booked for that time slot.")
    
    def save(self, *args, **kwargs):
        """Ensure validation runs before saving"""
        self.full_clean()  # runs clean() before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.court.name} on {self.date} from {self.start_time} to {self.end_time}"
