from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index),
    path('academic.html', views.academic),
    path('preschool.html', views.preschool),
    path('preschool-summer-camp.html', views.preschoolsummer),
    path('admission.html', views.admission),
    path('events.html', views.events),
    path('event-single.html', views.eventssingle),
    path('gallery.html', views.gallery),
    path('about.html', views.about),
    path('contact.html', views.contact),
    path('academic-arts.html', views.academic_arts),
    path('academic-athletics.html', views.academic_athletics),
    path('academic-curriculum.html', views.academic_curriculum),
    path('academic-calendar.html', views.academic_calendar),
    path('curriculum.html', views.curriculum),

]