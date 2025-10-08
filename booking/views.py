from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm


def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking was successful!")
            return redirect('create_booking')
    else:
        form = BookingForm()
    
    return render(request, 'booking/create_booking.html',{'form': form})


