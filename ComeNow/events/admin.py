from django.contrib import admin
from .models import EventModel, EventCategories

# Register your models here.
admin.site.register(EventModel)
admin.site.register(EventCategories)