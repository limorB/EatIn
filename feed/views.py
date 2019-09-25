from django.shortcuts import render
from cook.models import Food
from myCart.models import Cart
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def display_feed(request):
    if request.method == 'GET' or request.method == 'POST':
        foods = Food.objects.all()
        foods_desc = foods.order_by('-created_at')
        print(foods_desc)

        return render(request,'feed/index.html',{'all_foods':foods_desc})


def create_cart(added_time,quantity,food_id,user_id):
    Cart(
    added_time=added_time,
    quantity=quantity,
    food_id=food_id,
    user_id=user_id).save()


def added_to_cart_message(request,text):
    return messages.success(request, text)



@login_required(login_url='/accoutns/login/')
def add_to_cart(request):
    if request.method == 'POST':
        added_time = timezone.now()
        food_id = int(request.POST['food_id'])
        user_id = request.user.id
        quantity = int(request.POST['quantity'])
        food_title = request.POST['food_title']
        carts = Cart.objects.filter(user_id=user_id)
        if len(carts)>0:
            for cart in carts:
                if cart.food_id == food_id:
                    cart.quantity += quantity
                    cart.save()

                else:
                    create_cart(added_time,quantity,food_id,user_id)

        else:
            create_cart(added_time,quantity,food_id,user_id)

    foods = Food.objects.all()
    foods_desc = foods.order_by('-created_at')
    mess_text = "{} was added to your cart".format(food_title)
    added_to_cart_message(request,mess_text)
    return render(request,'feed/index.html',{'all_foods':foods_desc})
