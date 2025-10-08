from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['court', 'name', 'email', 'date', 'start_time', 'end_time']
        widget = {
            'date': forms.DateInput(attrs={'type': 'date'}), 
            'start_time': forms.TimeInput(attrs={'type': 'time', 'step': 3600}),
            'end_time': forms.TimeInput(attrs={'type': 'time','step': 3600}),
        }