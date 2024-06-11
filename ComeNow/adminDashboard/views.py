from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When, Value, BooleanField

from .forms import CreateEventForm, UserForm
from events.models import EventModel
from authentication.models import CustomUser

# Create your views here.
@login_required
def adminDashboard(request):
    return render(request, "adminDashboard/dashboard.html")



# User Management View

@login_required
def UserList(request):
    users = CustomUser.objects.all().annotate(
        is_admin=Case(
            When(role='admin', then=Value(True)),
            default=Value(False),
            output_field=BooleanField(),
        )
    ).order_by('-is_admin', 'role', 'username')
    
    context = {
        'users': users,
    }
    return render(request, "adminDashboard/user-list.html", context)


@login_required
def UpdateUser(request, id):
    user = CustomUser.objects.get(id=id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Update Successfully")
            return redirect('user-list')
    else:
        form = UserForm(instance=user)
        
    context = {
        'form': form,
    }
    
    return render(request, "adminDashboard/update-user.html", context)


@login_required
def DeleteUser(request, id):
    user = CustomUser.objects.get(id=id)
    user.delete()
    messages.success(request, "Delete Successfully")
    return redirect('user-list')



# Event Management Views

@login_required
def EventList(request):
    events = EventModel.objects.all()
    context = {
        'events': events,
    }
    return render(request, "adminDashboard/event-list.html", context)


@login_required
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


@login_required
def updateEvent(request, id):
    event = EventModel.objects.get(id=id)
    if request.method == "POST":
        form = CreateEventForm(request.POST, request.FILES, instance=event)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Update Succesfully")
            return redirect("event-list")
    else:
        form = CreateEventForm(instance=event)
    
    context = {
        'event': event,
        'form': form
    }
    
    return render(request, "adminDashboard/update-page.html", context)


@login_required
def deleteEvent(request, id):
    event = EventModel.objects.get(id=id)
    event.delete()
    messages.success(request, "Delete Successfully")
    return redirect("event-list")