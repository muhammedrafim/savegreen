from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from fcm.utils import get_device_model


class EventsNews(models.Model):
    choice = [('SPORTS', 'Sports'), ('ADMISSION', 'Admission'), ('ACADEMIC', 'Academic')]
    title = models.TextField()
    date = models.DateField()
    location = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    eventtype = models.TextField(choices=choice)


class FeaturedEventsNews(models.Model):
    title = models.TextField()
    date = models.DateField()
    location = models.TextField()
    description = models.TextField()


class Staffs(models.Model):
    name = models.TextField()
    designation = models.TextField()
    qualification = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    facebook = models.URLField()
    google = models.URLField()
    linkedin = models.URLField()
    mobile = models.IntegerField()

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.TextField()
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='pics')


class AcademicCalendar(models.Model):
    title = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()


class EventDetail(models.Model):
    title = models.TextField(max_length=30)
    datetime = models.DateTimeField()
    location = models.TextField(max_length=25)
    description = models.TextField()
    details = models.TextField()
    displayImage = models.ImageField(upload_to='pics')
    videourl = models.TextField(max_length=500,default="")

    def __str__(self):
        return self.title


def sendmsg(sender,instance,**kwargs):
    Device = get_device_model()

    Device.objects.all().send_message({'message': instance.title,'title':'SAVEGREEN AWCS','icon':'http://127.0.0.1:8000/static/img/slider/slide4.jpg','click':'http://127.0.0.1:8000/home/event/'+str(instance.id)})



class Imagegallery(models.Model):
    image = models.ImageField(upload_to='pics')
    event = models.ForeignKey(EventDetail, on_delete=models.CASCADE)


class Gallery(models.Model):
    title = models.TextField()
    displayimage = models.ImageField(upload_to='gallery')


class maingalleryimages(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery')
post_save.connect(sendmsg, sender=EventDetail)
