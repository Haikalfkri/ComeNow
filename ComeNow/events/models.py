from django.db import models
from django.utils import timezone

from authentication.models import CustomUser

# Create your models here.
class EventCategories(models.Model):
    category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category

class EventModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    contact = models.CharField(max_length=12)
    event_date = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)
    event_category = models.ForeignKey(EventCategories, on_delete=models.CASCADE)
    more_information = models.CharField(max_length=255)
    
    liked_by = models.ManyToManyField(CustomUser, related_name="event_like", blank=True)
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def get_status(self):
        now = timezone.now()
        if now.date() == self.event_date.date():
            if now.hour == self.event_date.hour:
                return "Start"
            elif now < self.event_date:
                return "Upcoming"
        elif now < self.event_date:
            return "Upcoming"
        return "Ended"


    @property
    def like_count(self):
        total = 0
        try:
           total = self.liked_by.count() 
        except:
            total = 0
        return total

    
    def __str__(self):
        return self.name