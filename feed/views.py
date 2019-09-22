from django.shortcuts import render
from django.http import HttpResponse
from cook.models import Food
from myCart.models import Cart
from django.utils import timezone



def display_feed(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        foods_desc = foods.order_by('-created_at')

        return render(request,'feed/index.html',{'all_foods':foods_desc})



def add_to_cart(request,food_id):
    if request.method == 'POST':
        added_time = timezone.now()
        user = User.objects.get(user_id = request.user.id)
        food = Food.objects.get(id=food_id)
        print("added_time:{},user:{},food:{}".format(added_time,user,food))


    return render(request,'feed/index.html')
