from datetime import timezone
from typing import Dict , Any

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.checks import messages
from django.db import transaction
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import *
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

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


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()





@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.CheckMessage(request,('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.ERROR(request,('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'Timelineapp/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


