from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bus(models.Model):
    bus_name=models.CharField(max_length=100)
    bus_number=models.CharField(max_length=20,unique=True)
    bus_origin=models.CharField(max_length=50)
    bus_destination=models.CharField(max_length=50)
    bus_seats=models.PositiveBigIntegerField()
    bus_features=models.TextField()
    bus_starttime=models.TimeField()
    bus_reachtime=models.TimeField()
    bus_no_of_seats=models.PositiveBigIntegerField()
    bus_price=models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return f"{self.bus_name} {self.bus_origin}-{self.bus_destination}"
    
class Seat(models.Model):
    bus = models.ForeignKey('Bus' , on_delete=models.CASCADE , related_name='seats')
    seat_number=models.CharField(max_length=10)
    seat_isbooked=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bus}-{self.seat_number}"


class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat,on_delete=models.CASCADE)
    booking_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.bus.bus_name}-{self.bus.bus_starttime}-{self.bus.bus_reachtime}-{self.seat.seat_number}"