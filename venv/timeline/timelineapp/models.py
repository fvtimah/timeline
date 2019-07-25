from django.db import models
from django.forms import forms
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Schedules ( models.Model ):
    schedual_choices = (
        ('P' , 'Private') ,
        ('U' , 'Public') ,
    )
    type = models.CharField ( choices = schedual_choices , default = "U" , max_length = 1 )
    name = models.TextField ( blank = True , max_length = 10 )
    description = models.TextField ( blank = True )
    date = models.DateTimeField ( auto_now_add = True , null = True , blank = True )


class appointments ( models.Model ):
    appointments_day = (
        ('Sat' , 'Saturday') ,
        ('Sun' , 'Sunday') ,
        ('Mon' , 'Monday') ,
        ('Tue' , 'Tuesday') ,
        ('Wed' , 'Wednesday') ,
        ('Thu' , 'Thursday') ,
        ('Fr' , 'Friday') ,
    )
    day = models.CharField ( choices = appointments_day , default = "sa" , max_length = 2 )
    name = models.TextField ( max_length = 50 )
    schedule = models.ForeignKey ( Schedules , on_delete = models.SET_NULL , null = True )



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    web_page = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)


    @receiver ( post_save , sender = User )
    def create_user_profile(sender , instance , created , **kwargs):
        if created:
            Profile.objects.create ( user = instance )

    @receiver ( post_save , sender = User )
    def save_user_profile(sender , instance , **kwargs):
        instance.profile.save ()


