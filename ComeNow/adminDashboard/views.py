from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from .forms import CreateEventForm
from events.models import EventModel

# Create your views here.
def adminDashboard(request):
    return render(request, "adminDashboard/dashboard.html")


def EventList(request):
    events = EventModel.objects.all()
    context = {
        'events': events,
    }
    return render(request, "adminDashboard/event-list.html", context)


def CreateEvent(request):
    if request.method == "POST":
        form = CreateEventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Create Event Successfully")
            return redirect("create-event")
    else:
        form = CreateEventForm()
        
    context = {
        'form': form,
    }
    
    return render(request, "adminDashboard/create-event.html", context)


def updateEvent(request, id):
    event = EventModel.objects.get(id=id)
    if request.method == "POST":
        form = CreateEventForm(request.POST, request.FILES, instance=event)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Update succesfully")
            return redirect("event-list")
    else:
        form = CreateEventForm(instance=event)
    
    context = {
        'event': event,
        'form': form
    }
    
    return render(request, "adminDashboard/update-page.html", context)