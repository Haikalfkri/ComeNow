from django.db import models
from authentication.models import CustomUser

# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=400, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    liked_by = models.ManyToManyField(CustomUser, related_name="post_like", blank=True)
    like_count = models.BigIntegerField(default=0)
    
    
    def __str__(self):
        return self.user.username