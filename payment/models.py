from django.db import models
from django.contrib.auth.models import User
from cook.models import Food
from decimal import Decimal

class Order(models.Model):
    eater = models.ForeignKey(User,
    on_delete = models.CASCADE
    )
    created_time = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=4, decimal_places=2,blank=False,null=False)
    payment_method = models.CharField(
        max_length=10,
        default='OTHER',
        null=False,
        choices=  [
            ('VISA', 'Visa'),
            ('PAYPAL', 'Paypal'),
            ]
    )
    payment_status = models.CharField(
            max_length=10,
            default='PENDING',
            null=False,
            choices=  [
                ('PENDING', 'Pendng'),
                ('REJECTED', 'Rejected'),
                ('COMPLETED', 'Completed'),
                ]
        )
