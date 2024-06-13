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
    
    context = {
        'event': event,
        'status': status,
    }
    
    return render(request, "events/detailPage.html", context)


@login_required
def eventLike(request):
    event_id = request.POST.get('event_id')
    event = get_object_or_404(EventModel, id=event_id)
    
    if event.liked_by.filter(id=request.user.id).exists():
        event.liked_by.remove(request.user)
    else:
        event.liked_by.add(request.user)
        
    return redirect('detail-page', id=event_id)