from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from cook.models import Food
from payment.models import Order

class CartItem(models.Model):
    order = models.ForeignKey(Order,on_delete = models.SET_NULL,null=True,default=None)
    user = models.ForeignKey(User,
    on_delete = models.CASCADE
    )
    food = models.ForeignKey(Food,
    on_delete = models.CASCADE
    )
    added_time = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(blank=False,null=False)
