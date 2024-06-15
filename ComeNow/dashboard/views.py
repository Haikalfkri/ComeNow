from django.shortcuts import render, redirect
from django.db.models import Case, When, Value, BooleanField
from django.contrib import messages

from events.models import EventModel
from authentication.models import CustomUser
from .forms import CreateEventForm, UserForm
from authentication.forms import UserRegistrationForm

# Create your views here.
def dashboardAdmin(request):
    return render(request, "dashboard/dash-admin/dashboard.html")


# Event Management

def eventList(request):
    events = EventModel.objects.all().order_by('-event_date')
    context = {
        'events': events,
    }
    return render(request, "dashboard/dash-admin/event-list.html", context)


def createEvent(request):
    if request.method == 'POST':
        form = CreateEventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Create Event Succesfull")
            return redirect('event-list')
    else:
        form = CreateEventForm()
        
    context = {
        'form': form
    }
    return render(request, "dashboard/dash-admin/create-event.html", context)


def updateEvent(request, event_id):
    event = EventModel.objects.get(id=event_id)
    if request.method == "POST":
        form = CreateEventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Update Successfull")
            return redirect('event-list')
    else:
        form = CreateEventForm(instance=event)
        
    context = {
        'form': form
    }
    
    return render(request, "dashboard/dash-admin/update-event.html", context)

def deleteEvent(request, event_id):
    event = EventModel.objects.get(id=event_id)
    event.delete()
    messages.success(request, "Delete Successfull")
    return redirect('event-list')
    


# User Manegement

def userList(request):
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
    return render(request, "dashboard/dash-admin/user-list.html", context)


def createUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Create User Successfull")
            return redirect("user-list")
    else:
        form = UserRegistrationForm()
        
    context = {
        'form': form
    }
    
    return render(request, "dashboard/dash-admin/create-user.html", context)


def userUpdate(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Update Successfull")
            return redirect('user-list')
    else:
        form = UserForm(instance=user)
        
    context = {
        'form': form
    }
    
    return render(request, "dashboard/dash-admin/user-update.html", context)


def deleteUser(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.delete()
    messages.success(request, "Delete Successfull")
    return redirect('user-list')



