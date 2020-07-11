from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import EventsNews, FeaturedEventsNews,  Staffs,  News, AcademicCalendar,Imagegallery, EventDetail ,Gallery,maingalleryimages
from django.core.paginator import Paginator
from django.contrib.auth.models import auth,User

def index(request):
    eventnews = EventDetail.objects.all().order_by('-id')[:3]
    eventtypes = EventsNews.objects.all().distinct('eventtype')
    featuredevent = FeaturedEventsNews.objects.all()
    teachers = Staffs.objects.all()
    news = News.objects.all()
    return render(request, "index.html", {'eventnews': eventnews,'news': news, 'eventtypes': eventtypes,'featuredevent':featuredevent, 'teachers': teachers})
def preschool(request):
    #st = Student.objects.all()
    return render(request,"preschool.html", )
def preschoolsummer(request):
    return render(request,"preschool-summer-camp.html")
def admission(request):
    return render(request,"admission.html")

def events(request):
    events = EventDetail.objects.all().order_by('-id')
    featuredevent = FeaturedEventsNews.objects.all()
    paginator = Paginator(events, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,"events.html", {'posts' : posts, 'featuredevent': featuredevent})

def eventssingle(request):
    return render(request, "event-single.html")

def gallery(request):
    _gallery = Gallery.objects.all()
    return render(request, "gallery.html" , {"gallery": _gallery})
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


def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            users = User.objects.get(username=username)
            if users.groups.filter(name='students').exists():
                auth.login(request,user)
                return redirect('student_dashboard')
            elif users.groups.filter(name='teachers').exists():
                auth.login(request,user)
                return redirect('teacher_dashboard')
    else :
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')