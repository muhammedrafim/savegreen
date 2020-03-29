from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index),
    path('academic.html', views.academic , name='academic'),
    path('preschool.html', views.preschool),
    path('preschool-summer-camp.html', views.preschoolsummer),
    path('admission.html', views.admission, name='admission'),
    path('events.html', views.events,name='events'),
    path('event-single.html', views.eventssingle),
    path('gallery.html', views.gallery , name='gallerys'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('academic-arts.html', views.academic_arts),
    path('academic-athletics.html', views.academic_athletics),
    path('academic-curriculum.html', views.academic_curriculum),
    path('academic-calendar.html', views.academic_calendar),
    path('curriculum.html', views.curriculum),
    path('event/<event_id>/',views.eventdetail, name='event'),
    path('gallery/<gallery_id>/', views.showgallery, name='gallery')

]