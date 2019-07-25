from django import forms
from django.contrib.auth.models import User

from .models import Schedules, appointments, Profile

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedules
        fields = {'name' , 'description' , }


class AppointmentsForm ( forms.ModelForm ):
    class Meta:
        model = appointments
        fields = "__all__"


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'location', 'birth_date')


