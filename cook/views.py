from django.shortcuts import render
from .forms import FoodForm
from .models import Food
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from accounts.views import login_view


# @login_required(login_url='accounts/login/')
def food_upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FoodForm(request.POST,request.FILES)
            print(form)
            if form.is_valid():
                print("form is valid")
                food = form.save(commit=False)
                food.user = request.user
                food.created_at = timezone.now()
                food.save()
                context = {'form':form}
                # messages.success(request, 'your post was uploaded')
                return redirect('/eatin/')

            else:
                messages.error(request, 'oops something went wrong, try again')
        form = FoodForm()
        context = {"form":form}
        return render(request, 'cook/index.html',context)
    else:
        print("you are not logged in")
        return login_view(request)
