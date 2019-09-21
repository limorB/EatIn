from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Food(models.Model):
    user = models.ForeignKey(User,
    on_delete = models.CASCADE
    )
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(blank=False,null=False)
    image = models.ImageField(upload_to = 'images/',default=None,blank=True)
