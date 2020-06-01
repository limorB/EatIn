from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
from .models import Profile
from .forms import RegistrationForm,ProfileRegForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from feed.views import display_feed
from payment.models import Order
from cook.models import Food
from myCart.models import CartItem






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


def myorders(request):
    if request.user.is_authenticated:
        eater_id = request.user.id
        orders = Order.objects.filter(eater_id=eater_id)
        orders_dict = {}
        orders_dict['orders'] = orders
        orders_dict['cart_items'] = []
        for order in orders:
            item = CartItem.objects.get(order_id = order.id)
            orders_dict['cart_items'].append(item)

        return render(request,'accounts/myorders.html',orders_dict)


    else:
        # when user isn't login he will be redirected to the login page
        return login_view(request)


def settings(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print("this is the user name {}".format(request.user.username))
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
            else:
                messages.error(request, 'Please correct the error below.')

        else:
            password_form = PasswordChangeForm(request.user)



    else:
        # when user isn't login he will be redirected to the login page
        return login_view(request)

    return render(request,'accounts/settings.html',{"user":request.user,"password_form": password_form})
