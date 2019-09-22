from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,
    on_delete = models.CASCADE,
    primary_key=True,
    )
    address = models.CharField(max_length=80,default=None,null=True)
    Type = models.CharField(
        max_length=10,
        default='EATER',
        null=False,
        choices=  [
            ('COOK', 'Cook'),
            ('EATER', 'Eater'),
            ('BOTH', 'Both'),
            ]
    )
