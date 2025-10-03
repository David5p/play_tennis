from django.http import HttpResponse


def booking_home(request):
    return HttpResponse("Hello, booking!")

