from django.shortcuts import render
from cook.models import Food
from myCart.models import CartItem,Order
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def display_feed(request):
    if request.method == 'GET' or request.method == 'POST':
        #show only food items with quantity greater than 0
        foods = Food.objects.filter(quantity__gt=0)
        for food in foods:
            print(food.quantity)

        foods_desc = foods.order_by('-created_at')

        return render(request,'feed/index.html',{'all_foods':foods_desc})


def create_cart(added_time,quantity,food_id,user_id):
    CartItem(
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
        if (request.POST['quantity']).isdigit():
            quantity = int(request.POST['quantity'])

            food_title = request.POST['food_title']
            cart_items = CartItem.objects.filter(user_id=user_id,order_id__isnull=True)
        # try with CartItem.objects.count()
            if len(cart_items)>0:
                for item in cart_items:
                    if item.food_id == food_id:
                        item.quantity += quantity
                        item.save()

                    else:
                        create_cart(added_time,quantity,food_id,user_id)
                        mess_text = "{} was added to your cart".format(food_title)
                        added_to_cart_message(request,mess_text)

            else:
                create_cart(added_time,quantity,food_id,user_id)
                mess_text = "{} was added to your cart".format(food_title)
                added_to_cart_message(request,mess_text)
        else:
            quantity = 0
            messages.warning(request, "please specify the desired amount")

    foods = Food.objects.filter(quantity__gt=0)
    foods_desc = foods.order_by('-created_at')
    return render(request,'feed/index.html',{'all_foods':foods_desc})
