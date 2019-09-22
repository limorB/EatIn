from django.shortcuts import render
from .forms import FoodForm
from .models import Food
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required


# @login_required(login_url='accoutns/login/')
def food_upload(request):
    if request.method == 'POST':
        form = FoodForm(request.POST,request.FILES)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user
            food.created_at = timezone.now()
            food.save()
            context = {'form':form}
            messages.success(request, 'your post was uploaded,hungry people are on the way')
            return redirect('/feed/')

        else:
            messages.error(request, 'oops something went wrong, try again')
    form = FoodForm()
    context = {"form":form}
    return render(request, 'cook/index.html',context)
