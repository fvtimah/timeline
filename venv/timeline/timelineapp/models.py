from django.db import models


# Create your models here.
class Schedules  (models.Model):
    booking = models.TextField()
    schedule = models.TextField()

