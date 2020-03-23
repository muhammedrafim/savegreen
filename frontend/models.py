from django.db import models

# Create your models here.
class EventsNews(models.Model):
    title = models.TextField()
    date = models.DateField()
    location = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    eventtype = models.TextField()

class FeaturedEventsNews(models.Model):
    title = models.TextField()
    date = models.DateField()
    location = models.TextField()
    description = models.TextField()

class Teachers(models.Model):
    name = models.TextField()
    subject = models.TextField()
    qualification = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    facebook = models.URLField()
    google = models.URLField()
    linkedin = models.URLField()
    mobile = models.IntegerField()

class News(models.Model):
    title = models.TextField()
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='pics')

class AcademicCalendar(models.Model):
    title = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
