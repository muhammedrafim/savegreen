from django.db import models

# Create your models here.
class EventsNews(models.Model):
    choice = [('SPORTS', 'Sports'),('ADMISSION', 'Admission') ,('ACADEMIC', 'Academic')]
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
    videourl = models.TextField(max_length=500)
    def __str__(self):
        return self.title
class Imagegallery(models.Model):
    image = models.ImageField(upload_to='pics')
    event = models.ForeignKey(EventDetail, on_delete=models.CASCADE)

class Gallery(models.Model):
    title = models.TextField()
    displayimage = models.ImageField(upload_to='gallery')
class maingalleryimages(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery')
