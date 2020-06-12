from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Food(models.Model):
    user = models.ForeignKey(User,
    on_delete = models.CASCADE
    )
    title = models.CharField(max_length=20,null=True)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(blank=False,null=False)
    image = models.ImageField(upload_to='media/images', default=None,blank=True)
    category = models.CharField(
        max_length=50,
        default='OTHER',
        null=False,
        choices= [
            ('ITALIAN', 'Italian'),
            ('DESERT', 'Desert'),
            ('BEVERAGES', 'Beverages'),
            ('THAI', 'Thai'),
            ('SUSHI', 'Sushi'),
            ('INADIAN', 'Indian'),
            ('MEDITERRANEAN','Mediterranean'),
            ('CHINESE','Chinese'),
            ('AMERICAN','American'),
            ('VIETNAMESE','Vietnamese'),
            ('GLUTEN-FREE','Gluten-Free'),
            ('VEGAN','Vegan'),
            ('SALAD','Salad'),
            ('ASIAN','Asian'),
            ('SOUP','Soup'),
            ('GREEK','Greek'),
            ('JAPANESE','Japanese'),
            ('HOME-COOKING','Home-Cooking'),
            ('OTHER','Other')

            ]
    )
