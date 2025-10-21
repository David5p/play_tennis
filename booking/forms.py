from django import forms
from .models import Booking
from datetime import date, time,  timedelta, datetime
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
    TIME_CHOICES = [(time(h, 0), f"{h:02d}:00")for h in range(7,21)]
    
    start_time = forms.ChoiceField(choices = TIME_CHOICES)
    end_time = forms.ChoiceField(choices = TIME_CHOICES)

    class Meta:
        model = Booking
        fields = ['court', 'name', 'email', 'date', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date',
                                           'min': date.today()
                                           .strftime('%Y-%m-%d')}), 
        }

     def clean_date(self):
        """Validate form logic so booking in the past cannot be made"""
        selected_date = self.cleaned_data['date']
        if selected_date < date.today():
            raise ValidationError("You cannot book a date in the past.")
        return selected_date

    def __init__(self, *args, **kwargs):
        """Accept user from view for conflict checking."""
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_start_time(self):
        """Convert the selected string back to a Python time object."""
        value = self.cleaned_data['start_time']
        if not value:
            raise forms.ValidationError("Please select a start time.")
        return time.fromisoformat(value)
    
    def clean_end_time(self):
        """Auto-set end_time to one hour after start_time if not manually chosen."""
        start = self.cleaned_data.get('start_time')
        end = self.cleaned_data.get('end_time')

        if start and not end:
            # If user didn’t choose duration, automatically add 1 hour
            dt = datetime.combine(datetime.today(), start) + timedelta(hours=1)
            return dt.time()

        if end:
            return time.fromisoformat(end)

        raise forms.ValidationError("Please select an end time.")
    
    
    def clean(self):
        """Prevent overlapping bookings for the same user."""
        cleaned_data = super().clean()
        user = self.user
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if user and date and start_time and end_time:
            from .models import Booking
            overlap = Booking.objects.filter(
                user=user, date=date,
                start_time__lt=end_time,
                end_time__gt=start_time,
            ).exists()

            if overlap:
                raise ValidationError("You already have a booking at this time.")

        return cleaned_data