from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    
    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default='user')
    

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    phone_number = PhoneNumberField(blank=True)
    education = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="Profiles/", default="Profiles/default_image.jpg")
    
    follow = models.ManyToManyField(CustomUser, related_name="follow", blank=True)
    follow_count = models.BigIntegerField(default=0)
    
    def profileImageUrl(self):
        try:
            url = self.profile_picture.url
        except:
            url = ''
        return url
        
    
    def __str__(self):
        return f"{self.username.username}'s profile"