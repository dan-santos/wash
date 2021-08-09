from django.shortcuts import render
from django.http import HttpResponse

def list_bookings(request):
    return HttpResponse('Lista de reservas disponíveis')