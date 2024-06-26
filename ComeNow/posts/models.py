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
    
    class Meta:
        verbose_name_plural = "Posts"
    
    

class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    posts = models.ManyToManyField(CustomUser, related_name="posts_comment")
    created = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=500)
    
    def __str__(self):
        return self.user.username
    
    
    class Meta:
        verbose_name_plural = "Comments"