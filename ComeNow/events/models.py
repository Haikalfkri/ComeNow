from django.db import models

# Create your models here.
class EventModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    contact = models.CharField(max_length=12)
    event_date = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)
    more_information = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url