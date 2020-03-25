from django.contrib import admin
from .models import EventsNews
from .models import FeaturedEventsNews
from .models import Teachers
from .models import News, AcademicCalendar,Imagegallery,EventDetail,maingalleryimages,Gallery

# Register your models here.
admin.site.register(EventsNews)
admin.site.register(FeaturedEventsNews)
admin.site.register(Teachers)
admin.site.register(News)
admin.site.register(AcademicCalendar)
admin.site.register(Imagegallery)
admin.site.register(EventDetail)
admin.site.register(maingalleryimages)
admin.site.register(Gallery)
