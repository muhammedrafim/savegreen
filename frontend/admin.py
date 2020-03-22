from django.contrib import admin
from .models import EventsNews
from .models import FeaturedEventsNews
from .models import Teachers
from .models import News
# Register your models here.
admin.site.register(EventsNews)
admin.site.register(FeaturedEventsNews)
admin.site.register(Teachers)
admin.site.register(News)