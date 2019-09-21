from django.shortcuts import render
from django.http import HttpResponse
from cook.models import Food


def display_feed(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        foods_desc = foods.order_by('-created_at')
        print(foods_desc)

        return render(request,'feed/index.html',{'all_foods':foods_desc})

# Create your views here.
