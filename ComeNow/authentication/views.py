from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm

# Create your views here.
@login_required
def redirect_base_on_role_and_group(request):
    user = request.user
    
    if user.role == 'admin' and user.groups.filter(name='admin').exists():
        return redirect('admin-home')
    elif user.role == 'user' and user.groups.filter(name='user').exists():
        return redirect('user-home')
    else:
        messages.error(request, "You don't have any permission")
        return redirect('login')



def UserRegister(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            group = Group.objects.get(name='user')
            user.groups.add(group)
            
            messages.success(request, "Register Succesfully")
            return redirect('login')
        else:
            messages.error(request, "Invalid Register")
    else:
        form = UserRegistrationForm()
    
    context = {
        'form': form
    }
    
    return render(request, "authentication/register.html", context)


def UserLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('events')
            else:
                messages.error(request, "Invalid login")
    
    return render(request, "authentication/login.html")


def UserLogout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('login')