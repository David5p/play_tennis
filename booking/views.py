from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')


@login_required(login_url='login') #Only logged in users can create a booking
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user # Link booking to the logged in user
            booking.save()
            messages.success(request, "Your booking was successful!")
            return redirect('create_booking')
    else:
        form = BookingForm()
    
    return render(request, 'booking/create_booking.html',{'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})