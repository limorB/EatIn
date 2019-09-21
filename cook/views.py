from django.shortcuts import render
from .forms import FoodForm
from .models import Food
from django.contrib import messages
from django.utils import timezone

#
# def food_upload(request):
#
#     return render(request, 'cook/index.html')


def food_upload(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            print("this is the form: {} after form.save".format(form))
            food.user = request.user
            print("see user below")
            print(food.user)
            food.created_at = timezone.now()
            food.save()
            context = {'form':form}
            return render(request, 'feed/index.html')

        else:
            messages.error(request, 'oops something went wrong, try again')
    form = FoodForm()
    context = {"form":form}
    return render(request, 'cook/index.html',context)
