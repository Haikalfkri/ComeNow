from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Case, When, Value, BooleanField
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


from events.models import EventModel
from authentication.models import CustomUser, UserProfile
from .forms import CreateEventForm, UserForm, UpdateProfileForm, LastandFirstNameForm
from authentication.forms import UserRegistrationForm
from .decorators import allowed_users

# Create your views here.

# dashboard admin

# Event Management
@login_required
@allowed_users(allowed_roles=['admin'])
def eventList(request):
    events = EventModel.objects.all().order_by('-event_date')
    context = {
        'events': events,
    }
    return render(request, "dashboard/dash-admin/event-list.html", context)


@login_required
@allowed_users(allowed_roles=['admin'])
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


@login_required
@allowed_users(allowed_roles=['admin'])
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


@login_required
@allowed_users(allowed_roles=['admin'])
def deleteEvent(request, event_id):
    event = EventModel.objects.get(id=event_id)
    event.delete()
    messages.success(request, "Delete Successfull")
    return redirect('event-list')
    

# User Manegement
@login_required
@allowed_users(allowed_roles=['admin'])
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


@login_required
@allowed_users(allowed_roles=['admin'])
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


@login_required
@allowed_users(allowed_roles=['admin'])
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


@login_required
@allowed_users(allowed_roles=['admin'])
def deleteUser(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.delete()
    messages.success(request, "Delete Successfull")
    return redirect('user-list')



# user dashboard

@login_required
@allowed_users(allowed_roles=['user'])
def eventLike(request):
    user = request.user
    liked_events = EventModel.objects.filter(liked_by=user)
    context = {
        'liked_events': liked_events
    }
        
    return render(request, "dashboard/dash-user/event-like.html", context)


@login_required
@allowed_users(allowed_roles=['user'])
def eventSaved(request):
    user = request.user
    saved_events = EventModel.objects.filter(favorites=user)
    context = {
        'saved_events': saved_events
    }
    
    return render(request, "dashboard/dash-user/event-saved.html", context)


@login_required
@allowed_users(allowed_roles=['user'])
def userOverview(request, id):
    user = get_object_or_404(CustomUser, id=id)
    user_profile = get_object_or_404(UserProfile, username=user)
    context = {
        'user_profile': user_profile,
        'user': user,
    }
    
    return render(request, "dashboard/dash-user/overview.html", context)


@login_required
@allowed_users(allowed_roles=['user'])
def userProfile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    profile = get_object_or_404(UserProfile, username=user)
    
    profile_picture_url = profile.get_profile_image_url()
    
    if request.method == 'POST':
        user_form = LastandFirstNameForm(request.POST, instance=user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Update Successfully")
            return redirect('update-profiles', user_id=user_id)
    else:
        user_form = LastandFirstNameForm(instance=user)
        profile_form = UpdateProfileForm(instance=profile)
        
    context = {
        'profile_form': profile_form,
        'user_form': user_form,
        'profile_picture_url': profile_picture_url
    }
    
    return render(request, "dashboard/dash-user/profile-view.html", context)


class PasswordsChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "dashboard/dash-user/password-change-view.html"
    success_url = reverse_lazy('change-password-profile')
    success_message = "Password Change Successfull"