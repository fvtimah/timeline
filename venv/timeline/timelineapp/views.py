from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def main (request):
    return render(request, 'timelineapp/main.html', {},)

def booking(request):
    return render(request, 'timelineapp/booking.html', {},)

def schedule(request):
    return render(request, 'timelineapp/schedule.html', {},)


