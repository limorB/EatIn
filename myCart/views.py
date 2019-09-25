from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cart
from cook.models import Food
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import pdb


@login_required(login_url='/accoutns/login/')
def display_cart(request):
    if request.method == 'GET':
        user_id = request.user.id
        carts = Cart.objects.filter(user_id=user_id)
        all_foods_list = []
        if len(carts)>0:
            for cart in carts:
                food = Food.objects.get(pk = cart.food_id)
                print(food.description)
                all_foods_list.append(food)
        else:
            print("your cart is empty")
            messages.info(request, "your cart is empty")
            return render(request, 'mycart/index.html')


    return render(request, 'mycart/index.html',{'foods':all_foods_list})


@login_required(login_url='/accoutns/login/')
def remove_from_cart(request):
    if request.method == 'POST':
        print("i got here")
        user_id = request.user.id
        food_id = int(request.POST['food_id'])
        cart = Cart.objects.get(user_id=user_id,food_id=food_id)
        print(cart.id)
        return display_cart(request)
    else:
        print("this is a get")
    return display_cart(request)
