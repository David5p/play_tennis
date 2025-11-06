from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.utils import timezone
from .models import Booking
from .forms import BookingForm


def home(request):
    return render(request, 'home.html')


def user_has_conflicting_booking(user, date, start_time, end_time):
    """
    Returns True if this user already has a booking at the same time.
    """
    return Booking.objects.filter(
        user=user,
        date=date,
        start_time__lt=end_time,
        end_time__gt=start_time
    ).exists()


class CustomLoginView(LoginView):
    def form_valid(self, form):
        messages.success(
            self.request, f"Welcome back, {form.get_user().username}!")
        return super().form_valid(form)


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')


@login_required(login_url='login')
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.name = request.user.get_full_name() or request.user.username

            # Use the helper directly here
            if user_has_conflicting_booking(
                request.user, booking.date, booking.start_time, booking.end_time
            ):
                messages.error(
                    request, "You already have a booking at that time.")
                return redirect('create_booking')

            booking.save()
            messages.success(request, "Your booking was successful!")
            return redirect('my_bookings')

    else:
        form = BookingForm(user=request.user)

    return render(request, 'booking/create_booking.html', {'form': form})


def register(request):
    """Simple user registration view."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, "Your account has been created successfully!")
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'booking/register.html', {'form': form})


@login_required(login_url='login')
def my_bookings(request):
    today = timezone.now().date()
    upcoming = Booking.objects.filter(
        user=request.user, date__gte=today).order_by('date')
    past = Booking.objects.filter(
        user=request.user, date__lt=today).order_by('-date')
    return render(request, 'booking/my_bookings.html', {
        'upcoming': upcoming,
        'past': past
    })


@login_required
def cancel_booking(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)

        # Prevent cancelling past bookings
        if booking.date < timezone.now().date():
            messages.error(request, "You cannot cancel past bookings.")
            return redirect('my_bookings')

        # Delete only upcoming booking
        booking.delete()
        messages.success(request, "Your booking has been cancelled.")
        return redirect('my_bookings')

    # Redirect if GET request
    return redirect('my_bookings')


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    # Prevent cancelling past bookings
    if booking.date < timezone.now().date():
        messages.error(request, "You cannot edit past bookings.")
        return redirect('my_bookings')

    # edit only upcoming booking
    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user, instance=booking)
        if form.is_valid():
            updated_booking = form.save(commit=False)
            overlap = Booking.objects.filter(
                user=request.user,
                date=updated_booking.date,
                start_time__lt=updated_booking.end_time,
                end_time__gt=updated_booking.start_time
            ).exclude(id=booking.id).exists()

            if overlap:
                messages.error(
                    request, "This change clashes with another booking.")
                return redirect('edit_booking', booking_id=booking.id)

            updated_booking.save()
            messages.success(
                request, "Your booking has been updated successfully.")
            return redirect('my_bookings')
    else:
        form = BookingForm(user=request.user, instance=booking)

    return render(request, 'booking/edit_booking.html',
                  {'form': form, 'booking': booking})
