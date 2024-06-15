from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from events.models import EventModel

# Create your views here.
def EventView(request):
    events = EventModel.objects.all().order_by('-event_date')
    context = {
        'events': events
    }
    
    return render(request, "events/events.html", context)


def DetailPage(request, id):
    event = get_object_or_404(EventModel, id=id)
    status = event.get_status
    like_count = event.like_count
    
    context = {
        'event': event,
        'status': status,
        'like_count': like_count,
    }
    
    return render(request, "events/detailPage.html", context)


@login_required
def eventLike(request):
    event_id = request.POST.get('event_id')
    event = get_object_or_404(EventModel, id=event_id)
    
    if event.liked_by.filter(id=request.user.id).exists():
        event.liked_by.remove(request.user)
        event.liked_count -= 1
    else:
        event.liked_by.add(request.user)
        event.liked_count += 1
    
    event.save()
    return redirect('detail-page', id=event_id)


@login_required
def eventFav(request):
    event_id = request.POST.get('event_id')
    event = get_object_or_404(EventModel, id=event_id)
    
    if event.favorites.filter(id=request.user.id).exists():
        event.favorites.remove(request.user)
        event.favorites_count -= 1
    else:
        event.favorites.add(request.user)
        event.favorites_count += 1
    
    event.save()
    return redirect('detail-page', id=event_id)


def aboutPage(request):
    return render(request, "base/about.html")


def contactPage(request):
    return render(request, "base/contact.html")