from django.contrib import admin
from .models import EventsNews
from .models import FeaturedEventsNews
from .models import Staffs
from .models import News, AcademicCalendar,Imagegallery,EventDetail,maingalleryimages,Gallery

# Register your models here.
class EventDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime', 'details', 'location')
admin.site.register(EventDetail,EventDetailAdmin)

class FeaturedAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description', 'location')
admin.site.register(FeaturedEventsNews,FeaturedAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('event', 'image')

admin.site.register(Imagegallery,GalleryAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation','mobile','qualification')

admin.site.register(Staffs,StaffAdmin)
