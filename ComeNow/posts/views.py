from django.shortcuts import render

# Create your views here.
def UserPosts(request):
    return render(request, "post/post.html")