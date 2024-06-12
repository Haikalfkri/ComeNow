from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from events.models import EventModel
from authentication.models import CustomUser

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
    if request.POST.get('action') == 'post':
        result = ''
        id = int(request.POST.get('eventid'))
        event = get_object_or_404(EventModel, id=id)
        if event.likes.filter(id=request.user.id).exists():
            event.likes.remove(request.user)
            event.like_count -= 1
            result = event.like_count
            event.save()
        else:
            event.likes.add(request.user)
            event.like_count += 1
            result = event.like_count
            event.save()

        return JsonResponse({'result': result})