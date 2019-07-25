from django.urls import path, include
from django.contrib import admin
from timelineapp import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = (
    path ( '' , main ) ,
    path ( 'schedules/details/<int:schedual_id>/' , schedules , ) ,
    path ( 'schedules/<int:schedual_id>/' , appointments , name = 'appointments' ) ,
    path ( 'schedule/new/' , views.schedule_new , name = 'schedule_new' ) ,
    path ( 'schedulelist/' , views.schedulelist , name = 'schedulelist' ) ,
    path ( 'appointment_new/' , views.appointment_new , name = 'appointment_new' ) ,
    path ( 'appointmentslist/' , views.appointmentslist , name = 'appointmentslist' ) ,
)

