from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
from .models import Profile
from .forms import RegistrationForm,ProfileRegForm
from django.contrib.auth.forms import AuthenticationForm
from feed.views import display_feed





def registration(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = ProfileRegForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            user = user_form.save()
            login(request,user)
            messages.success(request, 'You are now logged in.')

            return display_feed(request)
        else:
            messages.error(request, 'oops something went wrong, try again')

    else:
        user_form = RegistrationForm()
        profile_form = ProfileRegForm()

    context = {'user_form':user_form,'profile_form':profile_form}
    return render(request,'accounts/registration.html',context)




def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return display_feed(request)

    else:
        form = AuthenticationForm(request.POST)

    context = {'form':form}
    return render(request,'accounts/login.html',context)



def logout_view(request):
    if request.method == "POST":
        logout(request)

        return redirect('/accounts/login/')
