from django.shortcuts import render,redirect
from myCart.models import Cart
from cook.models import Food
from django.utils import timezone
from .forms import PaymentForm




def display_checkout(request):
    if request.method == 'GET':
        user_id = request.user.id
        cart_items = Cart.objects.filter(user_id=user_id)
        count_items = cart_items.count()
        if count_items == 0:
            messages.info(request, "Your bag is empty")
            context = {}
        else:
            created_time = timezone.now()
            total_price = 0
            for item in cart_items:
                sub_total = item.quantity*item.food.price
                total_price += sub_total
            form = PaymentForm()
            context = {
                        "cart_items":cart_items,
                        "count_items":count_items,
                        "total_price":total_price,
                        "form":form,

                        }
        return render(request, 'payment/index.html',context)
    else:
        return make_payment(request)





def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.eater_id = request.user.id
            order.created_time = timezone.now()
            cart_items = Cart.objects.filter(user_id=order.eater_id)
            total_price = 0
            for item in cart_items:
                sub_total = item.quantity*item.food.price
                total_price += sub_total
                #updating the food quantity
                food = Food.objects.get(id=item.food_id)
                food.quantity-=item.quantity
                print(food.quantity)
                print(item.quantity)
                food.save()
                #

            order.total_price = total_price
            order.save()
            #saving the order_id in cart_items
            for item in cart_items:
                item.order_id = order.id
                item.save()



    return render(request, 'payment/success.html')


# def update_feed_quantity(request):
