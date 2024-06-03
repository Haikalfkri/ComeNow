from django.db import models
from django.contrib.auth.models import AbstractUser 


# Create your models here.
class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    
    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default='user')