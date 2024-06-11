from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from events.models import EventModel, Likes

# Create your views here.
def EventView(request):
    events = EventModel.objects.all().order_by('-event_date')
    context = {
        'events': events
    }
    
    return render(request, "events/events.html", context)


def DetailPage(request, id):
    event = EventModel.objects.get(id=id)
    status = event.get_status
    
    context = {
        'event': event,
        'status': status,
    }
    
    return render(request, "events/detailPage.html", context)


@login_required
def like(request, event_id):
    user = request.user
    event = EventModel.objects.get(id=event_id)
    current_likes = event.likes
    liked = Likes.objects.filter(user=user, event=event).count()
    
    if not liked:
        liked = Likes.objects.create(user=user, event=event)
        current_likes += 1
        liked = True
    else:
        liked = Likes.objects.filter(user=user, event=event).delete()
        current_likes -= 1
        liked = False
        
        
    event.likes = current_likes
    event.save()
    
    return HttpResponseRedirect(reverse('events'))