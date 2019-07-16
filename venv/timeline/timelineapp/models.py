from django.db import models
from django.forms import forms


# Create your models here.
class Schedules (models.Model):
    schedual_choices = (
        ('P' , 'Private') ,
        ('U' , 'Public') ,
    )
    type = models.CharField( choices = schedual_choices ,default="U",max_length = 1 )
    name = models.TextField(blank = True, max_length = 10)
    description = models.TextField ( blank = True )
    date = models.DateTimeField ( auto_now_add = True, null=True, blank=True )




class appointments(models.Model):
    appointments_day = (
        ('Sat' , 'Saturday'),
        ('Sun','Sunday'),
        ('Mon', 'Monday'),
        ('Tue','Tuesday'),
        ('Wed','Wednesday'),
        ('Thu', 'Thursday'),
        ('Fr', 'Friday'),
    )
    day= models.CharField( choices = appointments_day,default="sa",max_length=2)
    name= models.TextField(max_length = 50)
    schedule = models.ForeignKey(Schedules, on_delete=models.SET_NULL, null=True )




