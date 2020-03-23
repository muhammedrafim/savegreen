from django.shortcuts import render
from django.http import HttpResponse
from .models import EventsNews
from .models import FeaturedEventsNews
from .models import Teachers
from .models import News, AcademicCalendar
def index(request):
    eventnews = EventsNews.objects.all()
    eventtypes = EventsNews.objects.all().distinct('eventtype')
    featuredevent = FeaturedEventsNews.objects.all()
    teachers = Teachers.objects.all()
    news = News.objects.all()
    return render(request, "index.html", {'eventnews': eventnews,'news': news, 'eventtypes': eventtypes,'featuredevent':featuredevent, 'teachers': teachers})
def academic(request):
    teachers = Teachers.objects.all();
    return render(request,"academic.html", {'teachers':teachers})
def preschool(request):
    return render(request,"preschool.html")
def preschoolsummer(request):
    return render(request,"preschool-summer-camp.html")
def admission(request):
    return render(request,"admission.html")
def events(request):
    return render(request,"events.html")
def eventssingle(request):
    return render(request, "event-single.html")
def gallery(request):
    return render(request, "gallery.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")


def academic_arts(request):
    return render(request, "academic-arts.html")


def academic_athletics(request):
    return render(request, "academic-athletics.html")


def academic_curriculum(request):
    return render(request, 'academic-curriculum.html')


def academic_calendar(request):
    calendar = AcademicCalendar.objects.all()
    return render(request, 'academic-calendar.html', {'calendar':calendar})


def curriculum(request):
    return render(request, 'curriculum.html')