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
        if len(carts) == 0:
            messages.info(request, "your cart is empty")

    return render(request, 'mycart/index.html',{'carts':carts})


@login_required(login_url='/accoutns/login/')
def remove_from_cart(request,id):
    if request.method == 'GET':
        user_id = request.user.id
        cart = Cart.objects.get(pk=id)
        cart.delete()
    return display_cart(request)

# @login_required(login_url='/accoutns/login/')
def update_quantity(request,id):
    cart = Cart.objects.get(pk=id)
    quantity  = request.GET['quantity']
    cart.quantity = quantity
    cart.save()

    print("cart id: {}".format(id))
    print(request.GET['quantity'])


    return render(request, 'mycart/index.html')
