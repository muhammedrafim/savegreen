from django.shortcuts import render
from django.http import HttpResponse
from .models import EventsNews, FeaturedEventsNews,  Teachers,  News, AcademicCalendar,Imagegallery, EventDetail ,Gallery,maingalleryimages
from django.core.paginator import Paginator


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
    events = EventDetail.objects.all()
    featuredevent = FeaturedEventsNews.objects.all()
    paginator = Paginator(events, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,"events.html", {'posts' : posts, 'featuredevent': featuredevent})

def eventssingle(request):
    return render(request, "event-single.html")

def gallery(request):
    _gallery = Gallery.objects.all()
    return render(request, "gallery.html" , {"gallery": _gallery})
def about(request):
    teachers = Teachers.objects.all()
    return render(request, "about.html",{"teachers" : teachers})
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


def eventdetail(request, event_id):
    event = EventDetail.objects.get(id=event_id)
    images = Imagegallery.objects.all().filter(event_id=event_id)
    return render(request , 'event-single.html', {"events": event ,"images" : images })


def showgallery(request, gallery_id):
    gallery = Gallery.objects.get(id=gallery_id)
    images = maingalleryimages.objects.all().filter(gallery_id =gallery_id)
    print(images)
    return render(request, 'viewgallery.html', {"images": images} )