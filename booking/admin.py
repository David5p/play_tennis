from django.contrib import admin
from.models import Court, Booking
# Register your models here.

@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('name', 'court_type')
    list_filter = ('court_type',)
    search_fields = ('name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'court', 'date', 'start_time', 'end_time', 'created_at')
    list_filter = ('court', 'date')
    search_fields = ('name', 'email')

