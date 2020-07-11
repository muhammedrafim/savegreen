from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index),
    path('events.html', views.events,name='events'),
    path('event-single.html', views.eventssingle),
    path('event/<event_id>/',views.eventdetail, name='event'),

]