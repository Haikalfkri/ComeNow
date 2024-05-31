from django.shortcuts import render
from events.models import EventModel

# Create your views here.
def EventView(request):
    events = EventModel.objects.all()
    
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