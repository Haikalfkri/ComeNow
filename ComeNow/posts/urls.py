from django.urls import path

from posts import views

urlpatterns = [
    path("posts/", views.UserPosts, name="posts"),
    path("post-like/", views.PostLike, name="post-like"),
]
