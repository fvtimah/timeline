from datetime import timezone
from typing import Dict , Any

from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import *
from django.urls import reverse

from .models import Schedules,appointments as Appointment


# Create your views here.

def main(request):
    return render ( request , 'timelineapp/main.html' , {} , )


def schedules(request , schedual_id= None):
    schedual = get_object_or_404 (Schedules, pk =schedual_id)
    context = {'schedual': schedual}
    return render ( request , 'timelineapp/index.html' , context , )


def appointments(request , schedual_id=None):
    schedual = get_object_or_404 (Schedules, pk =schedual_id)
    appointments = Appointment.objects.filter ( schedule = schedual )
    context = {'appointments': appointments}
    return render ( request , 'timelineapp/appointments.html' , context , )


def schedulelist(request):
    schedulelist= Schedules.objects.all()
    return render ( request , 'timelineapp/schedulelist.html' , {'schedulelist': schedulelist} , )


def appointmentslist(request):
    appointmentslist = Appointment.objects.all ()
    return render ( request , 'timelineapp/appointmentslist.html' , {'appointmentslist': appointmentslist},)



def schedule_new(request):
    if request.method == 'POST':
        form = ScheduleForm ( request.POST )
        if form.is_valid ():
            Schedules = form.save ( commit = False )
            Schedules.type = request.user
            Schedules.description = request.user
            schedules.date = timezone
            Schedules.save ()
        return redirect (reverse ('timelineapp:schedulelist') )
    else:
        form = ScheduleForm()
        return render ( request , 'timelineapp/schedule_new.html' , {'form': form} )





def appointment_new (request):
    if request.method == 'POST':
        form = AppointmentsForm (request.POST)
        if form.is_valid():
            Appointment=form.save( commit = False)
            Appointment.name= request.user
            Appointment.day = request.user
            Appointment.Schedules= request.user
            Appointment.save()
        return redirect (reverse ('timelineapp:appointmentslist') )
    else:
        form = AppointmentsForm()
        return render (request, 'timelineapp/appointment_new.html', {'form': form})
