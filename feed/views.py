from django.shortcuts import render
from cook.models import Food
from myCart.models import Cart
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist




def display_feed(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        foods_desc = foods.order_by('-created_at')

        return render(request,'feed/index.html',{'all_foods':foods_desc})


@login_required(login_url='/accoutns/login/')
def add_to_cart(request):
    if request.method == 'POST':
        added_time = timezone.now()
        food_id = int(request.POST['food_id'])
        user_id = request.user.id
        quantity = int(request.POST['quantity'])
        carts = Cart.objects.filter(user_id=user_id)
        if len(carts)>0:
            for cart in carts:
                if cart.food_id == food_id:
                    cart.quantity += quantity
                    cart.save()

                else:
                    Cart(
                    added_time=added_time,
                    quantity=quantity,
                    food_id=food_id,
                    user_id=user_id).save()

        else:
            Cart(
            added_time=added_time,
            quantity=quantity,
            food_id=food_id,
            user_id=user_id).save()

    return render(request,'feed/index.html')









# @login_required(login_url='/accoutns/login/')
# def add_to_cart(request):
#     if request.method == 'POST':
#         added_time = timezone.now()
#         food_id = request.POST['food_id']
#         user_id = request.user.id
#         quantity = request.POST['quantity']
#         cart, created = Cart.objects.get_or_create(
#         user_id = user_id,
#         defaults={
#         'food_id': food_id,
#         'added_time':added_time,
#         'quantity':quantity}
#         )
#         # print(created)
#         # print(cart[0])
#         # print(created)
#         if not created:
#             print(created)
#             Cart(
#             added_time=added_time,
#             quantity=quantity,
#             food_id=food_id,
#             user_id=user_id).save()






        # return render(request,'feed/index.html')
