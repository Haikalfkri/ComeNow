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
    
    def get_comment_count(self):
        return self.posts_comment.count()
    class Meta:
        verbose_name_plural = "Posts"
    
    

class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="posts_comment")
    created = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username
    
    
    class Meta:
        verbose_name_plural = "Comments"