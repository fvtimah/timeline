from django import forms
from .models import Schedules, appointments



class ScheduleForm (forms.ModelForm):
    class Meta:
        model = Schedules
        fields = {'name', 'description', }


class AppointmentsForm (forms.ModelForm):
    class Meta:
        model = appointments
        fields = "__all__"

