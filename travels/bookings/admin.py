from django.contrib import admin
from .models import Bus,Seat , Booking
# Register your models here.

class BusAdmin(admin.ModelAdmin):
    list_display=('bus_name','bus_number','bus_origin','bus_destination')


class SeatAdmin(admin.ModelAdmin):
    list_display=('seat_number','bus','seat_isbooked')

class BookingAdmin(admin.ModelAdmin):
    list_display=('user','bus','seat','booking_time')

admin.site.register(Bus,BusAdmin)
admin.site.register(Seat,SeatAdmin)
admin.site.register(Booking,BookingAdmin)