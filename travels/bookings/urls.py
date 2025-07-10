#from django.contrib import admin
from django.urls import path
from .views import RegisterView,LoginView,BusListCreateView,BusDetailView,BookingView,UserBookingView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('buses/',BusListCreateView.as_view(),name='buslist'),
    path('buses/<int:pk>/',BusDetailView.as_view(),name='busdetail'),
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('user/<int:user_id>/bookings/',UserBookingView.as_view(), name='user-booings'),
    path('booking/',BookingView.as_view(),name='bookings')

]