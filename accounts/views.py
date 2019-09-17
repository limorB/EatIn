from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
from .models import Profile
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
import pdb



def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            #form.save return a user (if valid)
            context = {'form':form}
            messages.success(request, 'You are now logged in.')
            return render(request,'feed/index.html',context)
        else:
            messages.error(request, 'oops something went wrong, try again')

    else:
        form = RegistrationForm()

    context = {'form':form}
    return render(request,'accounts/registration.html',context)



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/feed/')

    else:
        form = AuthenticationForm(request.POST)

    context = {'form':form}
    return render(request,'accounts/login.html',context)



def logout_view(request):
    if request.method == "POST":
        logout(request)
        #django knows which user is now logged in so we don't need to pass the current user
        return redirect('/accounts/login/')
