from django import forms
from .models import Booking
from datetime import time,  timedelta, datetime

class BookingForm(forms.ModelForm):
    TIME_CHOICES = [(time(h, 0), f"{h:02d}:00")for h in range(7,21)]
    
    start_time = forms.ChoiceField(choices = TIME_CHOICES)
    end_time = forms.ChoiceField(choices = TIME_CHOICES)

    class Meta:
        model = Booking
        fields = ['court', 'name', 'email', 'date', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}), 
        }
    
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