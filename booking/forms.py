from django import forms
from .models import Booking
from datetime import time

class BookingForm(forms.ModelForm):
    TIME_CHOICES = [(time(h, 0), f"{h:02d}:00")for h in range(7,22)]
    
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
        return time.fromisoformat(value)
    
    def clean_end_time(self):
        "Convert the selected string back to a Python time object"""
        value = self.cleaned_data['end_time']
        return time.fromisoformat(value)