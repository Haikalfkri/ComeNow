from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Posts

# Create your views here.
@login_required
def UserPosts(request):
    user = request.user
    posts = Posts.objects.all().order_by('-created')
    if request.method == "POST":
        post_body = request.POST.get('post')
        
        post = Posts.objects.create(user=user, body=post_body)
        post.save()
        
        return redirect("posts")

    context = {
        'posts': posts
    }
    
    return render(request, "post/post.html", context)

@login_required
def PostLike(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Posts, id=post_id)
    
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
        post.like_count -= 1
    else:
        post.liked_by.add(request.user)
        post.like_count += 1
        
    post.save()
    return redirect("posts")


@login_required()
def PostComment(request):
    return render(request, "comments.html")