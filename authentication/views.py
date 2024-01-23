from .models import CustomUser

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from . models import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user_category = request.POST['user_category']
        password2 = request.POST.get('password2')

        if password != password2:
            messages.info(request, "Password is not Matching")
            return redirect('/auth/signup/')

        try:
            if CustomUser.objects.get(username=username):
                messages.warning(request, "User name  is already Taken")
                return redirect('/auth/signup/')

        except Exception as identifier:
            pass

        user = CustomUser.objects.create_user(
            username=username, password=password, user_category=user_category)
        user.save()
        messages.success(request, "User is Created Please Login")
        # login(request, user)
        return redirect('/auth/login/')  # Redirect to your home page

    return render(request, 'signup.html')


def sys_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,
                            username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/auth/login/')

    return render(request, 'login.html')


def handleLogout(request):
    logout(request)
    messages.success(request, "Logout Success")
    return redirect('/auth/login')
# views.py


def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})
