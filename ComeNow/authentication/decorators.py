from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("events")
        else:
            return views_func(request, *args, **kwargs)
    return wrapper_func