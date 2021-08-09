from django.conf.urls import url
from django.urls import path

from .views import list_bookings

app_name = 'booking'

urlpatterns = [
    path('', list_bookings, name='list'),
]