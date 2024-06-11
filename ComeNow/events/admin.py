from django.contrib import admin
from .models import EventModel, EventCategories, Likes

# Register your models here.
admin.site.register(EventModel)
admin.site.register(EventCategories)
admin.site.register(Likes)